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
    	req = request.form
    	nazwa = req['nazwa']
    	stopien = req['stopien']
    	klimat = req['klimat']
    	biotop = req['biotop']
    	tem_min = req['tem_min']
    	tem_max = req['tem_max']
    	lata = req['lata']
    	r = requests.get('http://chceptasznika.herokuapp.com/spiders')
    	data = r.json()
    	return render_template('formularz.html', data = data, req = req, nazwa = nazwa)
    return render_template("formularz.html")


@app.route('/ptasznik/<_id>')
def ptasznik(_id):
	adres = 'http://chceptasznika.herokuapp.com/spider/id/' + str(_id)

	r = requests.get(adres)

	data = r.json()

	return render_template('ptasznik.html', _id = _id, data = data )


    




        
    