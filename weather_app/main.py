from flask import Flask
from flask import render_template
from config import OpenWeatherAPIKey
import requests

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def hello_world():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={54.607868}&lon={-5.926437}&appid={OpenWeatherAPIKey}")
    print (response.content)
    return render_template("weather.html")
@app.route("/todd")
def todd_page():
    return "<p>Todd is god</p>"

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
    