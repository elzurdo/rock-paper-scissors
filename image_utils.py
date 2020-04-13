from PIL import Image, ImageOps
from io import BytesIO
import base64


def base64_to_PIL_image(base64_img):
    return Image.open(BytesIO(base64.b64decode(base64_img)))

#reference: https://stackoverflow.com/questions/31826335/how-to-convert-pil-image-image-object-to-base64-string
def PIL_image_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue())

# convert: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
def save_image(image_string, filename='snapshot.jpg'):
    # image is orgiinally RGBA
    image = base64_to_PIL_image(image_string)
    #image = image.convert('L')   # this means black and white
    image = image.convert('RGB')
    image.save(filename)

    return PIL_image_to_base64(image)

