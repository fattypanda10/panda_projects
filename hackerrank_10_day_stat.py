### HackerRank - 10 days of Statistics {Completed} ###

####################################################################

## MEAN, MEDIAN, MODE

numby = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]

# mean
mean = round((sum(numbers) / len(numbers)), 1)

# median
numb_sort = sorted(numbers)
if len(numb_sort) % 2 == 0:
    median = (numb_sort[(len(numb_sort) // 2) - 1] + numb_sort[((len(numb_sort) // 2) + 1) - 1]) / 2
    median = round(median, 1)
else:
    median = numb_sort[((len(numb_sort) + 1) // 2) - 1]
    median = round(median, 1)
  
# mode
numb_counts = {i:numbers.count(i) for i in numbers}
max_numb, max_count = 0, 0
for numby, counts in numb_counts.items():
    if counts > max_count:
        max_count, max_numb = counts, numby
    elif (counts == max_count) and (numby < max_numb):
        max_count, max_numb = counts, numby

mode = max_numb

print(f"""
{mean}
{median}
{mode}
""")



####################################################################

## WEIGHTED MEAN

num_el = int(input())
numby = input().split()
numby = [int(i) for i in numby]
weights = input().split()
weights = [int(i) for i in weights]
sumy = 0
for i in range(len(numby)):
    sumy += numby[i] * weights[i]

weight_mean = round((sumy / sum(weights)), 1)
print(weight_mean)


####################################################################

## STANDARD DEVIATION

import math

num_el = int(input())
numbs = input().split()
numbs = [int(i) for i in numbs]

numb_mean = sum(numbs) / len(numbs)
el_diff = [(i - numb_mean) ** 2 for i in numbs]
numerator = sum(el_diff)

std_dev = math.sqrt(numerator / len(numbs))
std_dev_rnd = round(std_dev, 1)
print(std_dev_rnd)



####################################################################

##### QUARTILE

def median(numbs):
    numb_sort = sorted(numbs)
    if len(numb_sort) % 2 == 0:
        median = (numb_sort[(len(numb_sort) // 2) - 1] + numb_sort[((len(numb_sort) // 2) + 1) - 1]) / 2
        median = round(median, 1)
    else:
        median = numb_sort[((len(numb_sort) + 1) // 2) - 1]
        median = round(median, 1)
        
    return median 
    
# Main
numby = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]
numbers_sort = sorted(numbers)

if len(numbers_sort) % 2 == 0:
    q2 = median(numbers)
    left_half = numbers_sort[:(len(numbers_sort) // 2)]
    right_half = numbers_sort[(len(numbers_sort) // 2):]
    q1 = median(left_half)
    q3 = median(right_half)
else:
    q2 = median(numbers)
    left_half = numbers_sort[:numbers_sort.index(q2)]
    right_half = numbers_sort[numbers_sort.index(q2) + 1:]
    q1 = median(left_half)
    q3 = median(right_half)
    
print(int(q1))
print(int(q2))
print(int(q3))
    

####################################################################

##### INTERQUARTILE RANGE WITH FREQUENCY DATA

def median(numbs):
    numb_sort = sorted(numbs)
    if len(numb_sort) % 2 == 0:
        median = (numb_sort[(len(numb_sort) // 2) - 1] + numb_sort[((len(numb_sort) // 2) + 1) - 1]) / 2
    else:
        median = numb_sort[((len(numb_sort) + 1) // 2) - 1]

    return median 
    

def quartile(numbers):
    numbers_sort = sorted(numbers)
    if len(numbers_sort) % 2 == 0:
        q2 = median(numbers)
        left_half = numbers_sort[:(len(numbers_sort) // 2)]
        right_half = numbers_sort[(len(numbers_sort) // 2):]
        q1 = median(left_half)
        q3 = median(right_half)
    else:
        q2 = median(numbers)
        left_half = numbers_sort[:((len(numbers_sort) + 1) // 2) - 1]
        right_half = numbers_sort[((len(numbers_sort) + 1) // 2):]
        q1 = median(left_half)
        q3 = median(right_half)
        
    return q1, q2, q3
    
# Main
numby = int(input())

X = input().split()
X = [[int(i)] for i in X]

F = input().split()
F = [int(i) for i in F]

numbers = [X[i] * F[i] for i in range(len(X))]
numbers1 = []
for i in numbers:
    for j in i:
        numbers1.append(j)

Q1, Q2, Q3 = quartile(numbers1)
print(round(float(Q3 - Q1), 1))


####################################################################

##### BINOMIAL DISTRIBUTION - 1

import math as m
vals = input().split()
ratio = float(vals[0])/float(vals[1])
pg = 1 / (ratio + 1)
pb = 1 - pg
n = 6
prob = 0
for i in range(3,7):
    combi = (m.factorial(n)) / ((m.factorial(i)) * (m.factorial(n - i)))
    p = combi * (pb**i) * (pg**(n - i))
    prob += p
print(round(prob, 3))



####################################################################

##### BINOMIAL DISTRIBUTION - 2

import math as m
vals = input().split()
pd = float(vals[0]) / 100
pnd = 1 - pd
n = int(vals[1])
part_a = 0
part_b = 0
for i in range(0,3):
    combi = (m.factorial(n)) / ((m.factorial(i)) * (m.factorial(n - i)))
    p = combi * (pd**i) * (pnd**(n - i))
    part_a += p

for i in range(2,11):
    combi = (m.factorial(n)) / ((m.factorial(i)) * (m.factorial(n - i)))
    p = combi * (pd**i) * (pnd**(n - i))
    part_b += p

print(round(part_a, 3))
print(round(part_b, 3))



####################################################################

##### GEOMETRIC DISTRIBUTION - 1

# defect = success
vals = input().split()
inspect = int(input())
pd = float(vals[0]) / float(vals[1])
prob = ((1 - pd) ** (inspect - 1)) * (pd)
print(round(prob, 3))



####################################################################

##### GEOMETRIC DISTRIBUTION - 2

# defect = success
vals = input().split()
inspect = int(input())
pd = float(vals[0]) / float(vals[1])
prob = 0
for i in range(0, inspect):
    x = ((1 - pd) ** i) * (pd)
    prob += x
print(round(prob, 3))



####################################################################

##### POISSON DISTRIBUTION - 1

import math as m

mean = float(input())
var = int(input())
prob = (((m.e) ** (-mean)) * (mean ** var)) / m.factorial(var)
print(round(prob, 3))



####################################################################

##### POISSON DISTRIBUTION - 2

means = input().split()
mean_A = float(means[0])
mean_B = float(means[1])
mach_A_cost = 160 + 40 * (mean_A + ((mean_A) ** 2))
mach_B_cost = 128 + 40 * (mean_B + ((mean_B) ** 2))
print(round(mach_A_cost, 3))
print(round(mach_B_cost, 3))



####################################################################

##### NORMAL DISTRIBUTION - 1

import math as m
mean = 20
std_dev = 2
part_a = 19.5
part_b_lower = 20
part_b_upper = 22

cumu_prob = 0.5 * (1 + m.erf((part_a - mean) / (std_dev * m.sqrt(2))))

b_up = 0.5 * (1 + m.erf((part_b_upper - mean) / (std_dev * m.sqrt(2))))
b_low = 0.5 * (1 + m.erf((part_b_lower - mean) / (std_dev * m.sqrt(2))))

print(round(cumu_prob, 3))
print(round(b_up - b_low, 3))



####################################################################

##### NORMAL DISTRIBUTION - 2


import math as m
mean = 70
std_dev = 10
higher_than_80 = 80
passed = 60
failed = 60
ans1 = 1 - (0.5 * (1 + m.erf((higher_than_80 - mean) / (std_dev * m.sqrt(2)))))
ans2 = 1 - (0.5 * (1 + m.erf((passed - mean) / (std_dev * m.sqrt(2)))))
ans3 = 0.5 * (1 + m.erf((failed - mean) / (std_dev * m.sqrt(2))))

ans = [ans1, ans2, ans3]
for i in ans:
    print(round(i * 100, 2))



####################################################################

##### CENTRAL LIMIT THEOREM - 1

import math as m

pop_mean = 205
pop_stddev = 15
n_boxes = 49
normal_mean = n_boxes * pop_mean
normal_stddev = m.sqrt(n_boxes) * pop_stddev

ans = (0.5 * (1 + m.erf((9800 - normal_mean) / (normal_stddev * m.sqrt(2)))))

print(round(ans, 4))



####################################################################

##### CENTRAL LIMIT THEOREM - 2

import math as m

no_students = 100
max_tickets = 250
tick_pop_mean = 2.4
tick_pop_stddev = 2.0

tick_norm_mean = tick_pop_mean * no_students
tick_norm_stddev = m.sqrt(no_students) * tick_pop_stddev

ans = 0.5 * (1 + m.erf((250 - tick_norm_mean) / (tick_norm_stddev * m.sqrt(2))))

print(round(ans, 4))



####################################################################

##### CENTRAL LIMIT THEOREM - 3

import math as m

samp_size = 100
pop_mean = 500
pop_stddev = 80
z = 1.96
a = pop_mean - (z * (pop_stddev / m.sqrt(samp_size)))
b = pop_mean + (z * (pop_stddev / m.sqrt(samp_size)))
print(round(a, 2))
print(round(b, 2))



####################################################################

##### PEARSON CORRELATION COEFFICIENT 1

import math as m

def stddev(array_of_nums):
    numbs = array_of_nums
    numb_mean = sum(numbs) / len(numbs)
    el_diff = [(i - numb_mean) ** 2 for i in numbs]
    numerator = sum(el_diff)
    std_dev = m.sqrt(numerator / len(numbs))
    return std_dev

def mean(array_of_nums):
    return (sum(array_of_nums) / len(array_of_nums))

size = int(input())
x_input = input().split()
x = [float(i) for i in x_input]
y_input = input().split()
y = [float(i) for i in y_input]

mean_x = mean(x)
sd_x = stddev(x)
mean_y = mean(y)
sd_y = stddev(y)

numer = 0
for i in range(size):
    alpha = (x[i] - mean_x) * (y[i] - mean_y)
    numer += alpha
deno = size * sd_x * sd_y

pear_coeff = numer / deno
print(round(pear_coeff, 3))



####################################################################

##### SPEARMAN'S RANK COEFFICIENT 

import math as m

def stddev(array_of_nums):
    numbs = array_of_nums
    numb_mean = sum(numbs) / len(numbs)
    el_diff = [(i - numb_mean) ** 2 for i in numbs]
    numerator = sum(el_diff)
    std_dev = m.sqrt(numerator / len(numbs))
    return std_dev

def mean(array_of_nums):
    return (sum(array_of_nums) / len(array_of_nums))

size = int(input())
x_input = input().split()
x = [float(i) for i in x_input]
y_input = input().split()
y = [float(i) for i in y_input]

mean_x = mean(x)
sd_x = stddev(x)
mean_y = mean(y)
sd_y = stddev(y)

sort_x = sorted(x)
sort_y = sorted(y)

rank_x = {x[i]:sort_x.index(x[i]) + 1 for i in range(len(x))}
rank_y = {y[i]:sort_y.index(y[i]) + 1 for i in range(len(y))}
di_sq = [((rank_x[x[i]] - rank_y[y[i]]) ** 2) for i in range(size)]

numer = 6 * sum(di_sq) 
deno = size * ((size ** 2) - 1)

spearman_coeff = 1 - (numer / deno)
print(round(spearman_coeff, 3))



####################################################################

##### LEAST SQUARE REGRESSION LINE

import math as m

def stddev(array_of_nums):
    numbs = array_of_nums
    numb_mean = sum(numbs) / len(numbs)
    el_diff = [(i - numb_mean) ** 2 for i in numbs]
    numerator = sum(el_diff)
    std_dev = m.sqrt(numerator / len(numbs))
    return std_dev

def mean(array_of_nums):
    return (sum(array_of_nums) / len(array_of_nums))

def pearson(x_array, y_array):
    size = len(x_array)
    x = x_array
    y = y_array
    mean_x = mean(x)
    sd_x = stddev(x)
    mean_y = mean(y)
    sd_y = stddev(y)
    numer = 0
    for i in range(size):
        alpha = (x[i] - mean_x) * (y[i] - mean_y)
        numer += alpha
    deno = size * sd_x * sd_y
    pear_coeff = numer / deno
    return (round(pear_coeff, 3))
    
x_coord = [95, 85, 80, 70, 60]
y_coord = [85, 95, 70, 65, 70]

mean_x = mean(x_coord)
mean_y = mean(y_coord)
sd_x = stddev(x_coord)
sd_y = stddev(y_coord)
pear_coeff = pearson(x_coord, y_coord)
b = pear_coeff * (sd_y / sd_x)
a = mean_y - (b * mean_x)
ans = a + (b * 80)
print(round(ans, 3))



####################################################################

##### MULTIPLE LINEAR REGRESSION

import numpy as np

vals = input().split()
m = int(vals[0])
n = int(vals[1])
features = []
y_vals = []
i = 0
while i < n:
    a = input().split()
    charlie = [ float(a[q]) for q in range(len(a) - 1) ]
    charlie.insert(0, 1)
    features.append(charlie)
    y_vals.append(float(a[-1]))
    i += 1
i = 0
q = int(input())
test_features = []
while i < q:
    a = input().split()
    delta = [ float(p) for p in a ]
    delta.insert(0, 1)
    test_features.append(delta)
    i += 1
    
# Y = X * B
Y = (np.array(y_vals)).reshape(len(y_vals), 1)
X = np.array(features)
B1 = np.linalg.inv(np.matmul(np.transpose(X), X))
B2 = np.transpose(X)
B = np.matmul(np.matmul(B1, B2), Y)
a = B[0, 0]
b1 = B[1,0]
b2 = B[2, 0]

# y = a + b1 * x1 + b2 * x2
ans = [np.matmul(j, B) for j in test_features]
for k in ans:
    print(round(k[0],3))
