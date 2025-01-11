import pickle
from flask import Flask , request, app, jsonify,url_for,render_template
import numpy as np 
import pandas as pd 
import inspect

## create the flask app 
app=Flask('full_mlproject')
#Load the model 
model=pickle.load(open('regmodel.pkl' ,'rb'))

scalar=pickle.load(open('scaler.pkl'), 'wb')
 
print(inspect.getsource(app.route))

@app.rout('/')
def home():
    return render_template('home.html')

@app.rout('/predict_api', methods=['POST'])
def predict_api():
    data=request.json('data')
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(-1,1))
    output=model.predict(new_data)
    print(output[0])
    return(output[0])
if __name__=="__main__":
    app.run(debug=True)






