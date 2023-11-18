from PIL import Image


def compress(image_path: str, output_path: str, quality=90):
    image = Image.open(image_path)
    image = image.convert("RGB")
    image.save(output_path, quality=quality, optimize=True)
