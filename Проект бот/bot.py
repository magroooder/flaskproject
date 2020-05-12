from flask import Flask, request
import requests

app = Flask(__name__)


def check_weather():
    params = {"access_key": "86a3fe972756lk34a6a042bll348b1e3", "query": "Moscow"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return f"Сейчас в Москве {api_response['current']['temperature']} градусов"


def message(chat_id, text):
    method = "sendMessage"
    token = "1223553361:AAFHZNrNopgYK5e1KJTWzAIq1MRbwMo8OD8"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        weather = check_weather()
        message(chat_id, weather)
    return {"ok": True}
