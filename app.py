# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:16:59 2020

@author: UDIT DEO
"""

from flask import Flask, request, render_template
import pickle


app = Flask(__name__, template_folder='templates')


model = pickle.load(open('Licence_Model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/detect', methods=['POST'])
def detect():
    if request.method == 'POST':
        f = request.files['file']
        number = model(f.filename)
        return render_template("detect.html", name='Licence Plate Number is {}'.format(number))
   
    
if __name__ == "__main__":
    app.run(debug=False)

