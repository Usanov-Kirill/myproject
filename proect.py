import requests

def translate(lang, text):
    text = text
    url = "https://clients5.google.com/translate_a/t"
    params = {
        "client": "dict-chrome-ex",
        "sl": "auto",
        "tl": lang,
        "q": text,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)
    return response.json()[0][0]

tr = translate("en", "привет")
print(tr)
