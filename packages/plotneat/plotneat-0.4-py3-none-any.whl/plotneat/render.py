from typing import Optional

import plotly.graph_objects as go
from IPython.display import Image
from plotly.graph_objects import Figure

from .plotly_addons import prepare_minimalistic_show


def render(
    fig: Figure,
    out: str = "png",
    minimalistic: bool = True,
    height: Optional[int] = None,
    width: Optional[int] = None,
) -> None:
    """
    Renders a figure in a chosen format

    :param fig: figure to render
    :param out: filename or plotly renderer ("png", "jpeg","browser", ...)
    :param minimalistic: if True, renders in a minimalistic manner
    :param height: height (in px) - None defaults to original figure size
    :param width: width (in px) - None defaults to original figure size
    :return: /
    """

    if isinstance(fig, go.Figure):
        if height is None:
            height = fig["layout"]["height"]
        if width is None:
            width = fig["layout"]["width"]

        scale = 1
        if minimalistic is True:
            kwargs_show = prepare_minimalistic_show(fig)
        else:
            kwargs_show = dict()

        if out in ["png", "jpeg", "svg", "pdf"]:
            fig.to_image(
                format=out,
                engine="kaleido",
                width=width,
                height=height,
                scale=scale,
            )

        elif out.endswith(".json"):
            fig.write_json(out)

        elif (
            out.endswith(".png")
            or out.endswith(".jpeg")
            or out.endswith(".svg")
            or out.endswith(".pdf")
        ):
            fig.write_image(
                out,
                engine="kaleido",
                width=width,
                height=height,
                scale=scale,
            )

        elif out.endswith(".html"):
            fig.write_html(out)

        elif out == "Image":
            img_bytes = fig.to_image(
                format="png",
                width=width,
                height=height,
                scale=scale,
            )
            Image(img_bytes)

        else:
            fig.show(out, **kwargs_show)

    else:
        raise Exception("Unknown figure type")
