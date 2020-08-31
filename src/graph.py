from typing import Optional, Dict

import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.axes import Axes
from pandas import DataFrame


def set_title_axis(
        ax: Axes, title: Optional[str] = None, xlabel: Optional[str] = None,
        ylabel: Optional[str] = None
) -> Axes:
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax


def replace_df_value_by_str(df: DataFrame, value_str: Dict[str, str]) -> DataFrame:
    if not value_str:
        return df

    df_clone = df.copy()
    for key in value_str:
        df_clone = df_clone.replace(key, value_str[key])
    return df_clone


def plot_bar_graph(
        df: DataFrame, col_x: str, title: Optional[str],
        xlabel: Optional[str] = None, ylabel: Optional[str] = None,
        categories: Optional[Dict[str, str]] = None
):
    df[col_x] = replace_df_value_by_str(df[col_x], categories)
    ax = sb.countplot(data=df, x=col_x, palette=sb.color_palette('YlOrRd'))
    set_title_axis(ax, title, xlabel, ylabel)
    plt.show()


def plot_boxplot(
        df: DataFrame, col_x: str, col_y: str, title: Optional[str] = None,
        xlabel: Optional[str] = None, ylabel: Optional[str] = None,
        categories: Optional[Dict[str, str]] = None
):
    df = df.sort_values(by=[col_x])
    df[col_x] = replace_df_value_by_str(df[col_x], categories)
    df[col_y] = df[col_y].astype(float)
    ax = sb.boxplot(x=df[col_x], y=df[col_y])
    set_title_axis(ax, title, xlabel, ylabel)
    plt.show()


def plot_catplot_box(
        df: DataFrame, col_x: str, col_y: str,
        xlabel: Optional[str] = None, ylabel: Optional[str] = None,
        categories: Optional[Dict[str, str]] = None
):
    df = df.sort_values(by=col_x, ascending=True)
    df[col_y] = df[col_y].astype(float)
    df[col_x] = replace_df_value_by_str(df[col_x], categories)
    ax = sb.catplot(x=col_x, y=col_y, kind='boxen', data=df, height=8)
    ax.set_axis_labels(xlabel, ylabel)
    plt.show()


def plot_histogram(
        df: DataFrame, title: Optional[str], xlabel: Optional[str] = None,
        ylabel: Optional[str] = None
):
    ax = sb.distplot(df, kde=False)
    set_title_axis(ax, title, xlabel, ylabel)
    plt.show()


def plot_pie_graph(
        df: DataFrame, x_col: str, categories: Dict[str, str],
        title: Optional[str]
):
    count: Dict[str, int] = df[x_col].value_counts()
    values = [count[value] for value in count.index.tolist()]
    labels = [categories[value] for value in count.index.tolist()]

    total = sum(values)
    labels_perct = ['%s (%2.1f%%)' % (labels[i], values[i] / total * 100)
                    for i in range(len(labels))]
    patches, texts = plt.pie(values, startangle=30)
    plt.axis('equal')
    plt.title(title)
    plt.legend(handles=patches, labels=labels_perct, loc='best')
    plt.show()


class Graph2D():
    title: str
    x_col: str
    y_col: str
    xlabel: str
    ylabel: str
    label_categories: Dict[str, str]

    def __init__(
            self, x_col: str, y_col: Optional[str] = None,
            title: Optional[str] = None, xlabel: Optional[str] = None,
            ylabel: Optional[str] = None, label_categories: Optional[Dict[str, str]] = None
    ):
        self.x_col = x_col
        self.y_col = y_col
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.label_categories = label_categories
