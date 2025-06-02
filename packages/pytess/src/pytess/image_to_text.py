import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


def adaptive_threshold(image, scale):
    # Convert the image to grayscale.
    gray_image = ImageOps.grayscale(image)

    # Resize the image to enhance details.
    scale_factor = scale
    resized_image = gray_image.resize(
        (gray_image.width * scale_factor, gray_image.height * scale_factor),
        resample=Image.LANCZOS,
    )

    # Apply edge detection filter (find edges).
    return resized_image.filter(ImageFilter.FIND_EDGES)


def preprocess(image, scale, enhance):
    image = image.convert("RGB")

    image = ImageOps.autocontrast(image, cutoff=0.9)

    if enhance != 1.0:
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(enhance)

    # brightness_factor = 1.5  # Increase brightness by 50%
    # enhancer = ImageEnhance.Brightness(image)
    # image = enhancer.enhance(brightness_factor)


    # Convert to grayscale
    image = ImageOps.grayscale(image)

    # Resize the image.
    scale_factor = scale
    return image.resize(
        (image.width * scale_factor, image.height * scale_factor),
        resample=Image.LANCZOS,
    )


def extract_text(image, psm=3, scale=1, enhance=1.0):
    config = f"--psm {psm} -l eng"

    image = preprocess(image, scale=scale, enhance=enhance)
    # image = adaptive_threshold(image, scale=1)

    return pytesseract.image_to_string(image, config=config)
