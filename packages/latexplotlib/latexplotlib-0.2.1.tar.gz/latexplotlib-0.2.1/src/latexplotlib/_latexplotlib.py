import json
import os
import sys
import warnings
from pathlib import Path
from typing import Any, Callable, Tuple

import matplotlib.pyplot as plt
from appdirs import user_config_dir

GOLDEN_RATIO = (5 ** 0.5 + 1) / 2

HEIGHT = 630
WIDTH = 412

CONFIGFILE = "config.ini"

NAME = "latexplotlib"
CONFIGDIR = Path(user_config_dir(NAME))
CONFIGPATH = CONFIGDIR.joinpath(CONFIGFILE)


def export(fun: Callable):  # type: ignore
    mod = sys.modules[fun.__module__]
    if hasattr(mod, "__all__"):
        mod.__all__.append(fun.__name__)  # type: ignore
    else:
        mod.__all__ = [fun.__name__]  # type: ignore
    return fun


def _round(val: float) -> float:
    return int(10 * val) / 10


@export
def set_page_size(
    width: int,
    height: int,
):
    """Sets to size of the latex page in pts.

    You can find the size of the latex page under point 7 and 8 from

    \\usepackage{layout}
    \\layout*

    Parameters
    ----------
    width : int
        The width of the latex page in pts.
    height : int
        The height of the latex page in pts.
    """
    try:
        os.makedirs(CONFIGDIR)
    except FileExistsError:
        pass

    with open(CONFIGPATH, "w", encoding="utf-8") as cfg:
        json.dump({"width": width, "height": height}, cfg, indent=4)


@export
def get_page_size() -> Tuple[int, int]:
    """The size of the latex page in pts.

    Returns
    -------
    int, int
        (width, height) of the page in pts.
    """
    try:
        with open(CONFIGPATH, "r", encoding="utf-8") as cfg:
            config = json.load(cfg)
    except FileNotFoundError:
        warnings.warn("Page size not set, using defaults (see 'set_page_dimension').")
        return WIDTH, HEIGHT
    return (config["width"], config["height"])


@export
def reset_page_size():
    if os.path.exists(CONFIGPATH):
        os.remove(CONFIGPATH)


@export
def convert_pt_to_in(pts: int) -> float:
    """Converts a length in pts to a length in inches.

    Parameters
    ----------
    pts : int
        A length in pts.

    Returns
    -------
    float
        A length in inches.

    References
    ----------
    - https://www.overleaf.com/learn/latex/Lengths_in_LaTeX
    """
    return 12.0 * 249.0 / 250.0 / 864.0 * pts


def _set_size(nrows, ncols, fraction: float = 1.0, ratio: float = GOLDEN_RATIO):
    max_width_pt, max_height_pt = get_page_size()

    if fraction < 0:
        raise ValueError("fraction must be positive!")
    elif fraction > 1:
        width_pt = max_width_pt
    else:
        width_pt = max_width_pt * fraction

    height_pt = width_pt / ratio * (nrows / ncols)

    if height_pt > max_height_pt:
        width_pt = width_pt * max_height_pt / height_pt
        height_pt = max_height_pt

    return _round(convert_pt_to_in(width_pt)), _round(convert_pt_to_in(height_pt))


@export
def figsize(fraction: float = 1.0, ratio: float = GOLDEN_RATIO):
    return _set_size(1, 1, fraction=fraction, ratio=ratio)


@export
def subplots(
    *args, fraction: float = 1.0, ratio=GOLDEN_RATIO, **kwargs
) -> Tuple[Any, Any]:
    """A wrapper for matplotlib's 'plt.subplots' method

    This function wraps 'plt.subplots'

    Parameters
    ----------
    *args
        see help(plt.subplots)
    fraction : float, optional
        The fraction of of horizontal or vertical space to be used for the figure. For
        values larger then 1.0, the figure is to large to fit on the latex page without
        scaling it.
    ratio : float, optional
        The ratio of figure width to figure height for each individual axis element.
        Defaults to the golden ratio.
    **kwargs
        see help(plt.subplots)

    Returns
    -------
    Tuple[Figure, axes.Axes or array of Axes]
        see help(plt.subplots)

    References
    ----------
    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
    - https://jwalton.info/Embed-Publication-Matplotlib-Latex/
    """
    if "figsize" in kwargs:
        kwargs.pop("figsize")
        warnings.warn("keyword 'figsize' is ignored and its value discarded.")

    if "nrows" in kwargs:
        nrows = kwargs.pop("nrows")
        ncols = kwargs.pop("ncols")
    elif "ncols" in kwargs:
        nrows = args[0]
        ncols = kwargs.pop("ncols")
    else:
        nrows = args[0]
        ncols = args[1]

    return plt.subplots(  # type: ignore
        nrows,
        ncols,
        figsize=_set_size(nrows, ncols, fraction=fraction, ratio=ratio),
        **kwargs
    )
