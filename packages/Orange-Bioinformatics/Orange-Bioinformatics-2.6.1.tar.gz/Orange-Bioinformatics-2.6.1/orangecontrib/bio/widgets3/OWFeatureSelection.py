# -*- coding: utf-8 -*-
"""
Differential Gene Expression
----------------------------

"""
import sys
import itertools
from collections import defaultdict

import numpy as np
import scipy.stats

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import pyqtSignal as Signal

import pyqtgraph as pg

import Orange.data

from Orange.widgets import widget, gui, settings
from Orange.widgets.utils.datacaching import data_hints

from .OWVulcanoPlot import LabelSelectionWidget


def score_fold_change(a, b, axis=0):
    """
    Calculate the fold change between `a` and `b` samples.

    Parameters
    ----------
    a, b : array
        Arrays containing the samples
    axis : int
        Axis over which to compute the FC

    Returns
    -------
    FC : array
        The FC scores
    """
    mean_a = np.nanmean(a, axis=axis)
    mean_b = np.nanmean(b, axis=axis)
    return mean_a / mean_b


def score_log_fold_change(a, b, axis=0):
    """
    Return the log2(FC).

    See Also
    --------
    score_fold_change

    """
    return np.log2(score_fold_change(a, b, axis=axis))


def score_ttest(a, b, axis=0):
    T, P = scipy.stats.ttest_ind(a, b, axis=axis)
    return T, P


def score_ttest_t(a, b, axis=0):
    T, _ = score_ttest(a, b, axis=axis)
    return T


def score_ttest_p(a, b, axis=0):
    _, P = score_ttest(a, b, axis=axis)
    return P


def score_anova(*arrays, axis=0):
    arrays = [np.asarray(arr, dtype=float) for arr in arrays]

    if not len(arrays) > 1:
        raise TypeError("Need at least 2 positional arguments")

    if not 0 <= axis < 2:
        raise ValueError("0 <= axis < 2")

    if not all(arrays[i].ndim == arrays[i + 1].ndim
               for i in range(len(arrays) - 2)):
        raise ValueError("All arrays must have the same number of dimensions")

    if axis >= arrays[0].ndim:
        raise ValueError()

    if axis == 0:
        arrays = [arr.T for arr in arrays]

    scores = [scipy.stats.f_oneway(*ars) for ars in zip(*arrays)]
    F, P = zip(*scores)
    return np.array(F, dtype=float), np.array(P, dtype=float)


def score_anova_f(*arrays, axis=0):
    F, _ = score_anova(*arrays, axis=axis)
    return F


def score_anova_p(*arrays, axis=0):
    _, P = score_anova(*arrays, axis=axis)
    return P


def score_signal_to_noise(a, b, axis=0):
    mean_a = np.nanmean(a, axis=axis)
    mean_b = np.nanmean(b, axis=axis)

    std_a = np.nanstd(a, axis=axis, ddof=1)
    std_b = np.nanstd(b, axis=axis, ddof=1)

    return (mean_a - mean_b) / (std_a + std_b)


def score_mann_whitney(a, b, axis=0):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)

    if not 0 <= axis < 2:
        raise ValueError("Axis")

    if a.ndim != b.ndim:
        raise ValueError

    if axis >= a.ndim:
        raise ValueError

    if axis == 0:
        a, b = a.T, b.T

    res = [scipy.stats.mannwhitneyu(a_, b_) for a_, b_ in zip(a, b)]
    U, P = zip(*res)
    return np.array(U), np.array(P)


class InfiniteLine(pg.InfiniteLine):
    def paint(self, painter, option, widget=None):
        brect = self.boundingRect()
        c = brect.center()
        line = QtCore.QLineF(brect.left(), c.y(), brect.right(), c.y())
        t = painter.transform()
        line = t.map(line)
        painter.save()
        painter.resetTransform()
        painter.setPen(self.currentPen)
        painter.drawLine(line)
        painter.restore()


class Histogram(pg.PlotWidget):
    """
    A histogram plot with interactive 'tail' selection
    """
    #: Emitted when the selection boundary has changed
    selectionChanged = Signal()
    #: Emitted when the selection boundary has been edited by the user
    #: (by dragging the boundary lines)
    selectionEdited = Signal()

    #: Selection mode
    NoSelection, Low, High, TwoSided, Middle = 0, 1, 2, 3, 4

    def __init__(self, parent=None, **kwargs):
        pg.PlotWidget.__init__(self, parent, **kwargs)

        self.getAxis("bottom").setLabel("Score")
        self.getAxis("left").setLabel("Counts")

        self.__data = None
        self.__histcurve = None

        self.__mode = Histogram.NoSelection
        self.__min = 0
        self.__max = 0

        def makeline(pos):
            pen = QtGui.QPen(Qt.darkGray, 1)
            pen.setCosmetic(True)
            line = InfiniteLine(angle=90, pos=pos, pen=pen, movable=True)
            line.setCursor(Qt.SizeHorCursor)
            return line

        self.__cuthigh = makeline(self.__max)
        self.__cuthigh.sigPositionChanged.connect(self.__on_cuthigh_changed)
        self.__cuthigh.sigPositionChangeFinished.connect(self.selectionEdited)
        self.__cutlow = makeline(self.__min)
        self.__cutlow.sigPositionChanged.connect(self.__on_cutlow_changed)
        self.__cutlow.sigPositionChangeFinished.connect(self.selectionEdited)

        brush = pg.mkBrush((200, 200, 200, 180))
        self.__taillow = pg.PlotCurveItem(
            fillLevel=0, brush=brush, pen=QtGui.QPen(Qt.NoPen))
        self.__taillow.setVisible(False)

        self.__tailhigh = pg.PlotCurveItem(
            fillLevel=0, brush=brush, pen=QtGui.QPen(Qt.NoPen))
        self.__tailhigh.setVisible(False)

    def setData(self, hist, bins=None):
        """
        Set the histogram data
        """
        if bins is None:
            bins = np.arange(len(hist))

        self.__data = (hist, bins)
        if self.__histcurve is None:
            self.__histcurve = pg.PlotCurveItem(
                x=bins, y=hist, stepMode=True
            )
        else:
            self.__histcurve.setData(x=bins, y=hist, stepMode=True)

        self.__update()

    def setHistogramCurve(self, curveitem):
        """
        Set the histogram plot curve.
        """
        if self.__histcurve is curveitem:
            return

        if self.__histcurve is not None:
            self.removeItem(self.__histcurve)
            self.__histcurve = None
            self.__data = None

        if curveitem is not None:
            if not curveitem.opts["stepMode"]:
                raise ValueError("The curve must have `stepMode == True`")
            self.addItem(curveitem)
            self.__histcurve = curveitem
            self.__data = (curveitem.yData, curveitem.xData)

        self.__update()

    def histogramCurve(self):
        """
        Return the histogram plot curve.
        """
        return self.__histcurve

    def setSelectionMode(self, mode):
        """
        Set selection mode
        """
        if self.__mode != mode:
            self.__mode = mode
            self.__update_cutlines()
            self.__update_tails()

    def setLower(self, value):
        """
        Set the lower boundary value.
        """
        if self.__min != value:
            self.__min = value
            self.__update_cutlines()
            self.__update_tails()
            self.selectionChanged.emit()

    def setUpper(self, value):
        """
        Set the upper boundary value.
        """
        if self.__max != value:
            self.__max = value
            self.__update_cutlines()
            self.__update_tails()
            self.selectionChanged.emit()

    def setBoundary(self, lower, upper):
        """
        Set lower and upper boundary value.
        """
        changed = False
        if self.__min != lower:
            self.__min = lower
            changed = True

        if self.__max != upper:
            self.__max = upper
            changed = True

        if changed:
            self.__update_cutlines()
            self.__update_tails()
            self.selectionChanged.emit()

    def boundary(self):
        """
        Return the lower and upper boundary values.
        """
        return (self.__min, self.__max)

    def clear(self):
        """
        Clear the plot.
        """
        self.__data = None
        self.__histcurve = None
        super().clear()

    def __update(self):
        def additem(item):
            if item.scene() is not self.scene():
                self.addItem(item)

        def removeitem(item):
            if item.scene() is self.scene():
                self.removeItem(item)

        if self.__data is not None:
            additem(self.__cuthigh)
            additem(self.__cutlow)
            additem(self.__tailhigh)
            additem(self.__taillow)

            _, edges = self.__data
            # Update the allowable cutoff line bounds
            minx, maxx = np.min(edges), np.max(edges)
            span = maxx - minx
            bounds = minx - span * 0.005, maxx + span * 0.005

            self.__cuthigh.setBounds(bounds)
            self.__cutlow.setBounds(bounds)

            self.__update_cutlines()
            self.__update_tails()
        else:
            removeitem(self.__cuthigh)
            removeitem(self.__cutlow)
            removeitem(self.__tailhigh)
            removeitem(self.__taillow)

    def __update_cutlines(self):
        self.__cuthigh.setVisible(self.__mode & Histogram.High)
        self.__cuthigh.setValue(self.__max)
        self.__cutlow.setVisible(self.__mode & Histogram.Low)
        self.__cutlow.setValue(self.__min)

    def __update_tails(self):
        if self.__mode == Histogram.NoSelection:
            return
        if self.__data is None:
            return

        hist, edges = self.__data

        self.__taillow.setVisible(self.__mode & Histogram.Low)
        if self.__min > edges[0]:
            datalow = histogram_cut(hist, edges, edges[0], self.__min)
            self.__taillow.setData(*datalow, fillLevel=0, stepMode=True)
        else:
            self.__taillow.clear()

        self.__tailhigh.setVisible(self.__mode & Histogram.High)
        if self.__max < edges[-1]:
            datahigh = histogram_cut(hist, edges, self.__max, edges[-1])
            self.__tailhigh.setData(*datahigh, fillLevel=0, stepMode=True)
        else:
            self.__tailhigh.clear()

    def __on_cuthigh_changed(self):
        self.setUpper(self.__cuthigh.value())

    def __on_cutlow_changed(self):
        self.setLower(self.__cutlow.value())


def histogram_cut(hist, bins, low, high):
    """
    Return a subset of a histogram between low and high values.

    Parameters
    ----------
    hist : (N, ) array
        The histogram values/counts for each bin.
    bins : (N + 1) array
        The histogram bin edges.
    low, high : float
        The lower and upper edge where to cut the histogram

    Returns
    -------
    histsubset : (M, ) array
        The histogram subset
    binssubset : (M + 1) array
        New histogram bins. The first and the last value are equal
        to `low` and `high` respectively.

    Note that in general the first and the final bin widths are
    different then the widths in the input bins

    """
    if len(bins) < 2:
        raise ValueError()

    if low >= high:
        raise ValueError()

    low = max(bins[0], low)
    high = min(bins[-1], high)

    if low <= bins[0]:
        lowidx = 0
    else:
        lowidx = np.searchsorted(bins, low, side="left")

    if high >= bins[-1]:
        highidx = len(bins)
    else:
        highidx = np.searchsorted(bins, high, side="right")

    cbins = bins[lowidx: highidx]
    chist = hist[lowidx: highidx - 1]

    if cbins[0] > low:
        cbins = np.r_[low, cbins]
        chist = np.r_[hist[lowidx - 1], chist]

    if cbins[-1] < high:
        cbins = np.r_[cbins, high]
        chist = np.r_[chist, hist[highidx - 1]]

    assert cbins.size == chist.size + 1
    return cbins, chist


def test_low(array, low, high):
    return array <= low


def test_high(array, low, high):
    return array >= high


def test_two_tail(array, low, high):
    return (array >= high) | (array <= low)


def test_middle(array, low, high):
    return (array <= high) | (array >= low)


class SetContextHandler(settings.ContextHandler):
    def __init__(self, match_imperfect=False):
        super().__init__()
        self.match_imperfect = match_imperfect

    def match(self, context, items):
        items = set(items)

        if self.match_imperfect:
            intersection, union = items & context.items, items | context.items
            if len(union) > 0:
                return len(intersection) / len(union)
            else:
                return 0
        else:
            return 2 if items == context.items else 0

    def new_context(self, items):
        ctx = super().new_context()
        ctx.items = frozenset(items)
        return ctx

    def settings_to_widget(self, widget):
        super().settings_to_widget(widget)

        context = widget.current_context
        if context is None:
            return

        for setting, data, instance in \
                self.provider.traverse_settings(context.values, widget):
            if isinstance(setting, settings.ContextSetting) and \
                    setting.name in data:
                value = self.decode_setting(settings, data[setting.name])
                setattr(instance, setting.name, value)


class OWFeatureSelection(widget.OWWidget):
    name = "Differential Expression"
    description = "Gene selection by differential expression analysis."
    icon = "../widgets/icons/GeneSelection.svg"
    priority = 1010

    inputs = [("Data", Orange.data.Table, "set_data")]
    outputs = [("Data subset", Orange.data.Table, widget.Default),
               ("Remaining data subset", Orange.data.Table),
               ("Selected genes", Orange.data.Table)]

    #: Selection types
    LowTail, HighTail, TwoTail = 1, 2, 3
    #: Test type - i.e a two sample (t-test, ...) or multi-sample (ANOVA) test
    TwoSampleTest, VarSampleTest = 1, 2
    #: Available scoring methods

    Scores = [
        ("Fold Change", TwoTail, TwoSampleTest, score_fold_change),
        ("log2(Fold Change)", TwoTail, TwoSampleTest, score_log_fold_change),
        ("T-test", TwoTail, TwoSampleTest, score_ttest_t),
        ("T-test P-value", LowTail, TwoSampleTest, score_ttest_p),
        ("ANOVA", HighTail, VarSampleTest, score_anova_f),
        ("ANOVA P-value", LowTail, VarSampleTest, score_anova_p),
        ("Signal to Noise Ratio", TwoTail, TwoSampleTest,
         score_signal_to_noise),
#         ("Info Gain", HighTail, TwoSampleTest, None),
#         ("Chi Square", HighTail, TwoSampleTest, None),
        ("Mann-Whitney", LowTail, TwoSampleTest, score_mann_whitney),
    ]

    settingsHandler = SetContextHandler()

    #: Selected score index.
    score_index = settings.Setting(0)
    #: Compute the null score distribution (label permutations).
    compute_null = settings.Setting(False)
    #: Number of permutations to for null score distribution.
    permutations_count = settings.Setting(20)
    #: Alpha value (significance) for the selection on background
    #: null score distribution.
    alpha_value = settings.Setting(0.01)
    #: N best for the fixed best N scores selection.
    n_best = settings.Setting(20)

    #: Stored thresholds for scores.
    thresholds = settings.Setting({
        "Fold Change": (0.5, 2.),
        "log2(Fold Change)": (-1, 1),
        "T-test": (-2, 2),
        "T-test P-value": (0.01, 0.01),
        "ANOVA": (0, 3),
        "ANOVA P-value": (0, 0.01),
    })

    add_scores_to_output = settings.Setting(False)
    auto_commit = settings.Setting(False)

    target_selections = settings.ContextSetting({})
    current_target_selection = settings.ContextSetting((None, None))

    def __init__(self, parent=None):
        widget.OWWidget.__init__(self, parent)

        self.min_value, self.max_value = \
            self.thresholds.get(self.Scores[self.score_index][0], (1, 0))

        #: Input data set
        self.data = None
        #: All candidate group definitions List[str | Variable, List[str]]
        self.groups = []
        #: Current target group selection
        self.targets = []
        #: The computed scores
        self.scores = None
        #: The computed scores from label permutations
        self.nulldist = None
        #: Stored selections (TODO)
        self.target_selections = None
        #: Current target group key and selected values
        self.current_target_selection = (None, None)

        self.test_f = {
            OWFeatureSelection.LowTail: test_low,
            OWFeatureSelection.HighTail: test_high,
            OWFeatureSelection.TwoTail: test_two_tail,
        }

        self.histogram = Histogram(
            enableMouse=False, enableMenu=False, background="w"
        )
        self.histogram.enableAutoRange(enable=True)
        self.histogram.getViewBox().setMouseEnabled(False, False)
        self.histogram.selectionChanged.connect(
            self.__on_histogram_plot_selection_changed
        )
        self.histogram.selectionEdited.connect(
            self._invalidate_selection
        )

        self.mainArea.layout().addWidget(self.histogram)

        box = gui.widgetBox(self.controlArea, "Info")

        self.dataInfoLabel = gui.widgetLabel(box, "No data on input.\n")
        self.dataInfoLabel.setWordWrap(True)
        self.selectedInfoLabel = gui.widgetLabel(box, "\n")

        box1 = gui.widgetBox(self.controlArea, "Scoring Method")
        gui.comboBox(box1, self, "score_index",
                     items=[sm[0] for sm in self.Scores],
                     callback=[self.on_scoring_method_changed,
                               self.update_scores])

        box = gui.widgetBox(self.controlArea, "Target Labels")
        self.label_selection_widget = LabelSelectionWidget(self)
        self.label_selection_widget.setMaximumHeight(150)
        box.layout().addWidget(self.label_selection_widget)

        self.label_selection_widget.selection_changed.connect(
            self.on_target_changed)

        self.label_selection_widget.label_activated.connect(
            self.on_label_activated)

        box = gui.widgetBox(self.controlArea, "Selection")
        box.layout().setSpacing(0)

        self.max_value_spin = gui.doubleSpin(
            box, self, "max_value", minv=-1e6, maxv=1e6, step=1e-6,
            label="Upper threshold:", callback=self.update_boundary,
            callbackOnReturn=True)

        self.low_value_spin = gui.doubleSpin(
            box, self, "min_value", minv=-1e6, maxv=1e6, step=1e-6,
            label="Lower threshold:", callback=self.update_boundary,
            callbackOnReturn=True)

        check = gui.checkBox(
            box, self, "compute_null", "Compute null distribution",
            callback=self.update_scores)

        perm_spin = gui.spin(
            box, self, "permutations_count", minv=1, maxv=50,
            label="Permutations:", callback=self.update_scores,
            callbackOnReturn=True)

        check.disables.append(perm_spin)

        box1 = gui.widgetBox(box, orientation='horizontal')

        pval_spin = gui.doubleSpin(
            box1, self, "alpha_value", minv=2e-7, maxv=1.0, step=1e-7,
            label="α-value:")
        pval_select = gui.button(
            box1, self, "Select", callback=self.select_p_best,
            autoDefault=False
        )
        check.disables.append(pval_spin)
        check.disables.append(pval_select)

        check.makeConsistent()

        box1 = gui.widgetBox(box, orientation='horizontal')
        gui.spin(box1, self, "n_best", 0, 10000, step=1,
                 label="Best Ranked:")
        gui.button(box1, self, "Select", callback=self.select_n_best,
                   autoDefault=False)

        box = gui.widgetBox(self.controlArea, "Output")

        acbox = gui.auto_commit(
            box, self, "auto_commit", "Commit", box=None)
        acbox.button.setDefault(True)

        gui.checkBox(box, self, "add_scores_to_output",
                     "Add gene scores to output",
                     callback=self._invalidate_selection)

        gui.rubber(self.controlArea)

        self.on_scoring_method_changed()

        self.resize(800, 600)

    def sizeHint(self):
        return QtCore.QSize(800, 600)

    def clear(self):
        """Clear the widget state.
        """
        self.data = None
        self.attribute_targets = []
        self.class_targets = []
        self.labels = []
        self.targets = []
        self.nulldist = None
        self.scores = None
        self.dataInfoLabel.setText("No data on input.\n")
        self.selectedInfoLabel.setText("\n")
        self.label_selection_widget.clear()
        self.clear_plot()

    def clear_plot(self):
        """Clear the histogram plot.
        """
        self.histogram.clear()

    def initialize(self, data):
        """Initialize widget state from the data."""
        col_targets, row_targets = group_candidates(data)

        self.attribute_targets = col_targets
        self.class_targets = row_targets
        self.labels = col_targets + row_targets
        self.update_targets_widget()

    def update_targets_widget(self):
        """Update the contents of the targets widget.
        """
        labels = [
            (label.name if isinstance(label, Orange.data.Variable) else label,
             values)
            for label, values in self.labels
        ]
        self.label_selection_widget.clear()
        self.label_selection_widget.set_labels(labels)

        combobox = self.label_selection_widget.labels_combo
        for i, (key, _) in enumerate(self.labels):
            if isinstance(key, Orange.data.Variable):
                combobox.setItemIcon(i, gui.attributeIconDict[key])

        self.data_labels = labels

    def set_data(self, data):
        self.closeContext()

        self.clear()
        self.error([0, 1])
        self.data = data

        if self.data is not None:
            self.initialize(data)

        if self.data is not None and \
                not (self.attribute_targets or self.class_targets):
            # If both attr. labels and classes are missing, show an error
            self.error(
                1, "Cannot compute gene scores! Differential expression "
                   "widget requires a data-set with a discrete class "
                   "variable or attribute labels!"
            )
            self.data = None

        if self.data is not None:
            # Initialize the selected groups/labels.
            # Default selected group key
            rowshint = data_hints.get_hint(data, "genesinrows", False)
            if (rowshint and self.class_targets) or not self.attribute_targets:
                # Select the first group variable candidate
                index = len(self.attribute_targets)
            elif self.attribute_targets:
                # Select the first attribute label
                index = 0
            else:
                assert False
            # Default target sets for all group keys
            # (the first value is selected)
            self.target_selections = \
                [values[:1] for _, values in self.data_labels]

            label, values = self.data_labels[index]
            # Default current selection
            self.current_target_selection = label, values[:1]

            # Restore target label selection from context settings
            items = {(key, val)
                     for key, values in self.data_labels for val in values}
            self.openContext(items)
            self.label_selection_widget.set_selection(
                *self.current_target_selection)

        self.commit()

    def set_targets(self, targets):
        """Set the target groups for score computation.
        """
        self.targets = targets
        self.update_scores()

    def update_scores(self):
        """Compute the scores and update the histogram.
        """
        self.clear_plot()
        self.error(0)
        label, values = self.current_target_selection

        if not self.data or label is None:
            return

        _, side, test_type, score_func = self.Scores[self.score_index]

        def compute_scores(X, group_indices):
            arrays = [X[ind] for ind in group_indices]
            return score_func(*arrays, axis=0)

        def permute_indices(group_indices, random_state=None):
            assert all(ind.dtype.kind == "i" for ind in group_indices)
            if random_state is None:
                random_state = np.random
            joined = np.hstack(group_indices)
            random_state.shuffle(joined)
            split_ind = np.cumsum([len(ind) for ind in group_indices])
            return np.split(joined, split_ind[:-1])

        def selected_split():
            index = self.label_selection_widget.current_label()
            selection = self.label_selection_widget.selection_indexes()
            assert index >= 0
            if index < len(self.attribute_targets):
                key, values = self.attribute_targets[index]
            else:
                key, values = self.class_targets[index]

            return key, values, selection

        def group_indices(data, key, values, axis=0):
            if axis == 0:
                return group_indices_rows(data, key, values)
            else:
                assert axis == 1
                return group_indices_columns(data, key, values)

        def group_indices_rows(data, var, values):
            col_view, _ = data.get_column_view(var)
            target_ind = [var.values.index(t) for t in values]

            mask = np.zeros_like(col_view, dtype=bool)
            for i in target_ind:
                mask |= col_view == i

            return mask

        def group_indices_columns(data, key, values):
            target = set([(key, value) for value in values])
            mask = [not target.isdisjoint(var.attributes.items())
                    for var in data.domain.attributes]
            return np.array(mask, dtype=bool)

        split_key, split_values, split_selection = selected_split()
        if isinstance(split_key, Orange.data.Variable):
            axis = 0
        else:
            assert isinstance(split_key, str)
            axis = 1

        if test_type == OWFeatureSelection.TwoSampleTest:
            target = [split_values[i] for i in split_selection]
            G1 = group_indices(self.data, split_key, target, axis=axis)
            G2 = ~G1
            indices = [np.flatnonzero(G1), np.flatnonzero(G2)]
        elif test_type == self.VarSampleTest:
            indices = [group_indices(self.data, split_key, [value], axis=axis)
                       for value in split_values]
            indices = [np.flatnonzero(ind) for ind in indices]
        else:
            assert False

        if not all(np.count_nonzero(ind) > 0 for ind in indices):
            self.error(0, "Target labels most exclude/include at least one "
                          "value.")
            self.scores = None
            self.nulldist = None
            self.update_data_info_label()
            return

        X = self.data.X
        if axis == 1:
            X = X.T

        # TODO: Check that each label has more than one measurement,
        # raise warning otherwise.
        scores = compute_scores(X, indices, )

        null_scores = []
        if self.compute_null:
            rstate = np.random.RandomState(0)
            for i in range(self.permutations_count):
                p_indices = permute_indices(indices, rstate)
                assert all(pi.shape == i.shape
                           for pi, i in zip(indices, p_indices))
                pscore = compute_scores(X, p_indices)
                assert pscore.shape == scores.shape
                null_scores.append(pscore)

        self.scores = scores
        self.nulldist = null_scores

        if null_scores:
            nulldist = np.array(null_scores, dtype=float)
        else:
            nulldist = None

        self.setup_plot(self.score_index, scores, nulldist)
        self.update_data_info_label()
        self.update_selected_info_label()

    def setup_plot(self, scoreindex, scores, nulldist=None):
        """
        Setup the score histogram plot

        Parameters
        ----------
        scoreindex : int
            Score index (into OWFeatureSelection.Scores)
        scores : (N, ) array
            The scores obtained
        nulldist (P, N) array optional
            The scores obtained under P permutations of labels.
        """
        score_name, side, test_type, _ = self.Scores[scoreindex]
        low, high = self.thresholds.get(score_name, (-np.inf, np.inf))

        validmask = np.isfinite(scores)
        validscores = scores[validmask]

        nbins = max(np.sqrt(len(validscores)), 20)
        freq, edges = np.histogram(validscores, bins=nbins)
        self.histogram.setHistogramCurve(
            pg.PlotCurveItem(x=edges, y=freq, stepMode=True,
                             pen=pg.mkPen("b", width=2))
        )

        if nulldist is not None:
            nulldist = nulldist.ravel()
            validmask = np.isfinite(nulldist)
            validnulldist = nulldist[validmask]
            nullbins = edges  # XXX: extend to the full range of nulldist
            nullfreq, _ = np.histogram(validnulldist, bins=nullbins)
            nullfreq = nullfreq * (freq.sum() / nullfreq.sum())
            nullitem = pg.PlotCurveItem(
                x=nullbins, y=nullfreq, stepMode=True,
                pen=pg.mkPen((50, 50, 50, 100))
            )
            # Ensure it stacks behind the main curve
            nullitem.setZValue(nullitem.zValue() - 10)
            self.histogram.addItem(nullitem)

        # Restore saved thresholds
        eps = np.finfo(float).eps
        minx, maxx = edges[0] - eps, edges[-1] + eps

        low, high = max(low, minx), min(high, maxx)

        if side == OWFeatureSelection.LowTail:
            mode = Histogram.Low
        elif side == OWFeatureSelection.HighTail:
            mode = Histogram.High
        elif side == OWFeatureSelection.TwoTail:
            mode = Histogram.TwoSided
        else:
            assert False
        self.histogram.setSelectionMode(mode)
        self.histogram.setBoundary(low, high)

        # If this is a two sample test add markers to the left and right
        # plot indicating which group is over-expressed in that part
        if test_type == OWFeatureSelection.TwoSampleTest:
            maxy = np.max(freq)
            # XXX: Change use of integer constant
            if scoreindex == 0:  # fold change is centered on 1.0
                x1, y1 = (minx + 1) / 2, maxy
                x2, y2 = (maxx + 1) / 2, maxy
            else:
                x1, y1 = minx / 2, maxy
                x2, y2 = maxx / 2, maxy

            _, selected = self.current_target_selection
            labelidx = self.label_selection_widget.current_label()

            _, values = self.labels[labelidx]

            left = ", ".join(v for v in values if v not in selected)
            right = ", ".join(v for v in selected)

            labelitem = pg.TextItem(left, color=(40, 40, 40))
            labelitem.setPos(x1, y1)
            self.histogram.addItem(labelitem)

            labelitem = pg.TextItem(right, color=(40, 40, 40))
            labelitem.setPos(x2, y2)
            self.histogram.addItem(labelitem)

    def update_data_info_label(self):
        if self.data is not None:
            samples, genes = len(self.data), len(self.data.domain.attributes)
            label, _ = self.labels[self.label_selection_widget.current_label()]
            if not isinstance(label, Orange.data.Variable):
                samples, genes = genes, samples

            label, target_labels = self.targets
            text = "%i samples, %i genes\n" % (samples, genes)
            text += "Sample target: '%s'" % (",".join(target_labels))
        else:
            text = "No data on input.\n"

        self.dataInfoLabel.setText(text)

    def update_selected_info_label(self):
        pl = lambda c: "" if c == 1 else "s"
        if self.data is not None and self.scores is not None:
            scores = self.scores
            low, high = self.min_value, self.max_value
            _, side, _, _ = self.Scores[self.score_index]
            test = self.test_f[side]
            count_undef = np.count_nonzero(np.isnan(scores))
            count_scores = len(scores)
            scores = scores[np.isfinite(scores)]

            nselected = np.count_nonzero(test(scores, low, high))
            defined_txt = ("{} of {} score{} undefined."
                           .format(count_undef, count_scores, pl(count_scores)))

        elif self.data is not None:
            nselected = 0
            defined_txt = "No defined scores"
        else:
            nselected = 0
            defined_txt = ""

        self.selectedInfoLabel.setText(
            defined_txt + "\n" +
            "{} selected gene{}".format(nselected, pl(nselected))
        )

    def __on_histogram_plot_selection_changed(self):
        low, high = self.histogram.boundary()
        scorename, side, _, _ = self.Scores[self.score_index]
        self.thresholds[scorename] = (low, high)
        self.min_value = low
        self.max_value = high
        self.update_selected_info_label()

    def update_boundary(self):
        # The cutoff boundary value has been changed by the user
        # (in the controlArea widgets). Update the histogram plot
        # accordingly.
        if self.data is None:
            return

        _, side, _, _ = self.Scores[self.score_index]
        if side == OWFeatureSelection.LowTail:
            self.histogram.setLower(self.min_value)
        elif side == OWFeatureSelection.HighTail:
            self.histogram.setUpper(self.max_value)
        elif side == OWFeatureSelection.TwoTail:
            self.histogram.setBoundary(self.min_value, self.max_value)

        self._invalidate_selection()

    def select_n_best(self):
        """
        Select the `self.n_best` scored genes.
        """
        if self.scores is None:
            return

        score_name, side, _, _ = self.Scores[self.score_index]
        scores = self.scores
        scores = np.sort(scores[np.isfinite(scores)])

        if side == OWFeatureSelection.HighTail:
            cut = scores[-np.clip(self.n_best, 1, len(scores))]
            self.histogram.setUpper(cut)
        elif side == OWFeatureSelection.LowTail:
            cut = scores[np.clip(self.n_best, 0, len(scores) - 1)]
            self.histogram.setLower(cut)
        elif side == OWFeatureSelection.TwoTail:
            n = min(self.n_best, len(scores))
            scores_high = scores[-n:]
            scores_low = scores[:n]
            scores = np.r_[scores_high, scores_low]
            sign = np.r_[np.full_like(scores_high, 1),
                         np.full_like(scores_low, -1)]
            scores = np.abs(scores)

            if score_name == "Fold Change":
                # comparing fold change on a logarithmic scale
                scores = np.log(scores)
            sort_ind = np.argsort(scores)
            sign = sign[sort_ind][-n:]
            count_high = np.count_nonzero(sign == 1)
            count_low = len(sign) - count_high
            cuthigh = scores_high[-max(count_high, 1)]
            cutlow = scores_low[min(count_low, len(scores_low) - 1)]
            self.histogram.setBoundary(cutlow, cuthigh)

    def select_p_best(self):
        if not self.nulldist:
            return

        _, side, _, _ = self.Scores[self.score_index]
        nulldist = np.asarray(self.nulldist).ravel()
        nulldist = nulldist[np.isfinite(nulldist)]
        nulldist = np.sort(nulldist)

        assert 0 <= self.alpha_value <= 1
        p = self.alpha_value
        if side == OWFeatureSelection.HighTail:
            cut = np.percentile(nulldist, [100 * (1 - p)])
            self.max_value = cut
            self.histogram.setUpper(cut)
        elif side == OWFeatureSelection.LowTail:
            cut = np.percentile(nulldist, [100 * p])
            self.min_value = cut
            self.histogram.setLower(cut)
        elif side == OWFeatureSelection.TwoTail:
            p1, p2 = np.percentile(nulldist, [100 * p / 2, 100 * (1 - p / 2)])
            self.histogram.setBoundary(p1, p2)

    def _invalidate_selection(self):
        self.commit()

    def on_target_changed(self):
        label, values = self.label_selection_widget.current_selection()

        if values is None:
            values = []

#         labelidx = self.label_selection_widget.current_label()
#         if labelidx >= 0:
#             label, _ = self.labels[labelidx]

        self.current_target_selection = label, values
        # Save target label selection
        labels = [l for l, _ in self.data_labels]
        if label in labels:
            label_index = labels.index(label)
            self.target_selections[label_index] = values

        self.set_targets((label, values))

    def on_label_activated(self, index):
        selection = self.target_selections[index]
        if not selection:
            selection = self.data_labels[index][1][:1]
        self.label_selection_widget.set_selection(index, selection)

    def on_scoring_method_changed(self):
        _, _, test_type, _ = self.Scores[self.score_index]
        self.label_selection_widget.values_view.setEnabled(
            test_type == OWFeatureSelection.TwoSampleTest
        )
        self.__update_threshold_spinbox()

    def __update_threshold_spinbox(self):
        _, side, _, _ = self.Scores[self.score_index]
        self.low_value_spin.setVisible(side & OWFeatureSelection.LowTail)
        self.max_value_spin.setVisible(side & OWFeatureSelection.HighTail)

    def commit(self):
        """
        Commit (send) the outputs.
        """
        if self.data is None or self.scores is None:
            return

        key, _ = self.labels[self.label_selection_widget.current_label()]
        if isinstance(key, Orange.data.Variable):
            axis = 1
        else:
            axis = 0

        score_name, side, _, _ = self.Scores[self.score_index]
        low, high = self.histogram.boundary()

        scores = self.scores
        mask = np.isfinite(scores)
        test = self.test_f[side]
        selected_masked = test(scores[mask], low, high)
        selected = np.zeros_like(scores, dtype=bool)
        selected[mask] = selected_masked

        indices = np.flatnonzero(selected)
        remaining = np.flatnonzero(~selected)

        domain = self.data.domain

        if axis == 0:
            # Select rows
            score_var = Orange.data.ContinuousVariable(score_name)
            domain = Orange.data.Domain(domain.attributes, domain.class_vars,
                                        domain.metas + (score_var,))
            data = self.data.from_table(domain, self.data)
            data[:, score_var] = np.c_[scores]
            subsetdata = data[indices]
            remainingdata = data[remaining]
        else:
            # select columns
            attrs = [copy_variable(var) for var in domain.attributes]
            for var, score in zip(attrs, scores):
                var.attributes[score_name] = str(score)

            selected_attrs = [attrs[i] for i in selected]
            remaining_attrs = [attrs[i] for i in remaining]

            domain = Orange.data.Domain(
                selected_attrs, domain.class_vars, domain.metas)
            subsetdata = self.data.from_table(domain, self.data)

            domain = Orange.data.Domain(
                remaining_attrs, domain.class_vars, domain.metas)
            remainingdata = self.data.from_table(domain, self.data)

        self.send("Data subset", subsetdata)
        self.send("Remaining data subset", remainingdata)
        self.send("Selected genes", None)

import copy
from Orange.preprocess import transformation


def copy_variable(var):
    clone = copy.copy(var)
    clone.compute_value = transformation.Identity(var)
    clone.attributes = dict(var.attributes)
    return clone


def group_candidates(data):
    items = [attr.attributes.items() for attr in data.domain.attributes]
    items = list(itertools.chain(*items))

    targets = defaultdict(set)
    for label, value in items:
        targets[label].add(value)

    # Need at least 2 distinct values or key
    targets = [(key, sorted(vals)) for key, vals in targets.items() \
               if len(vals) >= 2]
    column_groups = sorted(targets)

    disc_vars = [var for var in data.domain.class_vars + data.domain.metas
                 if isinstance(var, Orange.data.DiscreteVariable)
                 and len(var.values) >= 2]

    row_groups = [(var, var.values) for var in disc_vars]

    return column_groups, row_groups


def test_main(argv=sys.argv):
    app = QtGui.QApplication(argv)
    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = "brown-selected"
    data = Orange.data.Table(filename)

    w = OWFeatureSelection()
    w.show()
    w.raise_()
    w.set_data(data)
    rval = app.exec_()
    w.set_data(None)
    w.saveSettings()
    return rval

if __name__ == "__main__":
    sys.exit(test_main())
