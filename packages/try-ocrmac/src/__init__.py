import logging
import sys

from ocrmac import ocrmac

# from PIL import Image, ImageOps


def extract_data(image_path):
    annotations = ocrmac.OCR(
        image_path, framework="livetext", language_preference=["en-US"]
    ).recognize()

    # m = re.search(r"RSI \(14\) = (?P<RSI14>\d+\.\d+)", extracted_text)
    # return m.groupdict()

    return [(text, confid) for (text, confid, _) in annotations]


def main():
    logging.dictConfig(level=logging.INFO)

    image_path = sys.argv[1]

    logging.info("image file: %s", image_path)

    result = extract_data(image_path)
    logging.info(result)


if __name__ == "__main__":
    main()
