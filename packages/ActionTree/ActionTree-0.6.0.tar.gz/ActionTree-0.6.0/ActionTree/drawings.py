# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import datetime
import os.path

import graphviz
import matplotlib.backends.backend_agg
import matplotlib.dates
import matplotlib.figure as mpl

from . import Action


# @todo Capture last execution in an immutable copy of the action.
# Currently "a.execute(); r = make_report(a); a.execute()" will modify (and invalidate if timing changes a lot) the report.
# Same for Graph? Yes if we implement the Graph class as suggested in following todo.
# Adding a new dependency would be reflected in the graph after its creation.


def nearest(v, values):
    for i, value in enumerate(values):
        if v < value:
            break
    if i == 0:
        return values[0]
    else:
        assert values[i - 1] <= v < values[i], (i, values[i - 1], v, values[i])
        if v - values[i - 1] <= values[i] - v:
            return values[i - 1]
        else:
            return values[i]

intervals = [
    1, 2, 5, 10, 15, 30, 60,
    2 * 60, 10 * 60, 30 * 60, 3600,
    2 * 3600, 3 * 3600, 6 * 3600, 12 * 3600, 24 * 3600,
]


class ExecutionReport(object):
    """
    Report about the execution of the action, containing successes and failures as well as timing information.
    """
    def __init__(self, action):
        self.root_action = action
        self.actions = self.__sort_actions(action)
        self.begin_time = min(a.begin_time for a in self.actions)
        self.end_time = max(a.end_time for a in self.actions)
        self.duration = self.end_time - self.begin_time

    def __sort_actions(self, root):
        actions = []
        dependents = {}
        def walk(action):
            if action not in actions:
                actions.append(action)
                for d in action.dependencies:
                    dependents.setdefault(id(d), set()).add(id(action))
                    walk(d)
        walk(root)

        ordinates = {}
        def compute(action, ordinate):
            ordinates[id(action)] = ordinate
            for d in sorted(action.dependencies, key=lambda d: d.end_time):
                if len(dependents[id(d)]) == 1:
                    ordinate = compute(d, ordinate - 1)
                else:
                    dependents[id(d)].remove(id(action))
            return ordinate
        last_ordinate = compute(root, len(actions) - 1)

        assert last_ordinate == 0
        assert sorted(ordinates.values()) == range(len(actions))

        return sorted(actions, key=lambda a: ordinates[id(a)])
        # @todo Maybe count intersections and do a local search (two-three steps) to find if we can remove some of them.

    def write_to_png(self, filename):
        """
        Write the report as a PNG image to the specified file.

        See also :meth:`get_mpl_figure` and :meth:`plot_on_mpl_axes` if you want to draw the report somewhere else.
        """
        figure = self.get_mpl_figure()
        canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(figure)
        canvas.print_figure(filename)

    def get_mpl_figure(self):  # pragma no cover (Untestable? But small.)
        """
        Return a :class:`matplotlib.figure.Figure` of this report.

        See also :meth:`plot_on_mpl_axes` if you want to draw the report on your own matplotlib figure.

        See also :meth:`write_to_png` for the simplest use-case.
        """
        fig = mpl.Figure()
        ax = fig.add_subplot(1, 1, 1)

        self.plot_on_mpl_axes(ax)

        return fig

    def plot_on_mpl_axes(self, ax):
        """
        Plot this report on the provided :class:`matplotlib.axes.Axes`.

        See also :meth:`write_to_png` and :meth:`get_mpl_figure` for the simpler use-cases.
        """
        ordinates = {id(a): len(self.actions) - i for i, a in enumerate(self.actions)}

        for a in self.actions:
            if a.status == Action.Successful:
                color = "blue"
            elif a.status == Action.Failed:
                color = "red"
            else:  # Canceled
                color = "gray"
            ax.plot([a.begin_time, a.end_time], [ordinates[id(a)], ordinates[id(a)]], color=color, lw=4)
            ax.annotate(str(a.label), xy=(a.begin_time, ordinates[id(a)]), xytext=(0, 3), textcoords="offset points")
            for d in a.dependencies:
                ax.plot([d.end_time, a.begin_time], [ordinates[id(d)], ordinates[id(a)]], "k:", lw=1)

        ax.get_yaxis().set_ticklabels([])
        ax.set_ylim(0.5, len(self.actions) + 1)

        min_time = self.begin_time.replace(microsecond=0)
        max_time = self.end_time.replace(microsecond=0) + datetime.timedelta(seconds=1)
        duration = int((max_time - min_time).total_seconds())

        ax.set_xlabel("Local time")
        ax.set_xlim(min_time, max_time)
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M:%S"))
        ax.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator(maxticks=4, minticks=5))

        ax2 = ax.twiny()
        ax2.set_xlabel("Relative time")
        ax2.set_xlim(min_time, max_time)
        ticks = range(0, duration, nearest(duration // 5, intervals))
        ax2.xaxis.set_ticks([self.begin_time + datetime.timedelta(seconds=s) for s in ticks])
        ax2.xaxis.set_ticklabels(ticks)


class DependencyGraph(object):
    """
    The dependencies of the action.
    """
    def __init__(self, action):
        self.__nodes = dict()
        self.__next_node = 0
        self.__graph = graphviz.Digraph("action", node_attr={"shape": "box"})
        self.__create_node(action)

    def __create_node(self, a):
        if id(a) not in self.__nodes:
            node = str(self.__next_node)
            label = str(a.label)
            self.__graph.node(node, label)
            self.__next_node += 1
            for d in a.dependencies:
                self.__graph.edge(node, self.__create_node(d))
            self.__nodes[id(a)] = node
        return self.__nodes[id(a)]

    def write_to_png(self, filename):
        """
        Write the graph as a PNG image to the specified file.

        See also :meth:`get_graphviz_graph` if you want to draw the graph somewhere else.
        """
        self.__graph.format = "png"
        directory = os.path.dirname(filename)
        filename = os.path.basename(filename)
        filename, ext = os.path.splitext(filename)
        self.__graph.render(directory=directory, filename=filename)

    def get_graphviz_graph(self):
        """
        Return a :class:`graphviz.Digraph` of this dependency graph.

        See also :meth:`write_to_png` for the simplest use-case.
        """
        return self.__graph
