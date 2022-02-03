# Gets the converted currency based on the latest exchange rate
import requests as req
import json

def curr_exchange(have_currency: str, want_currency: str, money: float) -> float:
    r_have_curr = req.get(f"http://www.floatrates.com/daily/{have_currency}.json")
    r_want_curr = req.get(f"http://www.floatrates.com/daily/{want_currency}.json")
    data_have_curr = json.loads(r_have_curr.text)
    data_want_curr = json.loads(r_want_curr.text)
    exch_rate_have_want = data_have_curr[want_currency]['rate']
    exch_rate_want_have = data_want_curr[have_currency]['rate']
    amt_rec = round((money * exch_rate_have_want), 2)
    cache[f"{have_currency.upper()}:{want_currency.upper()}"] = exch_rate_have_want
    cache[f"{want_currency.upper()}:{have_currency.upper()}"] = exch_rate_want_have
    return amt_rec


cache = {}
have_curr = input().lower()
while True:
    want_curr = input().lower()
    if want_curr == '':
        break
    else:
        amount = float(input())
        print("Checking the cache...")
        if f"{have_curr.upper()}:{want_curr.upper()}" not in cache:
            print("Sorry, but it is not in the cache!")
            got_money = curr_exchange(have_curr, want_curr, amount)
            print(f"You received {got_money} {want_curr.upper()}.")
        else:
            print("Oh! It is in the cache!")
            amount_rec = round((amount * cache[f"{have_curr.upper()}:{want_curr.upper()}"]), 2)
            print(f"You received {amount_rec} {want_curr.upper()}.")
            
            
