import logging
import pathlib
import sys

from pytess import extract, rsi

LOGGER = logging.getLogger(__name__)

IGNORE: list[str] = [
    # "m8_00700.jpg",
]


def main():
    logging.basicConfig(level=logging.INFO)

    image_base_dir = pathlib.Path(sys.argv[1])

    # filename_pat = "d3*.jpg"
    # filename_pat = "m8*.jpg"
    filename_pat = "w3*.jpg"

    LOGGER.info("filename pattern: %s", filename_pat)

    for image_path in sorted(image_base_dir.glob(filename_pat)):
        if image_path.name in IGNORE:
            LOGGER.info("bypass file: %s", image_path)
            continue

        LOGGER.info("image file: %s", image_path)

        result = extract.extract(image_path, rsi.dict_from_text)
        assert result  # noqa: S101

        LOGGER.info(result)


if __name__ == "__main__":
    main()
