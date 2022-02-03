# Second - gets all the rates once and then references it for further queries
import requests as req
import json

have_curr = input().lower()
r_have_curr = req.get(f"http://www.floatrates.com/daily/{have_curr}.json")
data_have_curr = json.loads(r_have_curr.text)
currs = [i for i in data_have_curr.keys()]
rates = [data_have_curr[i]['rate'] for i in currs]
curr_rates = {currs[i]: rates[i] for i in range(len(currs))}
cache = {}
default_currs = ['usd', 'eur']
for i in default_currs:
    if i in curr_rates:
        cache[i] = curr_rates[i]
while True:
    want_curr = input().lower()
    if want_curr == '':
        break
    else:
        amount = float(input())
        print("Checking the cache...")
        if want_curr not in cache:
            print("Sorry, but it is not in the cache!")
            got_money = round((amount * curr_rates[want_curr]), 2)
            cache[want_curr] = curr_rates[want_curr]
            print(f"You received {got_money} {want_curr.upper()}.")
        elif want_curr in cache:
            print("Oh! It is in the cache!")
            amount_rec = round((amount * curr_rates[want_curr]), 2)
            print(f"You received {amount_rec} {want_curr.upper()}.")
