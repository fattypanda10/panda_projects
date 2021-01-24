# EULER PROBLEMS 1- 10


######################### EULER - 1

# a = int(input())
# ans = []
# i = 1
# while i < a:
#     if i % 3 ==0 or i % 5 == 0:
#         ans.append(i)
#         i += 1
#     else:
#         pass
#         i += 1
# print(sum(ans))



######################### EULER - 2

# def fibo_sumeven():
#     a = 1
#     b = 2
#     terms = [a, b]
#     i = 0
#     addy = 0
#     check = True
#     while check:
#         addy = terms[i] + terms[i + 1]
#         if addy < 4000000:
#             terms.append(addy)
#             i += 1
#             check = True
#         elif addy >= 4000000:
#             check = False
#     alpha = []
#     for i in terms:
#         if i % 2 ==0:
#             alpha.append(i)
#         else:
#             pass
#     return sum(alpha)
# x = fibo_sumeven()
# print(x)


######################### EULER - 3

# def prime_test(a):  #a > 1
#     if a != 2 and a % 2 == 0:
#         return "not prime"
#     elif a == 2 or a % 2 != 0:
#         i = 2
#         count = 0
#         if a == i:
#             return "prime"
#         elif a != i:
#             while i < a:
#                 if a % i != 0:
#                     count += 1
#                     i += 1
#                 elif a % i == 0:
#                     count = 0
#                     break
#             if count == 0:
#                 return "not prime"
#             elif count > 0:
#                 return "prime"
            
# d = int(input("Number: "))
# divisor = 2
# dividend = d
# while dividend >= divisor:
#     check = prime_test(divisor)
#     if check == 'prime' and dividend % divisor == 0:
#         condi = True
#         while condi:
#             div = dividend // divisor
#             dividend = div
#             if dividend % divisor == 0:
#                 continue
#             elif dividend % divisor != 0 and dividend != 1:
#                 divisor += 1
#                 condi = False
#             elif dividend == 1:
#                 condi = False
#     elif check == 'prime' and dividend % divisor != 0:
#         divisor += 1
#     elif check == 'not prime':
#         divisor += 1
# print(f"Greatest Prime Divisor: {divisor}")


######################### EULER - 4

# def str_rev(a):
#     check = []
#     for i in range(0, len(a)):
#         alpha = a[-1* (i + 1)]
#         check.append(alpha)
#     return ''.join(check)
        
# combi = []
# for i in range(100, 1000):
#     for j in range(100, 1000):
#         combi.append(i * j)
# palins = []
# for alpha in combi:
#     if str(alpha) == str_rev(str(alpha)):
#         palins.append(alpha)
#     else:
#         pass
# print(max(palins))
    

######################### EULER - 5

# def prime_test(a):  #a > 1
#     if a != 2 and a % 2 == 0:
#         return "not prime"
#     elif a == 2 or a % 2 != 0:
#         i = 2
#         count = 0
#         if a == i:
#             return "prime"
#         elif a != i:
#             while i < a:
#                 if a % i != 0:
#                     count += 1
#                     i += 1
#                 elif a % i == 0:
#                     count = 0
#                     break
#             if count == 0:
#                 return "not prime"
#             elif count > 0:
#                 return "prime"
            
# def prime_fact(d):
#     divisor = 2
#     dividend = d
#     divs_req = []
#     while dividend >= divisor:
#         check = prime_test(divisor)
#         if check == 'prime' and dividend % divisor == 0:
#             condi = True
#             while condi:
#                 div = dividend // divisor
#                 dividend = div
#                 divs_req.append(divisor)
#                 if dividend % divisor == 0:
#                     continue
#                 elif dividend % divisor != 0 and dividend != 1:
#                     divisor += 1
#                     condi = False
#                 elif dividend == 1:
#                     condi = False
#         elif check == 'prime' and dividend % divisor != 0:
#             divisor += 1
#         elif check == 'not prime':
#             divisor += 1
#     return divs_req
#     print(f"Greatest Prime Divisor: {divisor}")
#     print(f"Prime Factorization: {divs_req}")

# LCM

# def lcm_nos(a):  #a is a list of the numbers
#     fact = []
#     fact_set = []
#     common_count = {}
#     common_min = {}
#     final = 1
#     for i in range(0, len(a)):        
#         fact.append(prime_fact(a[i]))
#         fact_set.append(set(prime_fact(a[i])))
#     for j in range(1, len(fact_set)):
#         fact_set[0] = fact_set[0].union(fact_set[j])
#     for alpha in fact_set[0]:
#         common_count[str(alpha)+"s"] = []
#         for beta in fact:
#             common_count[str(alpha)+"s"].append(beta.count(alpha))
#     for k in fact_set[0]:
#         common_min["min_"+str(k)+"s"] = max(common_count[str(k)+"s"])
#         if common_min["min_"+str(k)+"s"] != 0:
#             final *= k ** common_min["min_"+str(k)+"s"]
#         else:
#             pass 
#     return final
# x= lcm_nos(list(range(1,20)))
# print(x)

# HCF not asked in Euler 5 but noted here for completeness of HCF & LCM stuff
#Extra

# def hcf_nos(a):  #a is a list of the numbers
#     fact = []
#     fact_set = []
#     common_count = {}
#     common_min = {}
#     final = 1
#     for i in range(0, len(a)):        
#         fact.append(prime_fact(a[i]))
#         fact_set.append(set(prime_fact(a[i])))
#     for j in range(1, len(fact_set)):
#         fact_set[0] = fact_set[0].union(fact_set[j])
#     for alpha in fact_set[0]:
#         common_count[str(alpha)+"s"] = []
#         # common_min["min_"+str(alpha)+"s"] = []
#         for beta in fact:
#             common_count[str(alpha)+"s"].append(beta.count(alpha))
#             # common_min["min_"+str(alpha)+"s"].append(min(common_count[str(alpha)+"s"]))
#     for k in fact_set[0]:
#         common_min["min_"+str(k)+"s"] = min(common_count[str(k)+"s"])
#         if common_min["min_"+str(k)+"s"] != 0:
#             final *= k ** common_min["min_"+str(k)+"s"]
#         else:
#             pass
#     return final
# x= hcf_nos([8, 12, 20])
# print(x)

######################### EULER - 6

# def ans(n):
#     a = []
#     b = []
#     for i in range(1, n+1):
#         a.append(i**2)
#         b.append(i)
#     alpha = sum(a)
#     beta = (sum(b)) ** 2
#     req = alpha - beta
#     return abs(req)

# x = ans(100)
# print(x)


######################### EULER - 7

# n = int(input("Number: "))
# count_prime = 0
# that_prime = 0
# i = 2
# while count_prime != n:
#     if prime_test(i) == 'prime':
#         that_prime = i
#         count_prime += 1
#         i += 1
#     else:
#         i += 1
# print(that_prime)


######################### EULER - 8

# number = """
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450"""

# numby = list(number)
# for i in numby:
#     if i == '\n':
#         numby.remove(i)
#     else:
#         pass
# alpha = ''.join(numby)
# start = 0
# end = 13
# greatest = 1
# prod = 1
# those_digs = 0
# while end != 1000:
#     quad = alpha[start:end]
#     for digit in quad:
#         prod *= int(digit)
#     if prod > greatest:
#         greatest = prod
#         those_digs = quad
#     else:
#         pass
#     prod = 1
#     start += 1
#     end += 1
# print(f"Greatest Product: {greatest}")
# print(f"Corresponding {end - start} digits: {those_digs}")


######################### EULER - 9

# import math as m

# def pyth_trip():
#     a = []
#     b = []
#     c = []
#     triplets = []
#     prod = 1
    
#     for alpha in range(1, 1001):
#         a.append(alpha**2)
#         b.append(alpha**2)
#         c.append(alpha**2)

#     for i in a:
#         for j in b:
#             if j > i:
#                 for k in c:
#                     if k > j:
#                         if (i + j == k) and (int(m.sqrt(i)) + int(m.sqrt(j)) + int(m.sqrt(k)) == 1000):
#                             triplets.append([int(m.sqrt(i)), int(m.sqrt(j)), int(m.sqrt(k))])
#                         else:
#                             pass
#                     else:
#                         pass
#             else:
#                 pass
                
#     for z in triplets:
#         for y in z:
#             prod *= y
        
#     print(f"Product of Pytho_Triplet: {prod}")
#     print(f"Pytho_Triplet: {triplets}")
    
# pyth_trip()
                    

######################### EULER - 10

# def prime_test(a):  #a > 1
#     if a != 2 and a % 2 == 0:
#         return "not prime"
#     elif a == 2 or a % 2 != 0:
#         i = 2
#         count = 0
#         if a == i:
#             return "prime"
#         elif a != i:
#             while i < a:
#                 if a % i != 0:
#                     count += 1
#                     i += 1
#                 elif a % i == 0:
#                     count = 0
#                     break
#             if count == 0:
#                 return "not prime"
#             elif count > 0:
#                 return "prime"

# def no_primes(b):   # b > 0
#     primes= []
#     if b == 1:
#         return primes
#     elif b == 2:
#         primes.append(b)
#         return primes
#     elif b > 2:
#         primes.append(2)
#         j = 3
#         while j <= b:
#             alpha = prime_test(j)
#             if alpha == 'prime':
#                 primes.append(j)
#                 j += 1
#             elif alpha == 'not prime':
#                 j += 1       
#     return primes

# main1 = [i for i in range(1, 2000000, 2) if (i % 10 != 5 or i == 5)]
# listy = no_primes(20000) #with 20000 time=54 sec, with 40000, time=1.44 min
# for k in listy:
#     main1 = [i for i in main1 if (i % k != 0 or i == k)]
# main1.remove(1)
# main1.insert(0,2)
# # print(main1[0:30])
# print(len(main1))
# print(sum(main1))
