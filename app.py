from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

svc_model = pickle.load(open('svc_model.pkl', 'rb'))
logistic_model = pickle.load(open('logistic_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        Feature1 = float(request.form['CR_PROD_CNT_IL'])
        Feature2 = float(request.form['TURNOVER_PAYM'])
        Feature3 = float(request.form['CR_PROD_CNT_CC'])
        Feature4 = float(request.form['TRANS_COUNT_SUP_PRC'])
        Feature5 = float(request.form['TURNOVER_DYNAMIC_CUR_1M'])
        Feature6 = float(request.form['TURNOVER_DYNAMIC_CUR_3M'])
        Feature7 = float(request.form['CLNT_SETUP_TENOR'])
        Feature8 = float(request.form['REST_AVG_CUR'])
        Feature9 = float(request.form['CR_PROD_CNT_TOVR'])
        Feature10 = float(request.form['REST_AVG_PAYM'])

        model_option = request.form['model_option']
        
        placeholder_features = [0] * (59 - 10)
        features = np.array([[Feature1, Feature2, Feature3, Feature4, Feature5,
                              Feature6, Feature7, Feature8, Feature9, Feature10] + placeholder_features])
        
        if model_option == 'SVC Model':
            model = svc_model
        else:
            model = logistic_model

        prediction = model.predict(features)
        prediction_text = 'The customer is likely to churn.' if prediction[0] == 1 else 'The customer is not likely to churn.'

        return render_template('result.html', prediction=prediction_text)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
