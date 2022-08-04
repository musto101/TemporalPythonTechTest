from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os
import numpy as np
from werkzeug.utils import secure_filename, redirect
import glob

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template('upload.html')


UPLOAD_FOLDER = 'upload_folder/'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = joblib.load(filename='model/rf_track.joblib')


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if request.method == 'POST':
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(app.config['UPLOAD_FOLDER'] + filename)
    return render_template('upload.html')


@app.route('/predict', methods=['POST'])
def predict():
    list_of_files = glob.glob('upload_folder/*.csv')
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        test_dat = pd.read_csv(latest_file).dropna()
        pred = model.predict(test_dat)
        output = pred[0]
    return render_template('upload.html', prediction_text='Project ID should be ${}'.format(pred))


# list_of_files = glob.glob('upload_folder/*.csv')
#
# if list_of_files:
#     latest_file = max(list_of_files, key=os.path.getctime)
#     test_dat = pd.read_csv(latest_file).dropna()
#
#
# @app.route('/',methods=['POST'])
# def requestResults(dat):
#     # get the tweets text
#     pred = model.predict(test_dat.iloc[:, 2:])
#     return jsonify(pred)


if __name__ == '__main__':
    app.run(debug=True)