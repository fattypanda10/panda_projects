###### FINAL PROJECT - CARD BANKING SYSTEM ######

import sqlite3
import random as r

### Connection with the Database
conn = sqlite3.connect("card.s3db")
curs = conn.cursor()

### Card Table Creation 
curs.execute("DROP TABLE IF EXISTS card")
make_card_table = ("""CREATE TABLE card (
id INTEGER, 
number TEXT, 
pin TEXT, 
balance INTEGER DEFAULT 0);
""")
curs.execute(make_card_table)

### Luhn Validator
def luhn_valid(card_number):
    card_no1 = card_number
    if len(card_no1) <= 1:
        return False
    for i in card_no1:
        if i.isdigit() == False:
            return False
    card_no2 = [int(card_no1[i]) for i in range(len(card_no1))]
    card_no2.reverse()
    card_no2 = [card_no2[i] * 2 if i % 2 != 0 else card_no2[i]
                for i in range(len(card_no2))]
    card_no2.reverse()
    card_no2 = [card_no2[i] - 9 if card_no2[i] > 9 else card_no2[i]
                for i in range(len(card_no2))]
    sum_digs = 0
    for i in card_no2:
        sum_digs += i
    if sum_digs % 10 == 0:
        return True
    else:
        return False
    
### Random Number Generator of Required Length
def dig_gen(length):
    digits = []
    counter = 0
    while counter < length:
        digits.append(str(r.randint(0, 9)))
        counter += 1
    return ''.join(digits)

### Card and Pin Generator
def gen_card_pin():
    init_digs = '400000'
    card_gen = dig_gen(9)
    cardy = int((init_digs) + card_gen)
    # luhn part
    card_no1 = str(cardy)
    card_no2 = [int(card_no1[i]) for i in range(len(card_no1))]
    card_no2 = [card_no2[i] * 2 if i % 2 == 0 else card_no2[i] for i in range(len(card_no2))]
    card_no2 = [card_no2[i] - 9 if card_no2[i] > 9 else card_no2[i] for i in range(len(card_no2))]
    sum_digs = 0
    for i in card_no2:
        sum_digs += i
    if sum_digs % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - (sum_digs % 10)
    cardy = int(str(cardy) + str(checksum))
    piny = dig_gen(4)
    return cardy, piny

### Account Creation
def create_acct(card_count):
    while True:
        card_no, pin_gen = gen_card_pin()
        curs.execute("SELECT 'True' FROM card WHERE number = ? OR pin = ?", (card_no, pin_gen,))
        card_pin_exist = curs.fetchall()
        if len(card_pin_exist) != 0:
            continue
        else:
            break
    bal = 0
    card_gen_values = (card_count, str(card_no), str(pin_gen), bal)
    curs.execute("INSERT INTO card VALUES (?, ?, ?, ?)", card_gen_values)
    print(f"""
Your card has been created
Your card number:
{card_no}
Your card PIN:
{pin_gen}
""")
    conn.commit()
    
### Account Balance 
def balance(card_data_ext):
    curs.execute("SELECT balance FROM card WHERE number = ? AND pin = ?", (card_data_ext[0][0], card_data_ext[0][1],))
    curr_bal = curs.fetchall()
    return curr_bal[0][0]

### Income Addition
def income_add(card_data_ext):
    curr_bal = balance(card_data_ext)
    income = int(input("Enter income:\n"))
    new_bal = curr_bal + income
    curs.execute("UPDATE card SET balance = ? WHERE number = ? AND pin = ?;", (new_bal, card_data_ext[0][0], card_data_ext[0][1]))
    print("Income was added!")
    
### Money Transfer
def transfer(card_data_ext, receiver_card, money_trans):
    curs.execute("SELECT balance FROM card WHERE number = ?", (receiver_card,))
    curr_bal = curs.fetchall()
    receiver_card_bal = curr_bal[0][0]
    new_receiver_bal = receiver_card_bal + money_trans
    curs.execute("UPDATE card SET balance = ? WHERE number = ?;", (new_receiver_bal, receiver_card,))
    sender_card_bal = balance(card_data_ext)
    new_sender_bal = sender_card_bal - money_trans
    curs.execute("UPDATE card SET balance = ? WHERE number = ? AND pin = ?;", (new_sender_bal, card_data_ext[0][0], card_data_ext[0][1]))
    print("Success!")
    
### Login into Account    
def log_in():
    log_in_card = input("Enter your card number:\n")
    log_in_pin = input("Enter your PIN:\n")
    curs.execute("SELECT number FROM card WHERE number = ?", (log_in_card,))
    card_check = curs.fetchall()
    curs.execute("SELECT pin FROM card WHERE pin = ?", (log_in_pin,))
    pin_check = curs.fetchall()
    if len(card_check) == 0 or len(pin_check) == 0:
        print("Wrong card number or PIN!")
    elif ((len(card_check) and len(pin_check)) != 0):
        print("You have successfully logged in!")
        curs.execute("SELECT number, pin FROM card WHERE number = ? AND pin = ?", (log_in_card, log_in_pin,))
        card_data_ext = curs.fetchall()
        beta = True
        while beta:
            print("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")
            option = int(input())
            if option == 1:
                current_balance = balance(card_data_ext)
                print(f"Balance: {current_balance}")
            elif option == 2:
                income_add(card_data_ext)
            elif option == 3:
                receiver_card = input("Enter card number:\n")
                
                # Luhn Check Condition
                luhn_check = luhn_valid(receiver_card)
                
                # Transfer into own Account
                curs.execute("SELECT 'True' FROM card WHERE number = ?", (receiver_card,))
                card_in_db = curs.fetchall()

                # Checking for Invalid Receiver's Card
                if receiver_card == card_data_ext[0][0]:
                    print("You can't transfer money to the same account!")
                
                elif luhn_check == False:
                    print("Probably you made mistake in the card number. Please try again!")
                
                # Non-Existent Card
                elif len(card_in_db) == 0:
                    print("Such a card does not exist.")
                
                else:
                     curr_bal = balance(card_data_ext)
                     money_trans = int(input("Enter how much money you want to transfer:\n"))
                     # Inqdequate Money in Account for Transfer
                     if money_trans > curr_bal:
                         print("Not enough money!")
                     # All good with with Receiver's Card! --> Money Transfer
                     else:
                         transfer(card_data_ext, receiver_card, money_trans)
            elif option == 4:
                curs.execute("DELETE FROM card WHERE number = ? AND pin = ?", (card_data_ext[0][0], card_data_ext[0][1]))
                print('The account has been closed!')
            elif option == 5:
                print("You have successfully logged out!")
                beta = False
            elif option == 0:
                beta = False
            conn.commit()
        return 0
    conn.commit()
  
    
### Main Program
alpha = True
card_count = 0
while alpha:
    print("""
1. Create an account
2. Log into account
0. Exit
""")
    check = int(input())
    if check == 1:
        card_count += 1
        create_acct(card_count)
    elif check == 2:
        desire = log_in()
        if desire == 0:
            alpha = False
    elif check == 0:
        alpha = False
conn.commit()
conn.close()
print("Bye!")
