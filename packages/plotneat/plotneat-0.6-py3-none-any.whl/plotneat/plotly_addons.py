"""
Functions related to figures and plots with plotly
"""
from typing import Dict, Optional, Union

import numpy as np
import plotly.express.colors as pxc
from plotly.colors import n_colors
from plotly.graph_objects import Figure


def group_legend_by_name(fig: Figure, colors: Union[Dict, str, None] = None) -> None:
    """
    Groups all legends of a figure by their names
    Note: this also works with subplots.

    :param fig:
    :param colors:
    :return: /
    """

    group_names = dict()

    for sp_i in fig["data"]:
        sp_i_name = sp_i["name"]
        if sp_i_name is None:
            sp_i_name = "_"

        if sp_i_name in group_names.keys():
            sp_i["legendgroup"] = group_names[sp_i_name]

        else:
            if sp_i.legendgroup is None:
                group_names[sp_i_name] = "plot_key_" + sp_i_name
            else:
                group_names[sp_i_name] = sp_i["legendgroup"]

            sp_i["legendgroup"] = group_names[sp_i_name]

    if colors is not None:
        __update_legend_colors(fig, colors)


def prepare_minimalistic_show(fig: Figure) -> Dict:
    """
    Makes a minimalistic display of a figure, by removing the following:
        - Background (white)
        - Grid lines
        - Tips
        - Display mode bar
        - Harmonizing legends (according to name)

    Inputs
    ----------
    fig : (Figure)
        Figure identifier

    Inputs
    ----------
    kwargs : dict(config)
        Configuration to use in the minimalistic display

    """
    __remove_all_grids(fig, background="#FFF")

    clean_legend(fig, colors="safe")

    return dict(config={"displayModeBar": False, "showTips": False})


def clean_legend(fig: Figure, colors: Optional[Dict] = None) -> None:
    a = """
    Removes duplicate "name" in the legend of a figure (including subplots).

    Parameters
    ----------
    fig : (Figure)
        Figure identifier
    colors: dict or None
        Mapping of signal names to colors
        Default: None
    """

    # Join corresponding legends in groups
    group_legend_by_name(fig, colors)

    # Remove duplicates
    __remove_duplicate_legends(fig)


def __make_color_scale(n: int, scale: str = "green-red"):

    if scale == "green-red":
        colors = n_colors("rgb(5, 200, 200)", "rgb(200, 10, 10)", n, colortype="rgb")
    else:
        raise ValueError(f"Unknown color scale: {scale}")

    return colors


def __make_color_map(names, colormap, cycle_colormap=True):

    n_names = len(names)
    lower_cm = colormap.lower()

    if lower_cm == "plotly":
        colormap2use = pxc.qualitative.Plotly
    elif lower_cm == "d3":
        colormap2use = pxc.qualitative.D3
    elif lower_cm == "safe":
        colormap2use = pxc.qualitative.Safe
    elif lower_cm == "plasma_r":
        colormap2use = pxc.sequential.Plasma_r
    elif lower_cm == "green-red":
        colormap2use = __make_color_scale(n=n_names, scale="green-red")
    else:
        raise ValueError("Unknown color map: " + colormap)

    n_colors = len(colormap2use)

    if cycle_colormap is False and n_names > n_colors:
        raise ValueError(
            f"The chosen colormap ({colormap}) is too short for your legend"
        )

    colors = dict()
    i = 0
    for name_i in names:
        colors[name_i] = colormap2use[np.mod(i, n_colors)]
        i = i + 1

    return colors


def __remove_duplicate_legends(fig: Figure) -> None:
    names_already_in = list()
    for sp_i in fig["data"]:
        if sp_i["name"] in names_already_in:
            sp_i["showlegend"] = False
        else:
            sp_i["showlegend"] = True
            names_already_in.append(sp_i["name"])


def __update_legend_colors(fig: Figure, colors) -> None:
    if isinstance(colors, str):
        # Identify all names
        all_names = list()
        for sp_i in fig["data"]:
            if sp_i["name"] not in all_names:
                all_names.append(sp_i["name"])

        # Create the color map
        colors = __make_color_map(all_names, colors)

    for sp_i in fig["data"]:
        sp_i_name = sp_i["name"]
        if sp_i_name in colors.keys():
            color2use = colors[sp_i_name]
            try:
                sp_i["line"]["color"] = color2use
            except:
                pass

            try:
                sp_i["marker"]["color"] = color2use
            except:
                pass


def __remove_all_grids(fig: Figure, background: str = "#FFF") -> None:

    if isinstance(fig["layout"], list):
        layouts = fig["layout"]
    else:
        layouts = [fig["layout"]]

    for lay_i in layouts:
        lay_i["plot_bgcolor"] = background

        for field_j in lay_i:
            if field_j.startswith("xaxis") or field_j.startswith("yaxis"):
                lay_i[field_j]["showgrid"] = False
                lay_i[field_j]["linecolor"] = "#BCCCDC"
