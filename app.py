import os
import requests
import shutil
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'imagenes/'
classification_path = 'imagenes/clasificacion/'
categories = ['dog', 'cat']

api_key = 'acc_28a6ff7b733c038'
api_secret = '7ffe85f367883735b3ddba0dc7615c7f'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

for category in categories:
    category_path = os.path.join(classification_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

def classify_image(image_path):
    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')}
    )
    if response.status_code == 200:
        data = response.json()
        for tag in data['result']['tags']:
            for category in categories:
                if tag['tag']['en'] == category:
                    shutil.copy(image_path, os.path.join(classification_path, category, os.path.basename(image_path)))
                    return category
    return None

@app.route('/')
def index():
    images = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            images.append(filename)
    return render_template('index.html', images=images)

@app.route('/classify')
def classify_images():
    classifications = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            category = classify_image(image_path)
            classifications.append({'filename': filename, 'category': category})
    return jsonify(classifications)

@app.route('/imagenes/<path:filename>')
def send_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)