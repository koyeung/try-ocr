import logging
import os
from collections.abc import Callable
from typing import NotRequired, TypedDict

from PIL import Image

from pytess import image_to_text

LOGGER = logging.getLogger(__name__)


class Params(TypedDict):
    psm: int
    scale: float
    enhance: NotRequired[float]


PARAMS: list[Params] = [
    {"psm": 11, "scale": 2},
    {"psm": 3, "scale": 2},
    {"psm": 11, "scale": 3},
    {"psm": 11, "scale": 2, "enhance": 1.2},
    {"psm": 11, "scale": 5},
]


def extract(
    image_path: os.PathLike, dict_from_text: Callable[[str], dict[str, str]]
) -> dict[str, str]:
    image = Image.open(image_path)

    for params in PARAMS:
        LOGGER.info("using parameters: %s", params)

        text = image_to_text.extract_text(image, **params)
        LOGGER.debug("text: %s", text)

        data = dict_from_text(text)
        if data:
            return data

    return {}
