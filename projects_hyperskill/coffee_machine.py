class CoffeeMachine():
    
    def __init__(self):
        self.coffee = {}
        self.coffee['water'] = 400
        self.coffee['milk'] = 540
        self.coffee['beans'] = 120
        self.coffee['cups'] = 9
        self.coffee['money'] = 550
    
    def program(self):
        
        ### BUY FUNCTION
        def buy():
            option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            if option == 'back':
                pass
            elif option != 'back':
                if int(option) == 1:
                    req_w_esp = 250
                    req_b_esp = 16
                    if self.coffee['water'] < req_w_esp:
                        print("Sorry, not enough water!")
                    elif self.coffee['beans'] < req_b_esp:
                        print("Sorry, not enough coffee beans!")
                    elif self.coffee['water'] >= req_w_esp and self.coffee['beans'] >= req_b_esp:
                        print("I have enough resources, making you a coffee!")
                              
                        self.coffee['water'] = self.coffee['water'] - 250
                        self.coffee['milk'] = self.coffee['milk']
                        self.coffee['beans'] = self.coffee['beans'] - 16
                        self.coffee['cups'] = self.coffee['cups'] - 1
                        self.coffee['money'] = self.coffee['money'] + 4
            
                  
                elif int(option) == 2:
                    req_w_lat = 350
                    req_m_lat = 75
                    req_b_lat = 20
                    if self.coffee['water'] < req_w_lat:
                        print("Sorry, not enough water!")
                    elif self.coffee['milk'] < req_m_lat:
                        print("Sorry, not enough milk!")
                    elif self.coffee['beans'] < req_b_lat:
                        print("Sorry, not enough coffee beans!")
                    elif self.coffee['water'] >= req_w_lat and self.coffee['milk'] >= req_m_lat and self.coffee['beans'] >= req_b_lat:
                        print("I have enough resources, making you a coffee!")
                        
                        self.coffee['water'] = self.coffee['water'] - 350
                        self.coffee['milk'] = self.coffee['milk'] - 75
                        self.coffee['beans'] = self.coffee['beans'] - 20
                        self.coffee['cups'] = self.coffee['cups'] - 1
                        self.coffee['money'] = self.coffee['money'] + 7
                
                elif int(option) == 3:
                    req_w_cap = 200
                    req_m_cap = 100
                    req_b_cap = 12
                    if self.coffee['water'] < req_w_cap:
                        print("Sorry, not enough water!")
                    elif self.coffee['milk'] < req_m_cap:
                        print("Sorry, not enough milk!")
                    elif self.coffee['beans'] < req_b_cap:
                        print("Sorry, not enough coffee beans!")
                    elif self.coffee['water'] >= req_w_cap and self.coffee['milk'] >= req_m_cap and self.coffee['beans'] >= req_b_cap:
                        print("I have enough resources, making you a coffee!")
                      
                        self.coffee['water'] = self.coffee['water'] - 200
                        self.coffee['milk'] = self.coffee['milk'] - 100
                        self.coffee['beans'] = self.coffee['beans'] - 12
                        self.coffee['cups'] = self.coffee['cups'] - 1
                        self.coffee['money'] = self.coffee['money'] + 6
                          
            
        ### FILL FUNCTION
        def fill():
            add_w = int(input("Write how many ml of water do you want to add:\n"))
            add_m = int(input("Write how many ml of milk do you want to add:\n"))
            add_b = int(input("Write how many grams of coffee beans do you want to add:\n"))
            add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
                  
            self.coffee['water'] = self.coffee['water'] + add_w
            self.coffee['milk'] = self.coffee['milk'] + add_m
            self.coffee['beans'] = self.coffee['beans'] + add_b
            self.coffee['cups'] = self.coffee['cups'] + add_cups
            self.coffee['money'] = self.coffee['money']
            
        ### TAKE FUNCTION
        def take():
           print(f"I gave you ${self.coffee['money']}") 
           self.coffee['water'] = self.coffee['water']
           self.coffee['milk'] = self.coffee['milk']
           self.coffee['beans'] = self.coffee['beans']
           self.coffee['cups'] = self.coffee['cups']
           self.coffee['money'] = self.coffee['money'] - self.coffee['money']
           
            
        ### REMAINING FUNCTION
        def remaining():
            print("The coffee machine has:")
            print(f"""
                {self.coffee['water']} of water
                {self.coffee['milk']} of milk
                {self.coffee['beans']} of coffee beans
                {self.coffee['cups']} of disposable cups
                ${self.coffee['money']} of money""")
                
        alpha = True
        while alpha != False:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                buy()
            elif action == "fill":
                fill()
            elif action == "take":
                take()
            elif action == "remaining":
                remaining()
            elif action == "exit":
                alpha = False
        
coffee = CoffeeMachine()
coffee.program()
