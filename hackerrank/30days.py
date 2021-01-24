### These are some of the problems from HackerRank's 30-Day-Code challenge (completed successfully) solved at my end in Python


### CHECKING LEAP YEAR

# def is_leap(year):
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



### Age and Classes

# class Person:
#     def __init__(self,initialAge):
#         if initialAge < 0:
#             self.age = 0
#             print("Age is not valid, setting age to 0.")
#         elif initialAge > 0:
#             self.age = initialAge
#         # Add some more code to run some checks on initialAge
#     def amIOld(self):
#         if self.age < 13:
#             print("You are young.")
#         elif 13 <= self.age < 18:
#             print("You are a teenager.")
#         else:
#             print("You are old.")
#         # Do some computations in here and print out the correct statement to the console
#     def yearPasses(self):
#         self.age += 1
#         # Increment the age of the person in here

# t = int(input())
# for i in range(0, t):
#     age = int(input())         
#     p = Person(age)  
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()       
#     p.amIOld()
#     print("")


### Maximum no of consecutive 1s in the binary form of a number

# a = bin(int(input()))
# b = a[2:]
# c = ['1' * i for i in range(1, len(b) + 1)]
# ans = 0
# for j in c:
#     if j in b:
#         ans = j
#     else:
#         pass
# print(f"Max no. of consecutive 1s: {len(ans)}")
# print(f"Binary form: {b}")


#### Hourglass - Problem 11

# lines = 0
# big = []
# while lines < 6:
#     line = input()
#     big.append([int(i) for i in line.split()])
#     lines += 1
# count = 0
# a = 0
# b = 3
# j = 0
# k = 3
# small = []
# while b != 7:
#     while k != 7:
#         for i in range(a, b):
#             small.append(big[i][j:k])
#         j += 1
#         k += 1
#         count += 1
#     a += 1
#     b += 1
#     j = 0
#     k = 3
# three = []   
# for p in range(0, len(small) - 2, 3):
#     three.append([small[p], 
#                   small[p + 1], 
#                   small[p + 2]])
# # print(f"No. of 3x3 matrices: {count}")
# sumy = []
# for q in three:
#     alpha = sum(q[0]) + q[1][1] + sum(q[2])
#     sumy.append(alpha)
# print(max(sumy))


### Day 12 Problem - Inheritance 

# class Person:
# 	def __init__(self, firstName, lastName, idNumber):
# 		self.firstName = firstName
# 		self.lastName = lastName
# 		self.idNumber = idNumber
# 	def printPerson(self):
# 		print("Name:", self.lastName + ",", self.firstName)
# 		print("ID:", self.idNumber)

# class Student(Person):
#     #   Class Constructor
#     #   
#     #   Parameters:
#     #   firstName - A string denoting the Person's first name.
#     #   lastName - A string denoting the Person's last name.
#     #   id - An integer denoting the Person's ID number.
#     #   scores - An array of integers denoting the Person's test scores.
#     #
#     # Write your constructor here
    

#     #   Function Name: calculate
#     #   Return: A character denoting the grade.
#     #
#     # Write your function here
#     def __init__(self, firstName, lastName, id, scores):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = id
#         self.scores = scores

#     def calculate(self):
#         self.average = sum(self.scores) / len(self.scores)
#         if 90 <= self.average <= 100:
#             return "O"
#         elif 80 <= self.average < 90:
#             return "E"
#         elif 70 <= self.average < 80:
#             return "A"
#         elif 55 <= self.average < 70:
#             return "P"
#         elif 40 <= self.average < 55:
#             return "D"
#         elif self.average < 40:
#             return "T"
        
# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())


## Scope question

# a = [1,2,5]
# diff = 0
    
# p = 0
# q = 1
# while p != len(a) - 1:
#     for i in range(q, len(a)):
#         ab_diff = abs(a[p] - a[i])
#         if ab_diff > diff:
#             diff = ab_diff
#         else:
#             pass
#     p += 1
#     q += 1
# print(diff)


## Try Except Problem

# S = input().strip()
# try:
#     alpha = int(S)
#     print(alpha)
# except:
#     print("Bad String")

## Sorting porblem - Day 20! - Bubble Sort

# n = int(input())
# num_string = input()
# a = num_string.split()
# b = []
# for i in a:
#     b.append(int(i))
# count = 0
# numSwaps = 0
# while count != n:
#     for j in range(0, n - 1):
#         if b[j] >= b[j+1]:
#             c = b[j]
#             b[j] = b[j+1]
#             b[j+1] = c
#             numSwaps += 1
#         else:
#             pass
#     count += 1
# print(f"""Array is sorted in {numSwaps} swaps.
# First Element: {b[0]}
# Last Element: {b[-1]}""")


### Library - Due Date

# act = input().split()
# expect = input().split()

# actual = [int(i) for i in act]
# expected = [int(i) for i in expect]
# fine = -1

# if (actual[1] == expected[1]) and (actual[2] == expected[2]):
#     if actual[0] <= expected[0]:
#         fine = 0
#     elif actual[0] > expected[0]:
#         fine = 15 * (actual[0] - expected[0])
# elif (actual[1] < expected[1]) and (actual[2] == expected[2]):
#     fine = 0
# elif (actual[1] > expected[1]) and (actual[2] == expected[2]):
#     fine  = 500 * (actual[1] - expected[1])
# elif actual[2] > expected[2]:
#     fine = 10000
# elif actual[2] < expected[2]:
#     fine = 0

# print(fine)


### Prime Number

# import math
# def prime_test(a):  #a > 1
#     if a != 2 and a % 2 == 0:
#         return "Not prime"
#     elif a == 1:
#         return "Not prime"
#     elif a == 2 or a % 2 != 0:
#         i = 2
#         count = 0
#         if a == i:
#             return "Prime"
#         elif a != i:
#             while i <= math.ceil(math.sqrt(a)):
#                 if a % i != 0:
#                     i += 1
#                 elif a % i == 0:
#                     count = 1
#                     break
#             if count == 0:
#                 return "Prime"
#             elif count > 0:
#                 return "Not prime"
    
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
#             if alpha == 'Prime':
#                 primes.append(j)
#                 j += 1
#             elif alpha == 'Not prime':
#                 j += 1       
#     return primes

# a = int(input())
# i = 0
# numbers = []
# while i < a:
#     num = int(input())
#     numbers.append(num)
#     i += 1

# for j in numbers:
#     if len(str(j)) <= 9:
#         x = prime_test(j)
#         print(x)
#     elif len(str(j)) > 9:
#         if j % 2 == 0 or j % 10 == 5:
#             print("Not prime")
#         else:
#             limit = math.ceil(math.sqrt(j))
#             listy = no_primes(limit)
#             check = 0
#             for i in listy:
#                 if j % i != 0:
#                     pass
#                 elif j % i == 0:
#                     check = 1
#                     break
#             if check == 0:
#                 print("Prime")
#             else:
#                 print("Not prime")
    

#### BINARY TREE  Level Order

# import sys

# class Node:
#     def __init__(self,data):
#         self.right=self.left=None
#         self.data = data
# class Solution:
#     def insert(self,root,data):
#         if root==None:
#             return Node(data)
#         else:
#             if data<=root.data:
#                 cur=self.insert(root.left,data)
#                 root.left=cur
#             else:
#                 cur=self.insert(root.right,data)
#                 root.right=cur
#         return root

#     def levelOrder(self,root):

#         # def getHeight(self, root):
#         a = root.left
#         b = root.right
#         def path(node):
#             curr = node
#             count = 0
#             alpha = True
#             while alpha:
#                 if (curr.left != None) and (curr.right == None):
#                     count += 1
#                     curr = curr.left
#                 elif (curr.left == None) and (curr.right != None):
#                     count += 1
#                     curr = curr.right
#                 elif (curr.left != None) and (curr.right != None):
#                     p = path(curr.left)
#                     q = path(curr.right)
#                     count += max(p + 1, q + 1)
#                     alpha = False
#                 elif (curr.left == None) and (curr.right == None):
#                     alpha = False

#             return count

#         x = path(a) #left sub tree
#         y = path(b) # right sub tree
#         height_tree =  (1 + max(x, y))
#         # print(height_tree)

#         def children(node):
#             ans = []
#             curr = node
#             ans.append(curr.left)
#             ans.append(curr.right)
#             return ans  #list

#         def final(root):
#             lvl_order = [root.data]
#             curr = root
#             x = children(curr)
#             lvl = 0
#             while lvl != height_tree:
#                 temp = []
#                 for j in x:
#                     if type(j) != list:
#                         if j != None:
#                             lvl_order.append(j.data)
#                             p = children(j)
#                             temp.append(p)
#                         elif j == None:
#                             pass
#                     elif type(j) == list:
#                         for k in j:
#                             if k != None:
#                                 lvl_order.append(k.data)
#                                 p = children(k)
#                                 temp.append(p)
#                             elif k == None:
#                                 pass
#                 x = temp
#                 lvl += 1
#             return lvl_order

#         check = final(root)
#         print(*check)
        
# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# myTree.levelOrder(root)


#### BINARY TREE - FIND HEIGHT OF THE BINARY TREE 

# class Node:
#     def __init__(self,data):
#         self.right=self.left=None
#         self.data = data
# class Solution:
#     def insert(self,root,data):
#         if root==None:
#             return Node(data)
#         else:
#             if data<=root.data:
#                 cur=self.insert(root.left,data)
#                 root.left=cur
#             else:
#                 cur=self.insert(root.right,data)
#                 root.right=cur
#         return root

#     def getHeight(self, root):
#         a = root.left
#         b = root.right

#         def path(node):
#             curr = node
#             count = 0
#             alpha = True
#             while alpha:
#                 if (curr.left != None) and (curr.right == None):
#                     count += 1
#                     curr = curr.left
#                 elif (curr.left == None) and (curr.right != None):
#                     count += 1
#                     curr = curr.right
#                 elif (curr.left != None) and (curr.right != None):
#                     p = path(curr.left)
#                     q = path(curr.right)
#                     count += max(p + 1, q + 1)
#                     alpha = False
#                 elif (curr.left == None) and (curr.right == None):
#                     alpha = False

#             return count

#         x = path(a) #left sub tree
#         y = path(b) # right sub tree
#         return (1 + max(x, y))

    
# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height)       
    

### Gmail

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com

# a = int(input())
# i = 0
# names = []
# emails = []
# while i < a:
#     stuff = input().split()
#     names.append(stuff[0])
#     emails.append(stuff[1])
#     i += 1
# ans = []
# for i in range(len(emails)):
#     if '@gmail.com' in emails[i]:
#         listy = [names[i], emails[i]]
#         ans.append(listy)
#     else:
#         pass
# req_names = [i[0] for i in ans]
# req_names.sort()
# for i in req_names:
#     print(i)

####### BITSWISE AND - Day 29

# t = int(input())
# counter, data = 0, []
# while counter < t:
#     parts = input().split()
#     data.append([int(parts[0]), int(parts[1])])
#     counter += 1
# count = 0
# maxy = []
# for numby in range(len(data)):
#     n, k = data[numby][0], data[numby][1]
#     listy = range(1, n + 1)
#     max_AND = 0
#     if k == n:
#         for i in range(len(listy) - 3, len(listy)):
#             for j in range(i + 1, len(listy)):
#                 compy = listy[i] & listy [j]
#                 if max_AND < compy < k:
#                     max_AND = compy
#                     if (compy == k - 1) or (compy == k - 2):
#                             break
#         maxy.append(max_AND)
#     else:
#         for i in range(k - 3, k):
#             for j in range(i + 1, len(listy)):
#                 compy = listy[i] & listy [j]
#                 if max_AND < compy < k:
#                     max_AND = compy
#                     if (compy == k - 1) or (compy == k - 2):
#                         break
#         maxy.append(max_AND)
# for k in maxy:
#     print(k)
