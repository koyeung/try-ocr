import logging
import sys

from pytess import extract, hsi14

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)

    image_path = sys.argv[1]
    logger.info("image file: %s", image_path)

    result = extract.extract(image_path, hsi14.dict_from_text)
    assert result  # noqa: S101
    logger.info("result: %s", result)


if __name__ == "__main__":
    main()
