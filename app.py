import pickle
from flask import Flask , request, app, jsonify,url_for,render_template
import numpy as np 
import pandas as pd 
import inspect
import pickle 


## create the flask app 
app=Flask('full_mlproject')
#Load the model 
model=pickle.load(open('regmodel.pkl' ,'rb'))

scalar=pickle.load(open('scalar.pkl', 'rb'))

 
print(inspect.getsource(app.route))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    if not data: 
        return jsonify({"error": "No data field in the json request Json"}), 400
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    input_data = np.array(list(data.values())).reshape(1, -1)

        # Transform the input using the scaler
    new_data = scalar.transform(input_data)
    print("the bew data is ",new_data)

    output=model.predict(new_data)
    print("the predicted output is :" ,output[0])
    return jsonify(output[0])





@app.route('/predict', methods=['POST'])

def predict():
    data=[ float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("home.html", prediction_text="house predictions is {}".format(output))


if __name__=="__main__":
    app.run(debug=True)






