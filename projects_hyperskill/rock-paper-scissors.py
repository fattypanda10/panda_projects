import random

name = input("Enter your name: ")
print(f"Hello, {name}")
filey = open('rating.txt', 'r')
data_read = filey.readlines()
data = []
for i in data_read:
    data.append(i.strip())
names = []
scores = []
for j in data:
    c, d = j.split()
    names.append(c)
    scores.append(int(d))
if name in names:
    user_score = scores[names.index(name)]
else:
    user_score = 0
default = ['rock', 'paper', 'scissors']
user_options = input()
if user_options == '':
    options = default
else:
    options = user_options.split(sep = ',')
print("Okay, let's start")
user = input()
while user != '!exit':
    if user == '!rating':
        print(f"Your rating: {user_score}")
    elif user not in options:
        print("Invalid input")
    else:
        comp = random.choice(options)   
        user_index = options.index(user)
        if user_index == 0:
            sol = options[1:]
        elif user_index == options.index(options[-1]):
            sol = options[:-1]
        else:
            sol = options[user_index + 1::]
            for i in options[:user_index]:
                sol.append(i)
        sol_win = sol[:len(sol) // 2]  #winners
        sol_loss = sol[((len(sol) // 2)):]   #losers  
        if user == comp:
            print(f"There is a draw ({comp})")
            user_score += 50
        elif comp in sol_win:
            print(f"Sorry, but computer chose {comp}")
            user_score += 0
        elif comp in sol_loss:
            print(f"Well done. Computer chose {comp} and failed")
            user_score += 100
    user = input()
print("Bye!")
