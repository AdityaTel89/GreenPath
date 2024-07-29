from __future__ import division, print_function

import os

import cv2
import numpy as np
import pymongo
from flask import Flask, request, render_template, jsonify, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load model
MODEL_PATH = 'model.h5'
model = load_model(MODEL_PATH)

# MongoDB setup
client = pymongo.MongoClient('localhost', 27017)
db = client.Green_Path

# Utility functions
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def equalize(img):
    return cv2.equalizeHist(img)

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

def getClassName(classNo):
    class_names = [
        'Speed Limit 20 km/h', 'Speed Limit 30 km/h', 'Speed Limit 50 km/h', 'Speed Limit 60 km/h',
        'Speed Limit 70 km/h', 'Speed Limit 80 km/h', 'End of Speed Limit 80 km/h', 'Speed Limit 100 km/h',
        'Speed Limit 120 km/h', 'No passing', 'No passing for vehicles over 3.5 metric tons',
        'Right-of-way at the next intersection', 'Priority road', 'Yield', 'Stop', 'No vehicles',
        'Vehicles over 3.5 metric tons prohibited', 'No entry', 'General caution', 'Dangerous curve to the left',
        'Dangerous curve to the right', 'Double curve', 'Bumpy road', 'Slippery road', 'Road narrows on the right',
        'Road work', 'Traffic signals', 'Pedestrians', 'Children crossing', 'Bicycles crossing',
        'Beware of ice/snow', 'Wild animals crossing', 'End of all speed and passing limits', 'Turn right ahead',
        'Turn left ahead', 'Ahead only', 'Go straight or right', 'Go straight or left', 'Keep right', 'Keep left',
        'Roundabout mandatory', 'End of no passing', 'End of no passing by vehicles over 3.5 metric tons'
    ]
    return class_names[classNo]

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(32, 32))
    img = np.asarray(img)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)
    predictions = model.predict(img)
    classIndex = np.argmax(predictions, axis=1)
    preds = getClassName(classIndex[0])
    return preds

# User class for handling signup and login
class User:
    def signup(self):
        user = {
            "name": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400
        result = db.users.insert_one(user)
        user['_id'] = str(result.inserted_id)
        return jsonify(user), 200

    def login(self):
        user = db.users.find_one({
            "email": request.form.get('email'),
            "password": request.form.get('password')
        })
        if user:
            return jsonify({"message": "Login successful"}), 200

        return jsonify({"error": "Invalid login credentials"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    user = User()
    response = user.signup()
    if response[1] == 200:
        return render_template('auth.html')
    else:
        return render_template('login.html', error=response[0].get_json().get('error'))

@app.route('/login', methods=['POST'])
def login():
    user = User()
    response = user.login()
    if response[1] == 200:
        return render_template('auth.html')
    else:
        return render_template('login.html', error=response[0].get_json().get('error'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        location = request.form.get('location')
        description = request.form.get('description')
        incident_image = request.files['incidentImage']

        if incident_image:
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(incident_image.filename))
            incident_image.save(file_path)

            incident = {
                "location": location,
                "description": description,
                "image_path": file_path
            }
            db.incidents.insert_one(incident)

            return redirect(url_for('search'))

    return render_template('search.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/')
def logedin():
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        preds = model_predict(file_path, model)
        return preds
    return None

if __name__ == '__main__':
    app.run(port=5001, debug=True)
