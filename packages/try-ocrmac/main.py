# import re
import sys
from pprint import pprint

from ocrmac import ocrmac
# from PIL import Image, ImageOps


def extract_data(image_path):
    annotations = ocrmac.OCR(
        image_path, framework="livetext", language_preference=["en-US"]
    ).recognize()

    # m = re.search(r"RSI \(14\) = (?P<RSI14>\d+\.\d+)", extracted_text)
    # return m.groupdict()

    result = [(text, confid) for (text, confid, _) in annotations]

    return result


def main():
    # image_path = "data/d3_00002.jpg"
    # image_path = "data/d3_00027.jpg"
    # image_path = "data/d3_03692.jpg"
    image_path = sys.argv[1]

    print(f"image file: {image_path}")

    result = extract_data(image_path)
    pprint(result)


if __name__ == "__main__":
    main()
