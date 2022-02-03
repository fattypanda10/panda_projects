### REGEX Engine ### 
#### [Definitely not one of the best designs: would think it over once again!] ####

# string compare - single character
def regex_str_comp(reg_ex, stringy):
    if reg_ex == '':
        return True
    elif reg_ex == '' and stringy == '':
        return True
    elif reg_ex != '' and stringy == '':
        return False
    elif reg_ex == '.':
        return True
    else:
        return reg_ex == stringy

# with recursion - EQUAL
def match_eq_len_str_recur(reg_ex, stringy):
    if len(reg_ex) == 1 or len(reg_ex) == 0:
        return regex_str_comp(reg_ex, stringy)
    else:
        checker = []
        i, j = 0, 1
        while j != len(reg_ex) + 1:
            checker.append(match_eq_len_str_recur(reg_ex[i:j], stringy[i:j]))
            i += 1
            j += 1
    return True if all(checker) else False

## with recursion - Unequal
def match_uneq_len_str_recur(reg_ex, stringy):
    if len(reg_ex) > len(stringy):
        return False
    
    elif len(reg_ex) <= len(stringy):
        i, j = 0, len(reg_ex)
        check = []
        while j != len(stringy) + 1:
            check.append(match_eq_len_str_recur(reg_ex, stringy[i:j]))
            i += 1
            j += 1
        return True if any(check) else False
            
# Start and End characters matching with ^ and $   
def start_end_str_match(reg_ex, stringy):
    if reg_ex == "^." or reg_ex == ".$":
        return True
    elif "^" in reg_ex and "$" not in reg_ex:
        reg_ex1 = reg_ex[1:]
        return False if len(stringy) < len(reg_ex1) else (reg_ex1 == stringy[:len(reg_ex1)])
    elif "^" not in reg_ex and "$" in reg_ex:
        reg_ex1 = reg_ex[:-1]
        return False if len(stringy) < len(reg_ex1) else (reg_ex1 == stringy[-1 * len(reg_ex1):])
    elif "^" in reg_ex and "$" in reg_ex:
        reg_ex1 = reg_ex[1:-1]
        return reg_ex1 == stringy
    elif "^" not in reg_ex and "$" not in reg_ex:
        return match_eq_len_str_recur(reg_ex, stringy) if len(reg_ex) == len(stringy) else match_uneq_len_str_recur(reg_ex, stringy)
    
# Matching for "?", "*", "+"
def qm_star_plus_str_match(reg_ex, stringy):
    if (reg_ex[0] == "^" and reg_ex[-1] == "$"): 
        reg_ex = reg_ex.rstrip("$")
        reg_ex = reg_ex.lstrip("^")
        if reg_ex[-1] != stringy[-1]:
            return False
        elif ("+" in reg_ex or "*" in reg_ex):
            return True
    
    elif reg_ex[0] == "^" or reg_ex[-1] == "$":
        reg_ex = reg_ex.replace("+", "")
        return start_end_str_match(reg_ex, stringy)
    
    elif "?" in reg_ex:
        reg_ex = reg_ex.rstrip("$")
        reg_ex = reg_ex.lstrip("^")
        if ".?" in reg_ex:
            if len(stringy) < len(reg_ex) - 2:
                return False
            else:
                return True
        elif reg_ex.index("?") == 0:
            return True
        else:
            qm_ind_prec = reg_ex.index("?") - 1
            reg_ex1 = reg_ex.replace("?", "")
            check1 = reg_ex1 == stringy
            check0 = reg_ex1.replace(reg_ex1[qm_ind_prec], '') == stringy
            return check1 or check0
    
    elif "*" in reg_ex:
        reg_ex = reg_ex.rstrip("$")
        reg_ex = reg_ex.lstrip("^")
        if ".*" in reg_ex:
            if len(stringy) < len(reg_ex) - 2:
                return False
            else:
                return True
        else:
            star_ind_prec = reg_ex.index("*") - 1
            reg_ex1 = reg_ex.replace("*", '')
            check0 = reg_ex1.replace(reg_ex1[star_ind_prec], '') == stringy
            check_more = reg_ex1[:star_ind_prec] + reg_ex1[star_ind_prec] + reg_ex1[star_ind_prec + 1:]
            checks = []
            if len(check_more) == len(stringy):
                checks.append(check_more == stringy)
            else:
                i = 1
                while len(check_more) <= len(stringy):
                    check_more = reg_ex1[:star_ind_prec] + reg_ex1[star_ind_prec] * i + reg_ex1[star_ind_prec + 1:]
                    checks.append(check_more == stringy)
                    i += 1
            return any(checks) or check0

    elif "+" in reg_ex:
        reg_ex = reg_ex.rstrip("$")
        reg_ex = reg_ex.lstrip("^")
        if ".+" in reg_ex:
            if len(stringy) < len(reg_ex) - 2:
                return False
            else:
                return True
        else:
            plus_ind_prec = reg_ex.index("+") - 1
            reg_ex1 = reg_ex.replace("+", '')
            check1 = reg_ex1 == stringy
            check_more = reg_ex1[:plus_ind_prec] + reg_ex1[plus_ind_prec] + reg_ex1[plus_ind_prec + 1:]
            checks = []
            i = 1
            while len(check_more) < len(stringy):
                check_more = reg_ex1[:plus_ind_prec] + reg_ex1[plus_ind_prec] * i + reg_ex1[plus_ind_prec + 1:]
                checks.append(check_more == stringy)
                i += 1
            
            return any(checks) or check1


### Main
reg_str = input().split('|')
reg_ex = reg_str[0]
stringy = reg_str[1]

if "\\" in reg_ex:
    if reg_ex[0] == "^" or reg_ex[-1] == "$":
        reg_ex = reg_ex.replace("\\", "")
        print(start_end_str_match(reg_ex, stringy))
        
    else:
        indy = reg_ex.index("\\")
        reg_ex = reg_ex[:indy] + reg_ex[indy + 1:]
        if reg_ex == "?" or reg_ex == "*" or reg_ex == "+":
            print(True)
        elif "=" in stringy:
            print(reg_ex in stringy)
        else:
            print(reg_ex == stringy)
    
elif (len(reg_ex) == len(stringy) or len(reg_ex) == 0) and (('?' not in reg_ex) and ('*' not in reg_ex) and ('+' not in reg_ex)):
    print(match_eq_len_str_recur(reg_ex, stringy))
    
elif (reg_ex[0] == '^' or reg_ex[-1] == '$') and (('?' not in reg_ex) and ('*' not in reg_ex) and ('+' not in reg_ex)):
    print(start_end_str_match(reg_ex, stringy))
    
elif len(reg_ex) != len(stringy) and (('?' not in reg_ex) and ('*' not in reg_ex) and ('+' not in reg_ex)):
    print(match_uneq_len_str_recur(reg_ex, stringy))
    
else:
    print(qm_star_plus_str_match(reg_ex, stringy))
