import logging
import sys

from pytess import extract, rsi

LOGGER = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)

    image_path = sys.argv[1]
    LOGGER.info("image file: %s", image_path)

    result = extract.extract(image_path, rsi.dict_from_text)
    assert result  # noqa: S101

    LOGGER.info("result: %s", result)


if __name__ == "__main__":
    main()
