import os
from collections import defaultdict

import requests
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict

load_dotenv()


def calculate_exchange_rate(currencies: dict) -> dict:
    request_url = "https://api.currencyapi.com/v3/latest"
    headers = CaseInsensitiveDict()
    headers["apikey"] = os.getenv("API_KEY")

    rate_data = defaultdict(float)

    for curr in currencies["curr_req"]:
        request_params = {
            "base_currency": currencies["base_curr"],
            "currencies": curr
        }
        r = requests.get(request_url, params=request_params, headers=headers)
        if r.status_code == 200:
            req_rate = r.json()["data"][curr]["value"]
            rate_data[curr] = req_rate
    return rate_data


if __name__ == '__main__':
    currencies_dict = {
        "base_curr": "EUR",
        "curr_req": ["INR"]
    }
    exchange_rate = calculate_exchange_rate(currencies=currencies_dict)
    print(exchange_rate[currencies_dict["curr_req"][0]])
