import re
import sys

from pytess import extract


def extract_data(image_path):
    text = extract.extract_text(image_path)
    m = re.search(r"RSI \(14\) = (?P<RSI14>\d+\.\d+)", text)

    return m.groupdict()


def main():
    print("Hello from testocr!")

    # image_path = "data/d3_00002.jpg"
    # image_path = "data/d3_00027.jpg"
    # image_path = "data/d3_03692.jpg"
    image_path = sys.argv[1]

    print(f"image file: {image_path}")

    result = extract_data(image_path)
    print(result)


if __name__ == "__main__":
    main()
