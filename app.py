import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on html gui
    '''
    int_features=[int(x) for x in request.form.values()]
    print(int_features)
    final_features=[np.array(int_features)]
    print(final_features)
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    print(prediction)
    return render_template('index.html',prediction_text='Employee salary is {} dollars.'.format(output))

@app.route('/predict-api',methods=['POST'])
def predict_api():
    '''
    For direct api calls through request
    '''
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)



if __name__ == "__main__":
    app.run(debug=True,port=8000)