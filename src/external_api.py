import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def currency_conversion(currency_from, amount, api_key):
    """Функция конвертирует сумму заданной валюты в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"

    response = requests.request("GET", url, headers=headers)
    status_code = response.status_code
    if status_code != 200:
        if status_code == 429:
            print(f"Ошибка доступа к API конвертации валюты: {status_code} - превышен лимит использования API")
            return []
    result = response.json()["result"]
    return result
