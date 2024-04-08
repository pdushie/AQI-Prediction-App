from  flask import Flask, request, jsonify
from aqi_predict import predict_aqi

app = Flask(__name__)

@app.route('/')
def home():
    return(index.html)

@app.route('/tryit/<int:var>',methods=['GET'])
def tryit(var):
    return({"Result":var})

@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json
    x=data.get("x")
    y=data.get("y")
    z=data.get("z")
    w=data.get("w")
    result = predict_aqi(x,y,z,w)
    return {'Result': result}

if __name__ == '__main__':
    app.run(debug=True)
