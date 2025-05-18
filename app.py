import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import os

app=Flask(__name__)
model=pickle.load(open('housePred.pkl','rb'))
scaler=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    result=model.predict(new_data)
    print(result[0])
    return jsonify(result[0])

@app.route('/predict',methods=['POST'])
def predict(): 
    data=[]
    for x in request.form.values():
        data.append(float(x))
    final_input=scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    result=model.predict(final_input)
    print(result[0])
    return render_template('home.html',output=result[0])




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    

