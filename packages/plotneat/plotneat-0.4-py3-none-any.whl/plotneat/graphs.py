"""
Functions related to figures and plots.

functions:

    * duration_curve - plots a duration curve

"""
from typing import Optional, Union

import plotly.graph_objects as go
from pandas import DataFrame, Series


def duration_curve(
    df: Union[DataFrame, Series],
    ytitle: Optional[str] = None,
    xtitle: Optional[str] = None,
) -> go.Figure:
    """
    Plots a duration curve of the data in each of the columns of a dataframe

    :param df: dataset
    :param ytitle: name of the y axis (None to ignore)
    :param xtitle: name of the x axis (None to ignore)
    :return: figure
    """

    fig = go.Figure()

    if isinstance(df, Series):
        y_i = df.sort_values(axis=0, ascending=False, na_position="last")
        fig.add_trace(go.Scattergl(y=y_i, mode="lines"))
    else:
        for col_i in df:
            y_i = df[col_i].sort_values(axis=0, ascending=False, na_position="last")
            fig.add_trace(go.Scattergl(y=y_i, name=col_i, mode="lines"))

    if xtitle is not None:
        fig["layout"]["xaxis"]["title"] = xtitle
    if ytitle is not None:
        fig["layout"]["yaxis"]["title"] = ytitle

    return fig
