import logging
import pathlib
import sys

from pytess import extract, hsi14


def main():
    logging.basicConfig(level=logging.INFO)

    image_base_dir = pathlib.Path(sys.argv[1])

    for image_path in image_base_dir.glob("d6*.jpg"):
        logging.info("image file: %s", image_path)

        result = extract.extract(image_path, hsi14.dict_from_text)
        assert result  # noqa: S101
        logging.info(result)


if __name__ == "__main__":
    main()
