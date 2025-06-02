import logging

from PIL import Image

from pytess import image_to_text

logger = logging.getLogger(__name__)


def extract(image_path, dict_from_text):
    image = Image.open(image_path)

    for params in [
        {"psm": 11, "scale": 2},
        {"psm": 3, "scale": 2},
        {"psm": 11, "scale": 3},
        {"psm": 11, "scale": 2, "enhance": 1.2},
        # {"psm": 11, "scale": 4},
        {"psm": 11, "scale": 5},
    ]:
        logger.info("using parameters: %s", params)
        text = image_to_text.extract_text(image, **params)
        logger.debug("text: %s", text)
        data = dict_from_text(text)
        if data:
            return data

    return {}
