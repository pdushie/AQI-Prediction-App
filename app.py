from  flask import Flask, request, jsonify,render_template
from aqi_predict import predict_aqi

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tryit/<int:var>',methods=['GET'])
def tryit(var):
    return({"Result":var})

@app.route('/json_predict/', methods=['POST'])
def json_predict():
    data = request.get_json()
    NO2=data.get("no2_value")
    O3=data.get("o3_value")
    SO2=data.get("so2_value")
    CO=data.get("co_value")
    result = predict_aqi(NO2,O3,SO2,CO)
    return {'result':result}

@app.route('/predict/', methods=['POST'])
def predict():
    #data = request.get_json()
    NO2=float(request.form.get("no2_value"))
    O3=float(request.form.get("o3_value"))
    SO2=float(request.form.get("so2_value"))
    CO=float(request.form.get("co_value"))
    result = predict_aqi(NO2,O3,SO2,CO)
    return {'NO2':NO2,'O3':O3,'SO2':SO2,'CO':CO,'result':result}

if __name__ == '__main__':
    app.run(debug=True)
