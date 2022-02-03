import math as math
import sys

args = sys.argv
args_1 = args[1::]
paras = []
vals = []   # possible = ['--type', '--payment', '--principal', '--periods', '--interest']

for i in range(0, len(args_1)):
    paras.append(args_1[i][2:args_1[i].index('=')])
    if i == 0:
        vals.append((args_1[i][args_1[i].index('=')+1::]))
    else:
        vals.append(float((args_1[i][args_1[i].index('=')+1::])))

if len(vals) != 4 or min(vals[1::]) < 0:
    print("Incorrect parameters.")

else:
    if vals[0]  == "annuity":
        if 'periods' not in paras: #periods
            
            credit_prin = float(vals[paras.index('principal')])
            monthly_paymt = float(vals[paras.index('payment')]) #annuity
            credit_int = float(vals[paras.index('interest')])
            
            credit_int_month = credit_int / (12 * 100)
            numer = monthly_paymt
            denomi = ((monthly_paymt - (credit_int_month * credit_prin)))
            duration = math.ceil(math.log((numer / denomi), (1 + credit_int_month)))
            
            if duration == 1:
                print(f"You need {duration} month to repay this credit!")
            elif 1 < duration < 12:
                print(f"You need {duration} months to repay this credit!")
            elif duration == 12:
                print(f"You need {duration/duration} year to repay this credit!")
            elif duration > 12:
                years = duration // 12
                monthy = duration % 12
                if monthy == 0:
                    print(f"You need {years} years to repay this credit!")
                elif monthy == 1:
                    print(f"You need {years} years and {monthy} month to repay this credit!")
                elif monthy > 1:
                    print(f"You need {years} years and {monthy} months to repay this credit!")
            
            overpay = math.ceil((monthly_paymt * duration) - (credit_prin))
            print(f"Overpayment = {overpay}")
           
        elif 'payment' not in paras:    #payment
            
            credit_prin = float(vals[paras.index('principal')])
            count_per = int(vals[paras.index('periods')])
            credit_int = float(vals[paras.index('interest')])
            
            credit_int_month = credit_int / (12 * 100)
            numer = (credit_prin) * (credit_int_month) * (math.pow((1 + credit_int_month), count_per))
            denomi = (math.pow((1 + credit_int_month), count_per)) - 1
            
            annu = math.ceil(numer / denomi)
            overpay = math.ceil((annu * count_per) - (credit_prin))
            print(f"Your annuity payment = {annu}!")
            print(f"Overpayment = {overpay}")
            
        elif 'principal' not in paras:    #principal
            
            monthly_paymt = float(vals[paras.index('payment')]) #annuity
            count_per = int(vals[paras.index('periods')])
            credit_int = float(vals[paras.index('interest')])
            
            credit_int_month = credit_int / (12 * 100)
            numer = (monthly_paymt) * ((math.pow((1 + credit_int_month), count_per)) - 1)
            denomi = (credit_int_month) * (math.pow((1 + credit_int_month), count_per))
            princi = math.ceil((numer / denomi))
            overpay = math.ceil((monthly_paymt * count_per) - (princi))
            
            print(f"Your credit principal = {princi}!")
            print(f"Overpayment = {overpay}")
            
    elif vals[0] =='diff':
        credit_prin = float(vals[paras.index('principal')])
        count_per = int(vals[paras.index('periods')])
        credit_int = float(vals[paras.index('interest')])
        
        credit_int_month = credit_int / (12 * 100)
        count = 1
        total = 0
        while count <= count_per:
            alpha = (credit_prin / count_per)
            beta = (credit_int_month) * (((count_per * credit_prin) - (credit_prin * (count - 1))) / (count_per))
            diff_pay = math.ceil(alpha + beta)
            print(f"Month {count}: paid out {diff_pay}")
            total += diff_pay
            count += 1
        
        overpay = math.ceil(total - credit_prin)
        print(f"\nOverpayment = {overpay}") 
