#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:13:31 2020

@author: hello
"""

############# PROJECT: TRAVELLING SALESMAN PROBLEM #############

############## NOTES ################
# Features
    # self - adaptivity
    # elitism
    
# Selection
    # k-tournament
    # topK
    
# Crossover
    # Sequential
    # Edge
    # Order
    
# Mutation
    # Scramble
    # Inverse
    # Insert
    # Swap

# Elimination
    # lambda + mu
    # lambduMu

# Final optimization (local search)
    # 2 & 3 opt (k-opt/Local Hill Climbing) - to the final converged route
    # LK Heuristic 

################### MAIN CODE #########################
 
import csv
import random as r
import math
import copy as cp
import re
import time
# import threading
# import queue
# from queue import Queue
# from multiprocessing import Queue
# from multiprocessing import Process, Queue



### Individual Mutation Rate for self-adaptivity
def routeMutateRate(singleRoute):
    return max(0.2, (0.2 + (0.02 * r.random())))

### return t-best individuals from population - elitism
def elitism(population, t):
    fitnesses = [routeLength(i) for i in population]
    sortedFitnesses = sorted(fitnesses)
    topTIndices = [fitnesses.index(i) for i in sortedFitnesses]
    sortedRoutes = [population[i] for i in topTIndices]
    tBest = sortedRoutes[:t]
    return tBest
    
### For Finding Indices of Repeating Elements in a List
def repeatIndices1(array:list, numb:int) -> list:
    ans = []
    start = 0
    while len(ans) != array.count(numb):
        ind = array.index(numb, start)
        ans.append(ind)
        start = ind + 1
    return ans

### Get Neighbouring Cities
def getSidies(route):
    a = {i:[] for i in range(0, len(route))}
    for i, j in a.items():
        if route.index(i) == 0:
            j.extend(sorted([route[1], route[-1]]))
        elif route.index(i) == len(route) - 1:
            j.extend(sorted([route[0], route[-2]]))
        else:
            j.extend(sorted([route[route.index(i) - 1], route[route.index(i) + 1]]))
    return a

### Route Generation
def route(numberOfCities):
    order = [0]
    remainOrder = list(range(1, numberOfCities))
    r.shuffle(remainOrder)
    order.extend(remainOrder)
    order.append(0)
    return order

### Length of Route (Distance)
def routeLength(singleRoute):
    length, count = 0, 0
    i, j = 0, 1
    while count != (len(singleRoute) - 1):
        distance = distMat[ singleRoute[i] ][ singleRoute[j] ]
        length += distance
        i += 1
        j += 1
        count += 1
    return length

### Distance between Two Cities
def pairwiseDist(singleRoute):
    count = 0
    i, j = 0, 1
    pairDist = []
    while count != (len(singleRoute) - 1):
        distance = distMat[ singleRoute[i] ][ singleRoute[j] ]
        pairDist.append(distance)
        i += 1
        j += 1
        count += 1
    return pairDist

### Population Generation
def population(sizeOfPopulation):
    while True:
        population = [route(noCities) for i in range(sizeOfPopulation)]
        repeats = [population.count(i) for i in population]
        boolRepeats = [True if i == 1 else False for i in repeats]
        if all(boolRepeats):
            break 
    return population

### Selection
def kTourSelect(population, k):
    samples = r.sample(population, k)
    fitnesses = [routeLength(i) for i in samples]
    mini_fit = min(fitnesses)
    selected = samples[fitnesses.index(mini_fit)]
    return selected

def kTopSelect(population, k):
    fitnesses = [routeLength(i) for i in population]
    sortedFitnesses = sorted(fitnesses)
    topKFitnesses = sortedFitnesses[:k]
    topKIndices = [fitnesses.index(i) for i in topKFitnesses]
    selectedIndex = r.sample(topKIndices, 1)
    selected = population[selectedIndex[0]]
    return selected
 
### Crossover/Recombination   
def orderCrossover(father, mother):
    r1 = father[1:-1]
    r2 = mother[1:-1]
    child = []
    cutpts = sorted(r.sample(list(range(0, len(r1))), 2))
    pt1 = cutpts[0]
    pt2 = cutpts[1]
    seg = r1[pt1:pt2 + 1]
    child.extend(seg)
    r2AfterSeg = r2[pt2 + 1:]
    r2UnusedAfter = [i for i in r2AfterSeg if i not in child]
    r2UnusedBefore = [i for i in r2[:pt2+1] if i not in child]
    r2UnusedCombo =  cp.deepcopy(r2UnusedAfter)
    r2UnusedCombo.extend(r2UnusedBefore)
    x = len(r1[:pt1])
    childAfterLen = len(r1) - (len(seg) + x)
    i = 0
    while i < childAfterLen:
            child.append(r2UnusedCombo[i])
            i += 1            
    r2UnusedComboNew = [i for i in r2UnusedCombo if i not in child]
    start = 0
    j = 0
    while j < x:
        child.insert(start, r2UnusedComboNew[j])
        j += 1
        start += 1  
    
    child.insert(0, 0)
    child.insert(len(child), 0)         
    return child

def edgeCrossover(father, mother):
    r1 = father[:-1]
    alpha = getSidies(r1)
    r2 = mother[:-1]
    beta = getSidies(r2)
    
    for i in range(0, len(r1)):
        alpha[i].extend(beta[i])
        alpha[i] = sorted(alpha[i])
        for j in alpha[i]:
            if alpha[i].count(j) > 1:
                alpha[i].insert(alpha[i].index(j), f"{j}*")
                alpha[i].remove(j)
                alpha[i].remove(j)
    ans = []
    currNode = 0
    array = cp.deepcopy(alpha)        
    while len(ans) != len(r1):
        for i in array.keys():
            array[i] = [str(p) for p in array[i]]
        ans.append(currNode)
        for i in array.values():
            combi = str(currNode) + '*'
            if (str(currNode) in i):
                i.remove(str(currNode))
            if combi in i:
                i.remove(combi)
        len1 = []
        for p in array[currNode]:
            if len(p) > 1:
                len1.append(len(array[int(p.rstrip('*'))]))
            else:
                len1.append(len(array[int(p)]))
        x = re.compile('.\*')
        y = list(filter(x.match, array[currNode]))
        
        if len(y) != 0:
           nexty = int(y[0].rstrip("*"))
           
        elif len(y) == 0 and len(len1) !=0:
            setty = set(len1)
            checky = len(setty)
            minicount = len1.count(min(len1))
            
            if checky != 1 and (minicount > 1):
                minind = repeatIndices1(len1, min(len1))
                randy = r.sample(minind, 1)
                
                if len(array[currNode][randy[0]]) > 1:
                    nexty = int((array[currNode][randy[0]]).rstrip("*")) 
                else: 
                    nexty = int(array[currNode][randy[0]])
    
            elif checky != 1 and (minicount == 1):
                if len(array[currNode][len1.index(min(len1))]) > 1:
                    nexty = int((array[currNode][len1.index(min(len1))]).rstrip("*")) 
                else: 
                    nexty = int(array[currNode][len1.index(min(len1))])
                    
            elif checky == 1:
                randy = r.sample(list(range(len(len1))), 1)
                if len(array[currNode][randy[0]]) > 1:
                    nexty = int((array[currNode][randy[0]]).rstrip("*")) 
                else: 
                    nexty = int(array[currNode][randy[0]])
            
        elif len(y) == 0 and len(len1) == 0:
            if len(array[0]) != 0 and 0 not in ans:
                nexty = 0
            else:
                remain = [i for i in range(0, len(r1)) if i not in ans]
                r.shuffle(remain)
                ans.extend(remain)
                break
                
        currNode = nexty
        
    ans.insert(len(ans), 0)
    return ans

def seqCrossover(father, mother):
    
    def legit(currF, currM):
        legitF = 0
        legitM = 0
        # father   
        if currF != max_idx:
            for i in range(currF + 1, len(f)):
                legitF = f[i]
                if i <= max_idx and legitF not in used:
                    previousF = f[currF]
                    break
                elif i == max_idx and legitF in used:
                    previousF = f[currF]
                    for i in range(1, len(f)):
                        if i not in used:
                            legitF = i
        elif currF == max_idx:
            previousF = f[-1]
            for i in range(1, len(f)):
                if i not in used:
                    legitF = i
                    break
        
        # mother
        if currM != max_idx:
            for i in range(currM + 1, len(m)):
                legitM = m[i]
                if i <= max_idx and legitM not in used:
                    previousM = m[currM]
                    break
                elif i == max_idx and legitM in used:
                    previousM = m[currM]
                    for i in range(1, len(m)):
                        if i not in used:
                            legitM = i
                            break
        elif currM == max_idx:
            previousM = m[-1]
            for i in range(1, len(m)):
                if i not in used:
                    legitM = i
                    break
    
        return legitF, legitM, previousF, previousM

    f = father[:-1]
    m = mother[:-1]
    max_idx = len(f) - 1
    used, ans = [0], [0]
    currF = 0
    currM = 0
    winner = 0
    legitF, legitM, previousF, previousM = legit(currF, currM)
    # legitF = f[1]
    # legitM = m[1]
    # previousF = f[f.index(legitF) - 1]
    # previousM = m[m.index(legitM) - 1]
    while len(ans) != len(f):
        if distMat[previousF][legitF] <= distMat[previousM][legitM]:
            winner = legitF
            p = m.index(winner)
            used.append(winner)
            ans.append(winner)
            
            currF = f.index(winner)
            currM = p
            
            legitF, legitM, previousF, previousM = legit(currF, currM) 
            
        elif distMat[previousF][legitF] > distMat[previousM][legitM]:
            winner = legitM
            p = f.index(winner)
            used.append(winner)
            ans.append(winner)
            
            currF = p
            currM = m.index(winner)
            
            legitF, legitM, previousF, previousM = legit(currF, currM) 
    child = ans
    child.insert(len(child), 0)
    return child    


### Mutation
def scrambleMutate(singleRoute, alpha):
    routeSubset = singleRoute[1:-1]
    shuffleEndPoints= r.sample(list(range(len(routeSubset))), 2)
    startPoint = min(shuffleEndPoints)
    finishPoint = max(shuffleEndPoints)
    randf = r.random()
    if startPoint == 0 and randf <= alpha:
        subset1 = routeSubset[startPoint:finishPoint + 1]
        subset2 = routeSubset[finishPoint + 1:]
        subset1.extend(subset2)
        subset1.insert(0, 0)
        subset1.insert(len(subset1), 0)
        return subset1
    elif startPoint != 0 and randf <= alpha:
        subset1 = routeSubset[:startPoint]
        shuffleSubset = routeSubset[startPoint:finishPoint + 1]
        r.shuffle(shuffleSubset)
        subset2 = routeSubset[finishPoint + 1:]
        shuffleSubset.extend(subset2)
        subset1.extend(shuffleSubset)
        subset1.insert(0, 0)
        subset1.insert(len(subset1), 0)
        return subset1
    else:
        return singleRoute

def inverseMutate(singleRoute, alpha):
    routeSubset = singleRoute[1:-1]
    shuffleEndPoints= r.sample(list(range(len(routeSubset))), 2)
    startPoint = min(shuffleEndPoints)
    finishPoint = max(shuffleEndPoints)
    randf = r.random()
    if startPoint == 0 and randf <= alpha:
        subset1 = routeSubset[startPoint:finishPoint + 1]
        subset1.reverse()
        subset2 = routeSubset[finishPoint + 1:]
        subset1.extend(subset2)
        subset1.insert(0, 0)
        subset1.insert(len(subset1), 0)
        return subset1
    elif startPoint != 0 and randf <= alpha:
        subset1 = routeSubset[:startPoint]
        middleSubset = routeSubset[startPoint:finishPoint + 1]
        middleSubset.reverse()
        subset2 = routeSubset[finishPoint + 1:]
        middleSubset.extend(subset2)
        subset1.extend(middleSubset)
        subset1.insert(0, 0)
        subset1.insert(len(subset1), 0)
        return subset1
    else:
        return singleRoute
    
def insertMutate(singleRoute, alpha):
    routeSubset = singleRoute[1:-1]
    randf = r.random()
    if randf <= alpha:
        randomNodes = r.sample(routeSubset, 2)
        twoIndices = [routeSubset.index(i) for i in randomNodes]
        routeSubset.remove(randomNodes[1])
        routeSubset.insert(twoIndices[0] + 1, randomNodes[1])
        routeSubset.insert(0, 0)
        routeSubset.insert(len(routeSubset), 0)
        return routeSubset
    else:
        return singleRoute
    
def swapMutate(singleRoute, alpha):
    routeSubset = singleRoute[1:-1]
    randf = r.random()
    if randf <= alpha:
        indicesToSwap = r.sample(list(range(len(routeSubset))), 2)
        routeSubset[indicesToSwap[0]], routeSubset[indicesToSwap[1]] = routeSubset[indicesToSwap[1]], routeSubset[indicesToSwap[0]] 
    routeSubset.insert(0, 0)
    routeSubset.insert(len(routeSubset), 0)
    return routeSubset

### ELimination
def lambdaPlusMu(poppy, offspr):
    combo = poppy.copy()
    combo.extend(offspr)
    routeLengths = [routeLength(i) for i in combo]
    sortRouteLengths = sorted(routeLengths)
    selectedRouteLengths = sortRouteLengths[:len(poppy)]
    indexes = [routeLengths.index(i) for i in selectedRouteLengths]
    new_poppy = [combo[i] for i in indexes]
    return new_poppy

def lambdaMu(offspr, lambdaCandidates):
    fitnesses = [routeLength(i) for i in offspr]
    sortedFitnesses = sorted(fitnesses)
    topLambdaFitnesses = sortedFitnesses[:lambdaCandidates]
    topLambdaIndices = [fitnesses.index(i) for i in topLambdaFitnesses]
    newPopulation = [offspr[i] for i in topLambdaIndices]
    return newPopulation

### 2-opt Local Search Optimization
def twoOpt(route, i, j):
    optRoute = []
    r1 = route[0:i]
    r2 = route[i:j + 1]
    r2.reverse()
    r3 = route[j + 1:]
    
    optRoute.extend(r1)
    optRoute.extend(r2)
    optRoute.extend(r3)
    return optRoute

def twoOptAlgo(convRoute, convRouteDist, runTime):
    initialRoute = cp.deepcopy(convRoute)
    initialRouteDistance = convRouteDist
    initialRouteSubset = initialRoute[1:-1]
    optiRoute = 0
    optiRouteDist = 0
    counter = 0
    # 1 = Time Over, 2 = All Combinations Exhausted
    stopReason = 1  
    # Time Control
    time2Run = runTime
    # startTime = time.time()
    # totalRunTime = time.time() - startTime
    while True:
        for i in range(len(initialRouteSubset)):
            startTime = time.time()
            if time.time() - startTime > time2Run:
                    break
            else:
                for j in range(len(initialRouteSubset)):
                    startTime = time.time()
                    if time.time() - startTime > time2Run:
                        break
                    else:
                        newRoute = twoOpt(initialRouteSubset, i, j)
                        newRoute.insert(len(newRoute), 0)
                        newRoute.insert(0, 0)
                        newRouteDist = routeLength(newRoute)
                        if newRouteDist < initialRouteDistance:
                            optiRoute = newRoute
                            optiRouteDist = newRouteDist
                            initialRouteDistance = optiRouteDist
                        counter += 1
                        # append all
                        # optiRoute.append(newRoute)
                        # optiRouteDist.append(newRouteDist)   
                 
        if counter == len(initialRouteSubset) ** 2:
            stopReason = 2
            break     
          
    if optiRouteDist == 0 or optiRoute == 0:
        optiRoute = convRoute
        optiRouteDist = convRouteDist
    
    # qResults.put(optiRoute)
    # qResults.put(optiRouteDist)
    # qResults.put(stopReason)
    # return qResults
    
    return optiRoute, optiRouteDist, stopReason

def avg(array):
    return (sum(array) / len(array))

#################### MAIN GENETIC ALGORITHM #########################
beginTime = time.time()
distMat = []
csvFileNames = ["tour29.csv", "tour100.csv", "tour194.csv", "tour929.csv"]
csvFileName = csvFileNames[3]
with open(csvFileName) as csvfile:
    data = csv.reader(csvfile)
    for i in data:
        distMat.append(i)     
# distMat = [[float(j) for j in i] for i in distMat]
distMat = [[float(j) if float(j) != math.inf else float(10000000) for j in i] for i in distMat]
noCities = len(distMat[0])

eliteRoutes = 10
children = 60 - eliteRoutes
sizeOfPopulation = 60
k = 3
alpha = 0.5
beta = 1
selfAdapt = 1
iters = 1
optiRunTime = 20
noHistoryIters = 10
tolerance = 0.000001

poppy = population(sizeOfPopulation)
poppyLengths = [routeLength(i) for i in poppy]
poppyMutateRates = [routeMutateRate(i) for i in poppy]

if eliteRoutes == 0:
    offspr = []
else:
    eliteCandidates = elitism(poppy, eliteRoutes)
    offspr = cp.deepcopy(eliteCandidates)
    
iterCount = 0
print(f"0. Mean Fitness: {round(sum(poppyLengths) / len(poppyLengths), 5)} | Best Fitness: {round(min(poppyLengths), 5)}")

for i in range(iters):
    for j in range(children):
        
        # Selection - k tournament
        papa = kTourSelect(poppy, k)
        mama = kTourSelect(poppy, k)
          
        # Recombination/CrossOver
        randf = r.random()
        if randf <= beta:            
            baby = seqCrossover(papa, mama)
            family = [papa, mama, baby]
            familyFitness = [routeLength(i) for i in family]
                        
            if familyFitness[2] < min(familyFitness[0], familyFitness[1]):
                newParent = baby
                oldParent = family[familyFitness.index(max(familyFitness[:2]))]
                baby1 = seqCrossover(oldParent, newParent)
                baby = baby1
                
            # order
            # baby1 = orderCrossover(papa, mama)
            # baby2 = orderCrossover(mama, papa)
            
        else:
            fitnesses = [routeLength(i) for i in poppy]
            bestFitness = min(fitnesses)
            baby = poppy[fitnesses.index(bestFitness)]
            
            # papaFitness = routeLength(papa)
            # mamaFitness = routeLength(mama)
            # if papaFitness <= mamaFitness:
            #     baby = papa
            # else:
            #     baby = mama
        
        if selfAdapt == 0:
            mutBaby = inverseMutate(baby, alpha)
            # mutBaby, nr1, nr2 = twoOptAlgo(mutBaby, routeLength(mutBaby), 3)
            offspr.append(mutBaby)  
            # order
            # mutBaby1 = inverseMutate(baby1, alpha)
            # mutBaby2 = inverseMutate(baby2, alpha)
            # offspr.append(mutBaby1)
            # offspr.append(mutBaby2)

        elif selfAdapt == 1:
            papaMutateRate = poppyMutateRates[poppy.index(papa)]
            mamaMutateRate = poppyMutateRates[poppy.index(mama)]
            y = 2 * (r.random()) - 0.5
            babyMutateRate = papaMutateRate + (y * abs((mamaMutateRate - papaMutateRate)))
            mutBaby = inverseMutate(baby, babyMutateRate)
            # mutBaby, nr1, nr2 = twoOptAlgo(mutBaby, routeLength(mutBaby), 3)
            offspr.append(mutBaby)  
            # order
            # mutBaby1 = inverseMutate(baby1, alpha)
            # mutBaby2 = inverseMutate(baby2, alpha)
            # offspr.append(mutBaby1)
            # offspr.append(mutBaby2)
            
    if selfAdapt == 0:
        mutPoppy = [inverseMutate(i, alpha) for i in poppy]
        poppy = lambdaPlusMu(poppy, offspr)
        # poppy = lambdaMu(offspr, sizeOfPopulation)
    elif selfAdapt == 1:
        mutPoppy = [inverseMutate(i, babyMutateRate) for i in poppy]
        poppy = lambdaPlusMu(poppy, offspr)
        # poppy = lambdaMu(offspr, sizeOfPopulation)
    
    
    newPoppyLengths = [routeLength(i) for i in poppy]
    meanRouteLength = round(sum(newPoppyLengths) / len(newPoppyLengths), 5)
    minRouteLength = round(min(newPoppyLengths), 5)
    bestRoute = poppy[newPoppyLengths.index(min(newPoppyLengths))]
    bestRouteLength = routeLength(bestRoute)
    # print(f"MF: {meanRouteLength} | BF: {minRouteLength} | R: {bestRouteLength}")
    # print(f"MF: {meanRouteLength} | BF: {minRouteLength} | BRL: {bestRouteLength}")
    print(f"{i + 1}. Mean Fitness: {meanRouteLength} | Best Fitness: {minRouteLength}")
    # print(f"{i + 1}. MF: {meanRouteLength} | BF: {minRouteLength} | BRL: {bestRouteLength}")
    
    # Mutation Rate Change
    # if i >= 25:
    #     alpha = 0.3
    # if i >= 50:
    #     alpha = 0.1
    
    # if i >= 1:
    #     alpha = 0.5 - (0.3 * (i / iters))
    
    # Without self adaptivity
    if selfAdapt == 0:
        if (csvFileName in csvFileNames[2:]) and (i >= 1):
            alpha = 0.8 / (tolerance + ((minRouteLength - meanRouteLength)))
        elif i >= 1:
            alpha = 0.5 - (0.3 * (i / iters))
    
    # stopping criteria
    historyMeanRoute = []
    historyBestRoute = []
    historyMeanRoute.append(meanRouteLength)
    historyBestRoute.append(bestRouteLength)
    if len(historyMeanRoute) and len(historyBestRoute) >= 20:
        historyMeanRoute = []
        historyBestRoute = []
    if abs(avg(historyBestRoute[-1 * (noHistoryIters):]) - avg(historyMeanRoute[-1 * (noHistoryIters):])) <= tolerance:
        break
        
### Local Search Operator: 2-opt
print("\n---------------------------------------------------------------\n")
print(f"Running 2-opt Local Search for {optiRunTime} seconds...\n")
optiRoute, optiRouteDist, stopReason = twoOptAlgo(bestRoute, bestRouteLength, optiRunTime)

#######

# qResults = Queue()
# # newThread = threading.Thread(target=twoOptAlgo, args=(bestRoute, bestRouteLength), daemon=True)
# newProcess = Process(target=twoOptAlgo, args=(bestRoute, bestRouteLength, qResults), daemon=True)
# newProcess.start()
# # newThread.join(float(optiRunTime))
# newProcess.join(optiRunTime)
# print(newProcess.is_alive())
# # newProcess.close()
# time.sleep(optiRunTime)
# # qResults.join()
# optiRoute = qResults.get()
# optiRouteDist = qResults.get()
# stopReason  = qResults.get()

#######


if stopReason == 1:
    print("Runtime Over\n")
    if optiRouteDist == bestRouteLength:
        optiRouteDist = 'More Optimized Distance/Route not found\n'
    else:
        optiRouteDist = round(optiRouteDist, 5)
elif stopReason == 2:
    print("All 2-opt Combinations Exhausted before Time Limit\n")
    if optiRouteDist == bestRouteLength:
        optiRouteDist = 'More Optimized Distance/Route not found\n'
    else:
        optiRouteDist = round(optiRouteDist, 5)
bestRouteLength = round(bestRouteLength, 5)
print("---------------------------------------------------------------\n")
print(f"* Best Route Length after Genetic Algorithm: {bestRouteLength}\n")
print(f"* Optimized Route Length after 2-Opt: {optiRouteDist}\n")
# print(f"* Optimized Route: {optiRoute}\n")
finishTime = time.time()
print((f"* Total Time Taken: {round(((finishTime - beginTime)/60), 3)} minutes\n"))
# print(f"Best Route: {bestRoute} | Best Route Length: {bestRouteLength}")
# print(f"Optimized Route: {c1} | Optimized Route Length: {optiRoute}")




#### Testing ######
# bapu = select(poppy, 5)
# maa = select(poppy, 5)
# bacha = seqCrossover(bapu, maa)
# print(bacha)
# print(f)
# print(m)
# cand = route(noCities)
# mcand1 = scrambleMutate(cand, alpha)
# mcand = inverseMutate(cand, alpha)
# print(cand)
# print(mcand)
