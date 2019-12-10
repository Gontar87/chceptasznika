from app import app
from flask import Flask
from flask import render_template
from flask import request
import requests
import json


 
@app.route('/') 
def index():
    return render_template('index.html') 

@app.route('/upload') 
def upload():
    return render_template('upload.html')


@app.route('/formularz', methods=["GET", "POST"])
def formularz():
    if request.method == "POST":
        r = requests.get('http://chceptasznika.herokuapp.com/spiders')
        
        data = r.json()

        return render_template('formularz.html', data = data )

    return render_template("formularz.html")

@app.route('/ptasznik/<_id>')
def ptasznik(_id):

    r = requests.get('http://chceptasznika.herokuapp.com/spider/id/<_id>')
        
    data = r.json()

    return render_template('ptasznik.html', _id = _id, data = data )


    




        
    