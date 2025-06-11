from PIL import Image
from io import BytesIO

def crop_logo(img_data):
    img = Image.open(BytesIO(img_data))
    width, height = img.size
    cropped = img.crop((0, 40, width, height))
    output = BytesIO()
    output.name = 'photo.jpg'
    cropped.save(output, format='JPEG')
    output.seek(0)
    return output