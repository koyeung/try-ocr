import pytesseract
from PIL import Image, ImageOps


def extract_text(image_path):
    CONFIG = "-l eng"

    def preprocess(image):
        # Convert to grayscale
        image = ImageOps.grayscale(image)

        # Resize the image.
        scale_factor = 2
        return image.resize(
            (image.width * scale_factor, image.height * scale_factor),
            resample=Image.LANCZOS,
        )

    image = Image.open(image_path)
    image = preprocess(image)

    return pytesseract.image_to_string(image, config=CONFIG)
