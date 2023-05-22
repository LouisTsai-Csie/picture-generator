from flask import Flask, request, send_file, render_template, abort

from model import *
from utils.event import *
from utils.logging import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        width  = request.form['width']
        height = request.form['height']

        if not width or not height:
            abort(400)

        if not width.isdigit() or not height.isdigit():
            abort(400)

        image = generate_image(int(height), int(width))
        post_request_log('/api/genpic')
        send_event('APIRespond')
        return send_file(image, mimetype='image/png')
    
    get_request_log('/')
    send_event('GetIndex')
    return render_template('picture/index.html')


@app.errorhandler(400)
def handle_bad_request(error):
    return render_template('error/index.html', error='Invalid Input'), 400



if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './service_account.json'
    app.run()
    start_log()
