# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime

from flask import Flask, render_template

from flask import request

import json
import random
from sklearn.linear_model import LinearRegression
from sklearn import linear_model    # linear & logistic regression
from sklearn import preprocessing   # polynomial features for polynomial regression
from sklearn import model_selection
import numpy as np
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials

app = Flask(__name__)

@app.route('/query')
def query():
	building = request.args.get('building')
	#f = open("data.txt","r")
	#content = json.loads(f.read())
	if building=='a':
		content=random.randrange(1,200)
	else:
		content=random.randrange(150,400)
	return str(content)
	

@app.route('/store')
def store():
	f = open("data.txt", "r")
	return f.read()

@app.route('/predict')
def predict():
	value=[466,1675,3242,4514,4595,4289,3511]
	fin=[value]
	for i in range(14):
		new_val=[]
		for i in range(len(value)):
			new_val.append(random.randrange(int(value[i]*0.8),int(value[i]*1.2)))
		fin.append(new_val)
	val=[5,6,7,8,9,10,11]
	X=np.array(val*15)
	Y=np.array(fin)
	lm = linear_model.LinearRegression()
	poly = preprocessing.PolynomialFeatures(2)
	poly_X = poly.fit_transform(np.ndarray.flatten(X).reshape(-1,1))

	lm.fit(poly_X,np.ndarray.flatten(Y).reshape(-1,1)) 
	#reg=LinearRegression().fit(np.ndarray.flatten(X).reshape(-1,1),np.ndarray.flatten(Y).reshape(-1,1))
	stime = request.args.get('stime')
	etime = request.args.get('etime')
	min=5515
	val=stime
	for i in range(int(stime),int(etime)+1):
		#update=reg.predict(np.array(i).reshape(-1,1))
		update=lm.predict(poly.fit_transform(np.reshape([i], (1,-1))))
		print(update)
		if update<min:
			val=i
			min=update
	return str(val)	 
		
	
	

@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
