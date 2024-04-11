from  flask import Flask, request, jsonify,render_template
#from streamlit_app.py import predict_aqi
import pickle
import bz2file as bz2
import sklearn

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

model = decompress_pickle('aqi_dt_comp.pbz2')

def predict_aqi(no2_value, o3_value,so2_value,co_value):
    
    return (model.predict([[no2_value, o3_value, so2_value, co_value]]).item())



app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

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
