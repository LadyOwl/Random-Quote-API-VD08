from flask import Flask, render_template
import requests

app = Flask(__name__)

def translate_to_russian(text):

    try:
        url = "https://api.mymemory.translated.net/get"
        params = {
            'q': text,
            'langpair': 'en|ru'
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data['responseData']['translatedText']
    except Exception as e:

        return text

def get_random_quote():

    try:

        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        response.raise_for_status()
        data = response.json()[0]
        original_quote = data["q"]
        author = data["a"]


        translated_quote = translate_to_russian(original_quote)

        return {
            "original": original_quote,
            "translated": translated_quote,
            "author": author
        }
    except Exception as e:
        return {
            "original": "Не удалось загрузить цитату.",
            "translated": "Не удалось загрузить цитату.",
            "author": "Ошибка"
        }

@app.route('/')
def index():
    quote_data = get_random_quote()
    return render_template(
        'index.html',
        original=quote_data["original"],
        translated=quote_data["translated"],
        author=quote_data["author"]
    )

if __name__ == '__main__':
    app.run(debug=True)