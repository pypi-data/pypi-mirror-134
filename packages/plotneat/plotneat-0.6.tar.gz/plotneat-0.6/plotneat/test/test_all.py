import os

import pandas as pd
from plotly.graph_objects import Figure

from plotneat.graphs import duration_curve
from plotneat.plotly_addons import group_legend_by_name, prepare_minimalistic_show
from plotneat.render import render

PATH_OUT = "out_test"


def test_all():
    df = pd.DataFrame(data={"x": [1, 2, 3, 4, 5, 6, 7, 8]})

    fig_1 = duration_curve(df["x"])
    assert isinstance(fig_1, Figure)

    fig_2 = duration_curve(df)
    assert isinstance(fig_2, Figure)

    group_legend_by_name(fig_2)
    prepare_minimalistic_show(fig_2)

    try:
        os.mkdir(PATH_OUT)
    except:
        pass
    assert render(fig_2, out=f"{PATH_OUT}/1.json") is None
    render(fig_2, out=f"{PATH_OUT}/1.html")
    render(fig_2, out=f"{PATH_OUT}/1.png")
    render(fig_2, out=f"{PATH_OUT}/1.png", height=600, width=800)
