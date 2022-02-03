############# PROJECT: TRAVELLING SALESMAN PROBLEM ####################

################### KEY POINTS ########################################

# Implemented in Genetic Algorithm [GA]

# Selection (3)
    # k-tournament
    # Top-k
    # Roulette wheel
    # Sigma Scale
    
# Crossover (3)
    # Order
    # Edge
    # Sequential
    
# Mutation (4)
    # Scramble
    # Inverse
    # Insert
    # Swap

# Elimination (2)
    # lambda + mu
    # lambdu - Mu

# Stopping Criteria (2)
    # Based on the difference between mean of best fitness and mean fitness
    # of a number of iterations (user-input) for a user-defined tolerance
    # Also when the mean fitness becomes equal to best fitness

# Final optimization (local search) [LSO]
    # 2-Opt (multiple) on the best solution (converged) obtained afer using GA
    
# Methods employed to improve solution
    # self - adaptivity
    # elitism
    # variable mutation rate (as a function of the generation)
    # Advance Crossover (Based on research papers, if the baby has better fitness 
    # than the  worst of the parents then it is chosen as the parent
    # and used for crossover)

# Plots
    # Convergence (Mean Fitness), Best Fitness & Optimization Plots Vs Iterations
    # Convergence (Mean Fitness), Best Fitness & Optimization Plots Vs Time Taken
    
# Extensive and detailed experiments were also undertaken to understand, refine 
# and optimize the solution. They have been briefly mentioned below. For further
# details, please refer to the report.
    
    # Using LSO at several positions within the GA (on baby, on parents, on population etc.)
    # Using constant, increasing and decreasing mutation rates (with each generation)
    # Using recombination/crossover rate
    # For order crossover, another variant which produced two offsprings was also tried
    # All the parameters for the above operators were tuned and controlled intensively

# ^^^ The Report would describe everything in detail ^^^

################### MAIN CODE #########################################

import Reporter

######### REQUIRED MODULES ##################

import random as r
import math
import copy as cp
import re
import time
import numpy as np
import matplotlib.pyplot as plt

######### FUNCTIONS FOR GENETIC ALGORITHM #########

### CALCULATE AVERAGE OF A LIST/ARRAY
def avg(array):
    return (sum(array) / len(array))


### SELF-ADAPTIVITY - MUTATION RATE FOR EACH CANDIDATE
def routeMutateRate(singleRoute):
    return max(0.3, (0.3 + (0.09 * r.random())))


### ELITISM - RETURN t-BEST INDIVIDUALS FROM THE POPULATION
def elitism(population, t):
    fitnesses = [routeLength(i) for i in population]
    sortedFitnesses = sorted(fitnesses)
    topTIndices = [fitnesses.index(i) for i in sortedFitnesses]
    sortedRoutes = [population[i] for i in topTIndices]
    tBest = sortedRoutes[:t]
    return tBest
  
  
### FOR FINDING INDICES OF REPEATING ELEMENTS IN A LIST
def repeatIndices1(array:list, numb:int) -> list:
    ans = []
    start = 0
    while len(ans) != array.count(numb):
        ind = array.index(numb, start)
        ans.append(ind)
        start = ind + 1
    return ans


### GET NEIGHBOURING CITIES
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


### ROUTE GENERATION
def route(numberOfCities):
    order = [0]
    remainOrder = list(range(1, numberOfCities))
    r.shuffle(remainOrder)
    order.extend(remainOrder)
    order.append(0)
    return order


### LENGTH OF ROUTE (TOTAL DISTANCE)
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


### DISTANCE BETWEEN CITIES
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


### POPULATION GENERATION
def population(sizeOfPopulation):
    while True:
        population = [route(noCities) for i in range(sizeOfPopulation)]
        repeats = [population.count(i) for i in population]
        boolRepeats = [True if i == 1 else False for i in repeats]
        if all(boolRepeats):
            break 
    return population


############ SELECTION #####################

# K-TOURNAMENT
def kTourSelect(population, k):
    samples = r.sample(population, k)
    fitnesses = [routeLength(i) for i in samples]
    mini_fit = min(fitnesses)
    selected = samples[fitnesses.index(mini_fit)]
    return selected

# TOP-K
def kTopSelect(population, k):
    fitnesses = [routeLength(i) for i in population]
    sortedFitnesses = sorted(fitnesses)
    topKFitnesses = sortedFitnesses[:k]
    topKIndices = [fitnesses.index(i) for i in topKFitnesses]
    selectedIndex = r.sample(topKIndices, 1)
    selected = population[selectedIndex[0]]
    return selected

# ROULETTE WHEEL
def rouletteSelect(population):
    fits = np.array([(1 / routeLength(i)) for i in population])
    sumFits = np.sum(fits)
    fitsProb = np.array([((1 / routeLength(i)) / sumFits) for i in population])
    fitsProbNorm = np.array([i / np.sum(fitsProb) for i in fitsProb])
    indicesSelected = np.random.choice(list(range(len(population))), 1, False, fitsProbNorm)
    selected = population[indicesSelected[0]]
    return selected

# SIGMA SCALE
def sigmaScaleSelect(population):
    fitnesses = np.array([routeLength(i) for i in population])
    meanFits = np.mean(fitnesses)
    stdFits = np.std(fitnesses)
    zScoreFits = np.array([((i - meanFits) / (stdFits)) for i in fitnesses])
    threshold = -3
    zScoreThreshold = np.array([(i - threshold) for i in zScoreFits])
    fitsProb = np.array([zScoreThreshold[i] / np.sum(zScoreThreshold) if zScoreFits[i] > threshold else 0 for i in range(len(zScoreFits))])
    fitsProbNorm = np.array([i / np.sum(fitsProb) for i in fitsProb])
    indicesSelected = np.random.choice(list(range(len(population))), 1, False, fitsProbNorm)
    selected = population[indicesSelected[0]]
    return selected
    

############ CROSSOVER/RECOMBINATION ##################

# ORDER
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

# EDGE
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

# SEQUENTIAL
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


############### MUTATION ##############################

# SCRAMBLE
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

# INVERSE
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

# INSERT  
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

# SWAP   
def swapMutate(singleRoute, alpha):
    routeSubset = singleRoute[1:-1]
    randf = r.random()
    if randf <= alpha:
        indicesToSwap = r.sample(list(range(len(routeSubset))), 2)
        routeSubset[indicesToSwap[0]], routeSubset[indicesToSwap[1]] = routeSubset[indicesToSwap[1]], routeSubset[indicesToSwap[0]] 
    routeSubset.insert(0, 0)
    routeSubset.insert(len(routeSubset), 0)
    return routeSubset

############### ELIMINATION ###########################

# LAMBDA + MU
def lambdaPlusMu(poppy, offspr):
    combo = poppy.copy()
    combo.extend(offspr)
    routeLengths = [routeLength(i) for i in combo]
    sortRouteLengths = sorted(routeLengths)
    selectedRouteLengths = sortRouteLengths[:len(poppy)]
    indexes = [routeLengths.index(i) for i in selectedRouteLengths]
    new_poppy = [combo[i] for i in indexes]
    return new_poppy

# LAMBDA - MU
def lambdaMu(offspr, lambdaCandidates):
    fitnesses = [routeLength(i) for i in offspr]
    sortedFitnesses = sorted(fitnesses)
    topLambdaFitnesses = sortedFitnesses[:lambdaCandidates]
    topLambdaIndices = [fitnesses.index(i) for i in topLambdaFitnesses]
    newPopulation = [offspr[i] for i in topLambdaIndices]
    return newPopulation


############ OPTIMIZATION: 2-OPT LOCAL SEARCH OPERATOR ############

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
    # Stop Reason: 1 = Time Over, 2 = All Combinations Exhausted
    stopReason = 1  
    time2Run = runTime
    while True:
        startTime = time.time()
        for i in range(len(initialRouteSubset)):
            if time.time() - startTime > time2Run:
                    break
            else:
                for j in range(len(initialRouteSubset)):
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
                
        if counter == len(initialRouteSubset) ** 2:
            stopReason = 2
            break   
        
        break
    
    if optiRouteDist == 0 or optiRoute == 0:
        optiRoute = convRoute
        optiRouteDist = convRouteDist
        
    return optiRoute, optiRouteDist, stopReason

#############################################################################

# Modify the class name to match your student number.
class r0846712:
                
    def __init__(self):
        self.reporter = Reporter.Reporter(self.__class__.__name__)

    # The evolutionary algorithm's main loop
    def optimize(self, filename):
        
        # Read distance matrix from file.        
        file = open(filename)
        distanceMatrix = np.loadtxt(file, delimiter=",")
        file.close()
    
        # Your code here.
        global distMat, noCities
        filenames = ["tour29.csv", "tour100.csv", "tour194.csv", "tour929.csv"]
        distMat = distanceMatrix.tolist()
        distMat = [[float(j) if float(j) != math.inf else float(10000) for j in i] for i in distMat]
        noCities = len(distMat[0])
        
        ################# SETTINGS FOR GENETIC ALGORITHM ####################
        
        ### PREDETERMINED VALUES FOR GIVEN TOURS
        # ORDER OF VALUES IN THE "tourValues" BELOW:
            # 1. selection 
            # 2. crossOver
            # 3. mutation
            # 4. elimination
            # 5. advance CrossOver
            # 6. elitism
            # 7. self-adaptivity
            # 8. population size
            # 9. children size
            # 10. number of iterations
            # 11. number of two-opt LSO
        
        tourValues = {'./tour29.csv':  [1, 3, 3, 2, 0, 0, 0, 250, 250, 50, 75],
                      './tour100.csv': [4, 3, 3, 2, 0, 0, 0, 175, 175, 50, 75],
                      './tour194.csv': [4, 3, 2, 2, 1, 0, 1, 75, 75, 50, 75],
                      './tour929.csv': [4, 3, 2, 2, 0, 0, 0, 35, 35, 35, 20] 
                      }
                
           
        # ENABLE/DISABLE DIFFERENT TYPES OF OPERATORS
        
        # Selection Operator [k Tournament: 1, top-k: 2, roulette: 3, sigma Scale: 4]
        selectionOp = tourValues[filename][0]
        
        # Crossover Operator [Order: 1, Edge: 2, Sequential: 3]
        crossOverOp = tourValues[filename][1]
        
        # Mutation Operator [Scramble: 1, Inverse: 2, Insert: 3, Swap: 4]
        mutationOp = tourValues[filename][2]
        
        # Elimination Operator [lambdaPlusMu: 1, lambdaMu: 2]
        eliminationOp = tourValues[filename][3]
        
        # Features [Enable: 1, Disable: 0]
        # Advance CrossOver Scheme
        advanceCrossoverOp = tourValues[filename][4]
        
        # Elitism
        eliteRoutes = tourValues[filename][5]
        
        # Self-Adaptivity
        selfAdapt = tourValues[filename][6]
        
        # Genetic Algorithm Parameters
        sizeOfPopulation = tourValues[filename][7]
        children = tourValues[filename][8] - eliteRoutes
        
        # Number of Iterations & Two-Opt LSO
        iters = tourValues[filename][9]
        numberOfTwoOpt = tourValues[filename][10]
        
        # Constant (optimized) Parameters for all Tours
        k = 3
        alpha = 0.5
        beta = 1
        # iters = 50
        optiRunTime = 3
        # numberOfTwoOpt = 75
        noHistoryIters = 5
        tolerance = 1e-5
        
        #################### GENETIC ALGORITHM STARTS #######################
        
        mainBeginTime = time.time()
        poppy = population(sizeOfPopulation)
        poppyLengths = [routeLength(i) for i in poppy]
        
        if selfAdapt == 1:
            poppyMutateRates = [routeMutateRate(i) for i in poppy]
        
        startMeanFitness = sum(poppyLengths) / len(poppyLengths)
        startBestFitness = min(poppyLengths)
        
        ### FOR STORING RESULTS OF MEAN AND BEST FITNESS FOR EVERY GENERATION
        historyMeanRoute = [round(startMeanFitness, 5)]
        historyBestRoute = [round(startBestFitness, 5)]
        
        if eliteRoutes == 0:
            offspr = []
        else:
            eliteCandidates = elitism(poppy, eliteRoutes)
            offspr = cp.deepcopy(eliteCandidates)
            
        print(f"0. Mean Fitness: {round(startMeanFitness, 5)} | Best Fitness: {round(startBestFitness, 5)}")
        
        iterStartTime = time.time()
        while True:
            
            ### MAIN LOOP 
            for i in range(iters):
                for j in range(children):
                    
                    ### SELECTION
                    if selectionOp == 1:
                        papa = kTourSelect(poppy, k)
                        mama = kTourSelect(poppy, k)
                    elif selectionOp == 2:
                        papa = kTopSelect(poppy, k)
                        mama = kTopSelect(poppy, k)
                    elif selectionOp == 3:
                        papa = rouletteSelect(poppy)
                        mama = rouletteSelect(poppy)
                    elif selectionOp == 4:
                        papa = sigmaScaleSelect(poppy)
                        mama = sigmaScaleSelect(poppy)
                        
                    ### CROSSOVER/RECOMBINATION
                    if advanceCrossoverOp == 1:
                        randf = r.random()
                        if randf <= beta:
                            if crossOverOp == 1:
                                baby = orderCrossover(papa, mama)
                                
                            elif crossOverOp == 2:
                                baby = edgeCrossover(papa, mama)
                                
                            elif crossOverOp == 3:
                                baby = seqCrossover(papa, mama)
                              
                            family = [papa, mama, baby]
                            familyFitness = [routeLength(i) for i in family]
                            if familyFitness[2] < min(familyFitness[0], familyFitness[1]):
                                newParent = baby
                                oldParent = family[familyFitness.index(max(familyFitness[:2]))]
                                baby1 = seqCrossover(oldParent, newParent)
                                baby = baby1
                        else:
                            fitnesses = [routeLength(i) for i in poppy]
                            bestFitness = min(fitnesses)
                            baby = poppy[fitnesses.index(bestFitness)]
            
                    elif advanceCrossoverOp == 0:
                        if crossOverOp == 1:
                            baby = orderCrossover(papa, mama)
                            
                        elif crossOverOp == 2:
                            baby = edgeCrossover(papa, mama)
                            
                        elif crossOverOp == 3:
                            baby = seqCrossover(papa, mama)
                          
                    ### MUTATION
                    if selfAdapt == 0:
                        if mutationOp == 1:
                            mutBaby = scrambleMutate(baby, alpha)
                            
                        elif mutationOp == 2:
                            mutBaby = inverseMutate(baby, alpha)
                            
                        elif mutationOp == 3:
                            mutBaby = insertMutate(baby, alpha)
                            
                        elif mutationOp == 4:
                            mutBaby = swapMutate(baby, alpha)    
                        
                        offspr.append(mutBaby)  
                        
                    elif selfAdapt == 1:
                        papaMutateRate = poppyMutateRates[poppy.index(papa)]
                        mamaMutateRate = poppyMutateRates[poppy.index(mama)]
                        y = 2 * (r.random()) - 0.5
                        babyMutateRate = papaMutateRate + (y * abs((mamaMutateRate - papaMutateRate)))
                        if mutationOp == 1:
                            mutBaby = scrambleMutate(baby, babyMutateRate)
                            
                        elif mutationOp == 2:
                            mutBaby = inverseMutate(baby, babyMutateRate)
                            
                        elif mutationOp == 3:
                            mutBaby = insertMutate(baby, babyMutateRate)
                            
                        elif mutationOp == 4:
                            mutBaby = swapMutate(baby, babyMutateRate)
                        
                        offspr.append(mutBaby)
                               
                ### ELIMINATION
                if selfAdapt == 0:
                    if eliminationOp == 1:
                        poppy = lambdaPlusMu(poppy, offspr)
                        if mutationOp == 1:
                            mutPoppy = [scrambleMutate(i, alpha) for i in poppy]
                            
                        elif mutationOp == 2:
                            mutPoppy = [inverseMutate(i, alpha) for i in poppy]
                            
                        elif mutationOp == 3:
                            mutPoppy = [insertMutate(i, alpha) for i in poppy]
                            
                        elif mutationOp == 4:
                            mutPoppy = [swapMutate(i, alpha) for i in poppy]
                        poppy = mutPoppy
                        
                    elif eliminationOp == 2:
                        poppy = lambdaMu(offspr, sizeOfPopulation)
                        
                elif selfAdapt == 1:
                    if eliminationOp == 1:
                        poppy = lambdaPlusMu(poppy, offspr)
                        
                    elif eliminationOp == 2:
                        poppy = lambdaMu(offspr, sizeOfPopulation)
                    
                ### CALCULATION OF MEAN AND BEST FITNESS
                newPoppyLengths = [routeLength(i) for i in poppy]
                meanRouteLength = round(sum(newPoppyLengths) / len(newPoppyLengths), 5)
                minRouteLength = round(min(newPoppyLengths), 5)
                bestRoute = poppy[newPoppyLengths.index(min(newPoppyLengths))]
                bestRouteLength = routeLength(bestRoute)
                print(f"{i + 1}. Mean Fitness: {meanRouteLength} | Best Fitness: {minRouteLength}")
                
                ### WITHOUT SELF-ADAPTIVITY
                if selfAdapt == 0:
                    if (filename in filenames[2:]) and (i >= 1):
                        alpha = 0.8 / (tolerance + ((minRouteLength - meanRouteLength)))
                    elif i >= 1:
                        alpha = 0.5 - (0.3 * (i / iters))
            
                ### STOPPING CRITERIA
                historyMeanRoute.append(meanRouteLength)
                historyBestRoute.append(bestRouteLength)
                stopCondi = abs(avg(historyBestRoute[-1 * (noHistoryIters):]) - avg(historyMeanRoute[-1 * (noHistoryIters):])) <= tolerance
                if (stopCondi) or (meanRouteLength == minRouteLength):
                    break

        
            ###### LOCAL SEARCH OPTIMIZATION - 2-OPT ########
            historyOptiDist = [bestRouteLength]
            optimizedRoute = cp.deepcopy(bestRoute)
            optimizedRouteLength = cp.deepcopy(bestRouteLength)
            print("\n-------------------------------------------------------------\n")
            print(f"Running 2-opt Local Search for a maximum of {optiRunTime * numberOfTwoOpt} seconds...")
            print("\n-------------------------------------------------------------\n")
            
            optiStartTime = time.time()
            for j in range(numberOfTwoOpt):
                optiRoute, optiRouteDist, stopReason = twoOptAlgo(optimizedRoute, optimizedRouteLength, optiRunTime)
                optimizedRoute = optiRoute
                optimizedRouteLength = optiRouteDist
                historyOptiDist.append(optiRouteDist)
            
            iterFinishTime = time.time() 
            
            if stopReason == 1:
                print(f"---Runtime of {optiRunTime} seconds per 2-Opt optimization insufficient to cycle through all combinations!---\n")
                if math.isclose(optimizedRouteLength, bestRouteLength):
                    print('^^^ More Optimized Distance/Route NOT Found ^^^\n')
                else:
                    print('^ More Optimized Distance/Route Found ^\n')
                   
            elif stopReason == 2:
                print(f"* All 2-opt Combinations Exhausted before Time Limit of {optiRunTime * numberOfTwoOpt} seconds! *\n")
                if math.isclose(optimizedRouteLength, bestRouteLength):
                    print('^^^ More Optimized Distance/Route NOT Found ^^^\n')
                else:
                    print('^^^ More Optimized Distance/Route Found ^^^ \n')
                
            
            # FINAL RESULTS
            bestRouteLength = round(bestRouteLength, 5)
            optimizedRouteLength = round(optimizedRouteLength, 5)
            print("-------------------------------------------------------------\n")
            print("Final Results: \n")
            print(f"* Best Route Length after Genetic Algorithm --> {bestRouteLength}\n")
            print(f"* Optimized Route Length after 2-Opt Optimization --> {optimizedRouteLength}\n")
            print(f"* Optimized Route --> {optimizedRoute}\n")
            
            
            ### PLOTTING  
            
            # 1 - AGAINST NUMBER OF ITERATIONS
            # MEAN FITNESS
            fig1, ax1 = plt.subplots()
            plt.style.use('dark_background')
            ax1.set_xlabel("Iterations")
            ax1.set_ylabel("Mean Fitness")
            ax1.set_title("Variation of Mean Fitness")
            ax1.plot(range(len(historyMeanRoute)), historyMeanRoute, '--b', linewidth = 3, label="Mean Fitness")
            ax1.legend()
            
            # BEST FITNESS
            fig2, ax2 = plt.subplots()
            plt.style.use('dark_background')
            ax2.set_xlabel("Iterations")
            ax2.set_ylabel("Best Fitness")
            ax2.set_title("Variation of Best Fitness")
            ax2.plot(range(len(historyBestRoute)), historyBestRoute, '--r', linewidth = 3, label="Best Fitness")
            ax2.legend()
            
            # OPTIMIZATION FITNESS
            fig3, ax3 = plt.subplots()
            plt.style.use('dark_background')
            ax3.set_xlabel("Iterations")
            ax3.set_ylabel("Optimized Fitness")
            ax3.set_title("Variation of Best Fitness due to 2-Opt Optimization")
            ax3.plot(range(len(historyOptiDist)), historyOptiDist, '--y', linewidth = 3, label="Optimized Fitness")
            ax3.plot(numberOfTwoOpt, historyOptiDist[-1], "om", label='Most Optimized Point')
            ax3.annotate(f"{round(historyOptiDist[-1], 5)}", 
                          (numberOfTwoOpt, historyOptiDist[-1]), 
                          textcoords='offset points', 
                          xytext=(0, 50),
                          arrowprops=dict(facecolor='green',
                                          connectionstyle='angle3',
                                          arrowstyle='simple',                          
                                          ),
                          ha='center',
                          va='top'
                        )
            ax3.legend()
            
            # COMBINED - MEAN FITNESS, BEST FITNESS, OPTIMIZATION & MOST OPTIMIZED POINT
            fig4, ax4 = plt.subplots()
            plt.style.use('dark_background')
            ax4.set_xlabel("Iterations")
            ax4.set_ylabel("Mean Fitness | Best Fitness | Optimized Point")
            ax4.set_title("Variation of Mean Fitness, Best Fitness, Optimization & Most Optimized Point ")
            ax4.plot(range(len(historyMeanRoute)), historyMeanRoute, '--b', linewidth = 3, label="Mean Fitness")
            ax4.plot(range(len(historyBestRoute)), historyBestRoute, '--r', linewidth = 3,  label="Best Fitness")
            ax4.plot(range(len(historyBestRoute) - 1, len(historyBestRoute) + len(historyOptiDist) - 1), historyOptiDist, '--y', linewidth = 3, label="Optimized Fitness")
            ax4.plot(i + 1 + numberOfTwoOpt, historyOptiDist[-1], "om", label='Most Optimized Point')
            ax4.annotate(f"{round(historyOptiDist[-1], 5)}", 
                          ((len(historyBestRoute) + len(historyOptiDist) - 2), historyOptiDist[-1]), 
                          textcoords='offset points', 
                          xytext=(0, 50),
                          arrowprops=dict(facecolor='green',
                                          connectionstyle='angle3',
                                          arrowstyle='simple',                          
                                          ),
                          ha='center',
                          va='top'
                        )
            ax4.legend()
            
            # 2 - AGAINST TIME (ALGORITHMIC TIME)
            algorithmicTime = iterFinishTime - iterStartTime
            loopTime = optiStartTime - iterStartTime
            optiTime = iterFinishTime - optiStartTime
            
            timeStepSize1 = np.linspace(0, 
                                        loopTime,
                                        len(historyMeanRoute), 
                                        True, 
                                        dtype='float64').tolist()
            timeStepSize1 = [round(i, 2) for i in timeStepSize1]
            
            # MEAN FITNESS
            fig1, ax1 = plt.subplots()
            plt.style.use('dark_background')
            ax1.set_xlabel("Time Taken (seconds)")
            ax1.set_ylabel("Mean Fitness")
            ax1.set_title("Variation of Mean Fitness")
            ax1.plot(timeStepSize1, historyMeanRoute, '--b', linewidth = 3, label="Mean Fitness")
            ax1.legend()
            
            # BEST FITNESS
            fig2, ax2 = plt.subplots()
            plt.style.use('dark_background')
            ax2.set_xlabel("Time Taken (seconds)")
            ax2.set_ylabel("Best Fitness")
            ax2.set_title("Variation of Best Fitness")
            ax2.plot(timeStepSize1, historyBestRoute, '--r', linewidth = 3, label="Best Fitness")
            ax2.legend()
            
            timeStepSize2 = np.linspace(0, 
                                        optiTime, 
                                        len(historyOptiDist), 
                                        True, 
                                        dtype='float64').tolist()
            timeStepSize2 = [round(i, 2) for i in timeStepSize2]
            
            # OPTIMIZATION FITNESS
            fig3, ax3 = plt.subplots()
            plt.style.use('dark_background')
            ax3.set_xlabel("Time Taken (seconds)")
            ax3.set_ylabel("Optimized Fitness")
            ax3.set_title("Variation of Best Fitness due to 2-Opt Optimization")
            ax3.plot(timeStepSize2, historyOptiDist, '--y', linewidth = 3, label="Optimized Fitness")
            ax3.plot(timeStepSize2[-1], historyOptiDist[-1], "om", label='Most Optimized Point')
            ax3.annotate(f"{round(historyOptiDist[-1], 5)}", 
                         (timeStepSize2[-1], historyOptiDist[-1]), 
                         textcoords='offset points', 
                         xytext=(0, 50),
                         arrowprops=dict(facecolor='green',
                                         connectionstyle='angle3',
                                         arrowstyle='simple',                          
                                         ),
                         ha='center',
                         va='top'
                        )
            ax3.legend()
            
            timeStepSize3 = np.linspace(loopTime, 
                                        loopTime + optiTime, 
                                        len(historyOptiDist), 
                                        True, 
                                        dtype='float64').tolist()
            timeStepSize3 = [round(i, 2) for i in timeStepSize3]
            
            # COMBINED - MEAN FITNESS, BEST FITNESS, OPTIMIZATION & MOST OPTIMIZED POINT
            fig4, ax4 = plt.subplots()
            plt.style.use('dark_background')
            ax4.set_xlabel("Time Taken (seconds)")
            ax4.set_ylabel("Mean Fitness | Best Fitness | Optimized Point")
            ax4.set_title("Variation of Mean Fitness, Best Fitness, Optimization & Most Optimized Point ")
            ax4.plot(timeStepSize1, historyMeanRoute, '--b', linewidth = 3, label="Mean Fitness")
            ax4.plot(timeStepSize1, historyBestRoute, '--r', linewidth = 3,  label="Best Fitness")
            ax4.plot(timeStepSize3, historyOptiDist, '--y', linewidth = 3,  label="Optimized Fitness")
            ax4.plot(timeStepSize3[-1], historyOptiDist[-1], "om", label='Most Optimized Point')
            ax4.annotate(f"{round(historyOptiDist[-1], 5)}", 
                         (timeStepSize3[-1], historyOptiDist[-1]), 
                         textcoords='offset points', 
                         xytext=(0, 50),
                         arrowprops=dict(facecolor='green',
                                         connectionstyle='angle3',
                                         arrowstyle='simple',                          
                                         ),
                         ha='center',
                         va='top'
                        )
            ax4.legend()
            
            # TIME TAKEN
            finalFinishTime = time.time()
            print((f"* Algorithmic Time Taken --> {round((algorithmicTime/60), 3)} minutes\n"))
            print((f"* Total Time Taken --> {round(((finalFinishTime - mainBeginTime)/60), 3)} minutes\n"))
            print("-------------------------------------------------------------\n")
            print("Plots: First 4 against Number of Iterations, Next 4 against Time")
            
            meanObjective = meanRouteLength
            bestObjective = optimizedRouteLength
            bestSolution = np.array(optimizedRoute)
            
          # while( yourConvergenceTestsHere ):
    
            # Your code here.
    
            # Call the reporter with:
            #  - the mean objective function value of the population
            #  - the best objective function value of the population
            #  - a 1D numpy array in the cycle notation containing the best solution 
            #    with city numbering starting from 0
            timeLeft = self.reporter.report(meanObjective, bestObjective, bestSolution)
            if timeLeft < 0:
                break
            
            break

        # Your code here.
        return meanObjective, bestObjective, bestSolution


########################################################################