from  flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return("AQI App")

if __name__ == '__main__':
    app.run()
