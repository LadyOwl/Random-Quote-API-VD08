# app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

# Функция для получения цитаты из ZenQuotes
def get_random_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        data = response.json()[0]  # ZenQuotes возвращает список из одного элемента
        return {
            "quote": data["q"],
            "author": data["a"]
        }
    except Exception as e:
        return {
            "quote": "Не удалось загрузить цитату. Попробуйте позже.",
            "author": "Ошибка"
        }

@app.route('/')
def index():
    quote_data = get_random_quote()
    return render_template('index.html', quote=quote_data["quote"], author=quote_data["author"])

if __name__ == '__main__':
    app.run(debug=True)