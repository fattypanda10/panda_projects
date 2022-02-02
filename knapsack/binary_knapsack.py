##### Binary Knapsack Problem Using Genetic Algorithm #####
##### With two options - fixed mutation rate and variable mutation rate. The relevant part can be uncommented #####
##### Result of each iteration could consist of different variables. Uncomment accordingly #####

############################################################################################################

import random as r
import math

# Generate a single candidate solution
def individual(size):
    selection_order = list(range(size))
    r.shuffle(selection_order)
    return selection_order

# Generate mutation rate for each candidate solution
def mut_rate(single_order):
    return max(0.01, (0.1 + (0.02 * r.random())))
    
# Generation of Population of Individuals/Candidate Solution
def population(size, pop_size):
    pop = [individual(size) for i in range(pop_size)]
    return pop

# Determining the fitness of each individual/candidate solution
def fitness(single_order):
    sack_value = 0
    remaining_capacity = capacity
    for i in single_order:
        if weights[i] <= remaining_capacity:
            sack_value += values[i]
            remaining_capacity -= weights[i]
    return sack_value

# Determining the items in the Knapsack
def kp_items(single_order):
    in_kp = []
    remaining_capacity = capacity
    for i in single_order:
        if weights[i] <= remaining_capacity:
            in_kp.append(i)
            remaining_capacity -= weights[i]
    return in_kp
    
# Selection {k-tournament selection}
def select(population, k):
    samples = r.sample(population, k)
    fitnesses = [fitness(i) for i in samples]
    maxy_fit = max(fitnesses)
    selected = samples[fitnesses.index(maxy_fit)]
    return selected
    
# Crossover or Recombination
def crossover(father, mother, papa_mutrate, mama_mutrate, beta):
    fkp = kp_items(father)
    mkp = kp_items(mother)
    fset1 = set(fkp)
    mset1 = set(mkp)
    cset = fset1.intersection(mset1)
    sym_diff = fset1.symmetric_difference(mset1)
    randf = r.random()
    for i in sym_diff:
        if randf < beta:
            cset.add(i)
    child = list(cset)
    r.shuffle(child)
    fset2 = set(father)
    mset2 = set(mother)
    remain = list((fset2.union(mset2)).difference(cset))
    r.shuffle(remain)
    child.extend(remain)
    y = 2 * r.random() - 0.5
    x = papa_mutrate + (y * (mama_mutrate - papa_mutrate))
    return [child, x]
    
# Mutation
def mutate(single_order, alpha):
    mut_copy = single_order.copy()
    randf = r.random()
    if randf <= alpha:
        indices_to_swap = r.sample(list(range(len(mut_copy))), 2)
        mut_copy[indices_to_swap[0]], mut_copy[indices_to_swap[1]] = mut_copy[indices_to_swap[1]], mut_copy[indices_to_swap[0]] 
    return mut_copy

# Elimination and (consequently) generation of new population
def eliminate(poppy, offspr):
    combo = poppy.copy()
    combo.extend(offspr)
    fitty = [fitness(i) for i in combo]
    sort_fitty = sorted(fitty, reverse=True)
    fit_select = sort_fitty[:len(poppy)]
    indexes = [fitty.index(i) for i in fit_select]
    new_poppy = [combo[i] for i in indexes]
    return new_poppy
    

##### Main - Parameters to control #####
##### {candidate solution size, population size, offspring/children size, k-tournament selection, alpha: mutation rate (constant), beta: crossover rate, iterations} #####
size = 200
pop_size = 500
children = 500
k = 125
# alpha = 0.05 
beta = 0.5 
iters = 500 

values = [math.pow(2, r.gauss(0, 1)) for i in range(size)]
weights = [math.pow(2, r.gauss(0, 1)) for i in range(size)]
capacity = 0.25 * sum(weights)

poppy = population(size, pop_size)
poppy_mutrates = [mut_rate(i) for i in poppy]
offspr = []
fits = [fitness(i) for i in poppy]

print(f"Mean Fitness: {round(sum(fits) / len(fits), 5)} | Best Fitness: {round(max(fits), 5)}")

for i in range(iters):
    for j in range(children):
        papa = select(poppy, size)
        papa_mutrate = poppy_mutrates[poppy.index(papa)]
        mama = select(poppy, size)
        mama_mutrate = poppy_mutrates[poppy.index(mama)]
        baby, baby_mutrate = crossover(papa, mama, papa_mutrate, mama_mutrate, beta)
        # mut_baby = mutate(baby, alpha)
        mut_baby = mutate(baby, baby_mutrate)
        offspr.append(mut_baby)

    
    # mut_poppy = [mutate(i, alpha) for i in poppy]
    mut_poppy = [mutate(poppy[i], poppy_mutrates[i]) for i in range(len(poppy))]
    poppy = eliminate(mut_poppy, offspr)
    
    fits_new = [fitness(i) for i in poppy]
    mean_fits = round(sum(fits_new) / len(fits_new), 5)
    maxo_fit = round(max(fits_new), 5)
    best_sample = poppy[fits_new.index(max(fits_new))]
    best_sample_kp = kp_items(best_sample)
    # print(f"MF: {mean_fits} | BF: {maxo_fit} | S: {best_sample} | KP: {best_sample_kp}")
    print(f"Mean Fitness: {mean_fits} | Best Fitness: {maxo_fit}")