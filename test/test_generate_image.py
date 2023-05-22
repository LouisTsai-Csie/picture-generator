import pytest
import io
import PIL
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from model import *

class TestDemo:
    def test_generate_image_correct(self):
        args = {
            'height': 100,
            'width': 200
        }
        response = generate_image(args['height'], args['width'])

        assert response.readable()==True

        image = Image.open(response)
        width, height = image.size

        assert args['height'] == height
        assert args['width']  == width

    def test_generate_image_invalid_argument_height(self):
        args = {
            'height': -1,
            'width': 100,
        }
        response = generate_image(args['height'], args['width'])
        assert response['error'] == 'invalid arguments'
    
    def test_generate_image_invalid_argument_width(self):
        args = {
            'height': 100,
            'width': -1
        }
        response = generate_image(args['height'], args['width'])
        assert response['error'] == 'invalid arguments'
    
    def test_generate_image_invalid_data_type_height(self):
        args = {
            'height': '100',
            'width': 100
        }
        response = generate_image(args['height'], args['width'])
        assert response['error'] == 'invalid data type'
    
    def test_generate_image_invalid_data_type_width(self):
        args = {
            'height': 100,
            'width': '200'
        }
        response = generate_image(args['height'], args['width'])
        assert response['error'] == 'invalid data type'


