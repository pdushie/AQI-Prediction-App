from  flask import Flask, request, jsonify,render_template
from aqi_predict import predict_aqi

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tryit/<int:var>',methods=['GET'])
def tryit(var):
    return({"Result":var})

@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json()
    NO2=data.get("no2_value")
    O3=data.get("o3_value")
    SO2=data.get("so2_value")
    CO=data.get("co_value")
    result = predict_aqi(NO2,O3,SO2,CO)
    return {'Result': result}

if __name__ == '__main__':
    app.run(debug=True)
