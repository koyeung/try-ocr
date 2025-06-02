import logging

from PIL import Image

from pytess import image_to_text


def extract(image_path, dict_from_text):
    image = Image.open(image_path)

    for params in [
        {"scale": 2},
        {"psm": 11, "scale": 2},
    ]:
        logging.info("using parameters: %s", params)
        text = image_to_text.extract_text(image, **params)
        logging.debug("text: ", text)
        data = dict_from_text(text)
        if data:
            return data

    return {}
