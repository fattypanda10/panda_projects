##### Exercism - Python Track (26 problems) #########


### Exercise - 1 - HELLO WORLD
# print( "Hello, World!")



### Exercise - 2 - TWO FER
# def two_fer(*X):
#     if len(X) != 0:
#         return (f"One for {X[0]}, one for me.")
#     else:
#         return ("One for you, one for me.")



### Exercise - 3 - RAINDROPS
# def convert(number):
# 	result = ''
# 	
# 	if number % 3 == 0:
# 		result += "Pling"

# 	if number % 5 == 0:
# 		result += "Plang"

# 	if number % 7 == 0:
# 		result += "Plong"
# 		
# 	if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
# 		result = str(number)
# 	
# 	return result



### Exercise - 4 - HIGH SCORES
# def latest(scores):
# 	return scores[-1]


# def personal_best(scores):
# 	return max(scores)


# def personal_top_three(scores):
# 	a = scores
# 	ans = []
# 	if len(a) > 3:
# 		i = 0
# 		while i < 3:
# 			s = max(a)
# 			ans.append(s)
# 			a.remove(s)
# 			i += 1
# 		return ans

# 	elif len(a) <= 3:
# 		b = sorted(a, reverse = True)
# 		return b


### Exercise - 5 - MATRIX
# class Matrix:
#     def __init__(self, matrix_string):
#         listy = matrix_string.split('\n')
#         self.mat = []
#         for i in listy:
#             data = i.split()
#             conv = []
#             for x in data:
#                 conv.append(int(x))
#             self.mat.append(conv)

#     def row(self, index):
#         alpha = index - 1
#         return self.mat[alpha]

#     def column(self, index):
#         j = 0
#         p = []
#         col = []
#         while j < len(self.mat[0]):
#             for i in range(len(self.mat)):
#                 p.append(self.mat[i][j])
#             col.append(p)
#             p = []
#             j += 1
#         beta = index - 1
#         return col[beta]



### Exercise - 6 - HAMMING 
# def distance(strand_a, strand_b):
#     if len(strand_a) == 0 and len(strand_b) == 0:
#         return 0

#     elif len(strand_a) == 0 or len(strand_b) == 0:
#         if len(strand_a) == 0:
#             raise ValueError("Left strand empty")
#         else:
#             raise ValueError("Right strand empty")

#     elif len(strand_a) != len(strand_b):
#         if len(strand_a) > len(strand_b):
#             raise ValueError("Left strand longer")
#         elif len(strand_a) < len(strand_b):
#             raise ValueError("Right strand longer")

#     else:
#         count = 0
#         for i in range(len(strand_a)):
#             check = strand_a[i] == strand_b[i]
#             if not check:
#                 count += 1
#             else:
#                 pass
#         return count


### Exercise - 7 - ISOGRAM
# import string as s

# def is_isogram(string):

#     alpha_set = list(s.ascii_lowercase)
#     alpha_set.append(' ')
#     alpha_set.append('-')

#     count = 0
#     word = string.lower()
#     for i in alpha_set:
#         if i not in [' ', '-']:
#             if word.count(i) > 1:
#                 count = 1
#         elif i in [' ', '-']:
#             if word.count(i) > 1:
#                 pass
       
#     if count == 1:
#         return False
#     elif count == 0:
#         return True


### Exercise - 8 - SCRABBLE
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10

# def score(word):
#     set_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T', '1']
#     set_2 = ['D', 'G', '2']
#     set_3 = ['B', 'C', 'M', 'P', '3']
#     set_4 = ['F', 'H', 'V', 'W', 'Y', '4']
#     set_5 = ['K', '5']
#     set_6 = ['J', 'X', '8']
#     set_7 = ['Q', 'Z', '10']
#     set_all = [set_1, set_2, set_3, set_4, set_5, set_6, set_7]
#     points = {}
#     i = 0
#     while i < 7:
#         for j in set_all:
#             for k in j[:-1]:
#                 points.update({k: int(j[-1])})
#         i += 1
#     score = 0
#     the_word = word.upper()
#     for x in the_word:
#         score += points[x]
#     return score


### Exercise - 9 - ACRONYM
# def abbreviate(words):
#     delimits = ['_', '-']
#     first_letters = []
#     wordies = words.split()
    
#     for i in delimits:
#         while wordies.count(i) != 0:
#             wordies.remove(i)
#         for j in wordies:
#             if i in j:
#                 if (j[0] == i) or (j[-1] == i):
#                     position = wordies.index(j)
#                     wordies.remove(j)
#                     new = j.strip(i)
#                     wordies.insert(position, new)
#                 else:
#                     position = wordies.index(j)
#                     wordies.remove(j)
#                     j = j.split(i)
#                     for k in range(len(j) - 1, -1, -1):
#                         wordies.insert(position, j[k])       
#     for i in wordies:
#         first_letters.append(i[0].upper())
#     abb = ''.join(first_letters)
#     return abb



### Exercise - 10 - Difference of Squares
# def square_of_sum(number):
#     n = number
#     sum_sq = ((n * (n + 1)) // 2) ** 2
#     return sum_sq


# def sum_of_squares(number):
#     n = number
#     sq = [i ** 2 for i in range(n + 1)]
#     return sum(sq)


# def difference_of_squares(number):
#     alpha = square_of_sum(number)
#     beta = sum_of_squares(number)
#     return alpha - beta



### Exercise - 11 - Leap
# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 != 0:
#             leap = True
#         elif year % 100 == 0 and year % 400 != 0:
#             leap = False
#         elif year % 100 == 0 and year % 400 == 0:
#             leap = True
#     else:
#         leap = False
#     return leap



### Exercise - 12 - String Reversal
# def reverse(text):
#     a = text
#     check = []
#     beta = ''
#     for i in range(0, len(a)):
#         alpha = a[-1 * (i + 1)]
#         check.append(alpha)
#     return beta.join(check)


### Exercise - 13 - Sum of multiples
# import math as m


# def sum_of_multiples(limit, multiples):
#     mul_list = []
#     for i in multiples:
#         if i != 0:
#             for j in range(1, m.ceil(limit / i)):
#                 if ((i * j) < limit) and ((i * j) not in mul_list):
#                     mul_list.append(i * j)
#         else:
#             mul_list.append(0)
#     return sum(mul_list)



### Exercise - 14 - Armstrong Number
# def is_armstrong_number(number):
#     num_str = str(number)
#     len_num_str = len(num_str)
#     sumy = 0
#     for i in num_str:
#         sumy += (int(i) ** len_num_str)
#     return True if (sumy == number) else False


## Exercise - 15 - Robot name - Good!
# import random as r
# import string as s

# used_seeds = []


# def gen_name():
#     seed = r.random()
#     while seed in used_seeds != False:
#         seed = r.random()
#     used_seeds.append(seed)
#     alpha_set = list(s.ascii_uppercase)
#     all_chars = []
#     counter = 0
#     dig_len = 3
#     alpha_len = 2
#     while counter < alpha_len:
#         all_chars.append(r.choice(alpha_set))
#         counter += 1

#     counter = 0

#     while counter < dig_len:
#         all_chars.append(str(r.randint(0, 9)))
#         counter += 1
#     name = ''.join(all_chars)
#     return name


# class Robot:

#     def __init__(self):
#         self.name = gen_name()

#     def reset(self):
#         self.name = ''
#         self.name = gen_name()



### Exercise - 16 - Pangram
# import string


# def is_pangram(sentence):
#     alpha_set = string.ascii_lowercase
#     non_alpha_set = ['-', " ' ", '_', '.', ' " ']
#     used_alpha = []
#     sent_split = sentence.split()
#     combi_sent = (''.join(sent_split)).lower()
#     for k in alpha_set:
#         if (k in combi_sent) and (k not in used_alpha) and (k not in non_alpha_set):
#             used_alpha.append(k)
#     return True if len(used_alpha) == 26 else False

        

### Exercise - 17 - RNA Transcription
# def to_rna(dna_strand):
#     code = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
#     rna = []
#     if dna_strand == '':
#         return ''
#     else:
#         for i in dna_strand:
#             rna.append(code[i])
#         return ''.join(rna)


### Exercise - 18 - Resistor Color
# def color_code(color):
#     codes = {'black': 0,
#              'brown': 1,
#              'red': 2,
#              'orange': 3,
#              'yellow': 4,
#              'green': 5,
#              'blue': 6,
#              'violet': 7,
#              'grey': 8,
#              'white': 9}
#     return codes[color]


# def colors():
#     colors = ['black',
#               'brown',
#               'red',
#               'orange',
#               'yellow',
#               'green',
#               'blue',
#               'violet',
#               'grey',
#               'white']
#     return colors



### Exercise - 19 - Resistor Colour Duo
# def value(colors):
#     codes = {'black': 0,
#               'brown': 1,
#               'red': 2,
#               'orange': 3,
#               'yellow': 4,
#               'green': 5,
#               'blue': 6,
#               'violet': 7,
#               'grey': 8,
#               'white': 9}

#     resistance = []
#     for i in colors[0:2]:
#         resistance.append(str(codes[i]))
#     return int(''.join(resistance))


### Exercise - 20 - Luhn Algo! - Great!
# class Luhn:
#     def __init__(self, card_num):
#         self.cardy = card_num

#     def valid(self):
#         card_split = self.cardy.split()
#         card_no1 = ''.join(card_split)
#         if len(card_no1) <= 1:
#             return False
#         for i in card_no1:
#             if i.isdigit() == False:
#                 return False
#         card_no2 = [int(card_no1[i]) for i in range(len(card_no1))]
#         card_no2.reverse()
#         card_no2 = [card_no2[i] * 2 if i % 2 != 0 else card_no2[i]
#                     for i in range(len(card_no2))]
#         card_no2.reverse()
#         card_no2 = [card_no2[i] - 9 if card_no2[i] > 9 else card_no2[i]
#                     for i in range(len(card_no2))]
#         sum_digs = 0
#         for i in card_no2:
#             sum_digs += i
#         if sum_digs % 10 == 0:
#             return True
#         else:
#             return False


### Exercise - 21 - Darts
# import math

# def score(x, y):
#     r = math.sqrt((x ** 2) + (y ** 2))
#     if 0 <= r <= 1:
#         return 10
#     elif 1 < r <= 5:
#         return 5
#     elif 5 < r <= 10:
#         return 1
#     elif r > 10:
#         return 0

### Exercise - 22 -  Series
# def slices(series, length):
#     if series == '' or length <= 0 or length > len(series):
#         raise ValueError("Invalid Input")
#     else:
#         size = length
#         start = 0
#         end = start + size
#         sub_str = []
#         while end != len(series) + 1:
#             sub_str.append(series[start:end])
#             start += 1
#             end += 1
#         return sub_str



### Exercise - 23 - Bob
# import string

# def response(hey_bob):
#     ques = hey_bob

#     check1 = 0
#     check_set1 = list(string.ascii_lowercase)
#     for i in ques:
#         if i in check_set1:
#             check1 = 1
#             break
#     check2 = 0
#     check_set2 = [str(i) for i in range(0, 10)]
#     for i in ques:
#         if i in check_set2:
#             check2 = 1
#             break
#     if '?' in ques and ques.count('?') == 1 and ques.isupper() != True:
#         if ques.strip()[-1] == '?':
#             return 'Sure.'
#         else:
#             return 'Whatever.'
#     elif ques.isupper() == True and ques[-1] != '?':
#         return 'Whoa, chill out!'
#     elif ques.isupper() == True and ques[-1] == '?':
#         return "Calm down, I know what I'm doing!"
#     elif (check1 == 0) and ((ques.count("\t") >= 1) or (ques.count("\n") >= 1) or (ques.count(" ") >= 0)) and (check2 == 0):
#         return 'Fine. Be that way!'
#     else:
#         return "Whatever."



### Exercise - 24 - Sieve - Good!! Finally!!
# def primes(limit):
#     if limit == 1:
#         return []
#     else:
#         listy = set(range(2, limit + 1))
#         p = 2
#         while p != limit:
#             to_be_removed = set(range(2 * p, limit + 1, p))
#             removal = listy.difference(to_be_removed)
#             listy = removal
#             p += 1
#         return (sorted(list(listy)))


### Exercise - 25 - nth Prime
# def sum_prop_fact(n):
#     facts = []
#     count = 0
#     for i in range(1, n):
#         if n % i == 0:
#             facts.append(i)
#             count += 1
#     return sum(facts)


# def classify(number):
#     if number == 0 or number == -1:
#         raise ValueError("Invalid Input")
#     else:
#         sum_facts = sum_prop_fact(number)
#         if sum_facts == number:
#             return "perfect"
#         elif sum_facts > number:
#             return 'abundant'
#         elif sum_facts < number:
#             return 'deficient'



### Exercise - 26 - Pythogorean Triplet
# import math as m

# def pyth_trip(number):
#     a = [(i ** 2) for i in range(1, number + 1)]
#     b = [(i ** 2) for i in range(1, number + 1)]
#     c = [(i ** 2) for i in range(1, number + 1)]
#     triplets = []
    
#     for i in a:
#         for j in b:
#             if j > i:
#                 for k in c:
#                     if k > j:
#                         if (i + j == k) and (int(m.sqrt(i)) + int(m.sqrt(j)) + int(m.sqrt(k)) == number):
#                             triplets.append([int(m.sqrt(i)), int(m.sqrt(j)), int(m.sqrt(k))])
                
#     return triplets

# print(pyth_trip(30000))ß

# import math as m

# def pyth_trip(number):
#     a = range(1, number + 1)
#     b = range(1, number + 1)
#     c = range(1, number + 1)
#     triplets = []
    
#     for i in a:
#         for j in b:
#             if j > i:
#                 for k in c:
#                     if k > j:
#                         if ((i**2) + (j**2) == (k**2)) and (i + j + k == number):
#                             triplets.append([i, j, k])
                
#     return triplets

# print(pyth_trip(1000))


### Exercise - 26 - Anagram
# import random


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         while n != 1:
#             alpha = 1
#             alpha *= n * factorial(n - 1)
#             n -= 1
#             return alpha


# def find_anagrams(word, candidates):
#     case = {}
#     for alpha in candidates:
#         case[alpha.lower()] = alpha
#     mod_cand = [i.lower() for i in candidates if len(i) == len(word)]
#     word_itself = list(word.lower())
#     word_itself1 = sorted(word_itself)
#     mod_cand1 = []
#     for x in mod_cand:
#         y = sorted(list(x.lower()))
#         if (y == word_itself1):
#             if (x != word.lower()):
#                 mod_cand1.append(x)
#     available = []
#     if mod_cand1 == []:
#         return available
#     else:
#         used = []
#         repeats = {}
#         for j in word_itself:
#             counter = word_itself.count(j)
#             if counter > 1:
#                 repeats[j] = counter
#         limit = factorial(len(word))
#         for k in repeats.values():
#             limit = limit // factorial(k)
#         limit -= 1
#         while len(used) != limit:
#             b = list(word.lower())
#             c = random.sample(b, len(word))
#             d = ''.join(c)
#             if d != word and d not in used:
#                 used.append(d)
#                 for k in mod_cand1:
#                     if k == d:
#                         available.append(case[k])
#                 if len(available) == len(mod_cand1):
#                     break
#         return available
