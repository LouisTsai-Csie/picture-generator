from PIL import Image
import io
import random

def generate_image(height, width):

    if not width or not height: return {'error': 'invalid arguments'}

    if not isinstance(height, int) or not isinstance(width, int): return {'error': 'invalid data type'}

    if width<=0 or height<=0: return {'error': 'invalid arguments'}

    image = Image.new('RGBA', (width, height), (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    image_buffer.seek(0)

    return image_buffer
