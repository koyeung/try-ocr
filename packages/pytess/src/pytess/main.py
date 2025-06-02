import re
import sys

import pytesseract
from PIL import Image, ImageOps


def extract_data(image_path):
    CONFIG = "-l eng"

    def resize_image(image):
        # Resize the image.
        scale_factor = 2
        return image.resize(
            (image.width * scale_factor, image.height * scale_factor),
            resample=Image.LANCZOS,
        )

    def gray_image(image):
        return ImageOps.grayscale(image)

    image = Image.open(image_path)
    image = gray_image(image)
    image = resize_image(image)

    extracted_text = pytesseract.image_to_string(image, config=CONFIG)

    m = re.search(r"RSI \(14\) = (?P<RSI14>\d+\.\d+)", extracted_text)

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
