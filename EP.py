## SO the idea here is to create algorithm using the Evolutionary Programming formula that is able to get your first name from a random population of 500 strings with the 
## same Length as your name.

##The steps for Evolutionary Programming is:
#1. Initialize the population. In this case we are initializing 500 strings with same length as my first name 'mina'
#2. Calculate fitness for each individual in the population. In this case our fitness function calculates how many letters we got correct in the string, value '4' being the best
#3. Reproduce selected individuals to form a new population using the fitness funciton. In this case we are taking the best 50% of the population, you can either duplicate them to keep the population number 500 or leave them as is. 
#4. Perform mutation on the population. In this case, mutation is done on 20% of the population
#5. Loop to step 2 until some condition is met.

import random 
import string
import math

POP_SIZE = 200
MUT_RATE = 0.2
TARGET = 'mina tamer'
GENES = 'abcdefghiklmnopqrstuvwxyz '

def fitness(string, target):
    score = 0
    for i in range(len(target)):
        if string[i] == target[i]:
            score += 1
    return score

def mutate(individual, genes):
    length = len(individual)
    individual = list(individual)
    index_to_mutate = random.randint(0, length - 1) 
    individual[index_to_mutate] = random.choice(genes)  
    return ''.join(individual)  

# def mutate(sequence):
#     for i in range(len(sequence)):
#         if random.random() < MUT_RATE:
#             sequence[i] = random.choice(string.printable)
#     return sequence



def evolutionary_programming(pop_size, genes, target, mutation_rate):
    target_length = len(target)
    generation = 0
    population = [''.join(random.choice(GENES) for _ in range(len(TARGET))) for _ in range(POP_SIZE)]

    
    while True:
        # calculate fitness scores
        fitness_scores = [(individual, fitness(individual, target)) for individual in population]
        for individual, score in fitness_scores:
            if score == target_length:
                print("Target Reached!")
                best_individual, best_score = max(fitness_scores, key=lambda x: x[1])
                print(f"Generation {generation}: Best string: '{best_individual}', Fitness: {best_score}")
                return individual
        
        # sort fitness scores descendingly 
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        top_half = [individual for individual, _ in fitness_scores[:pop_size // 2]]
    
        best_individual, best_score = max(fitness_scores, key=lambda x: x[1])
        
        # print the best individual and its score for this generation
        fitness_scores = [(individual, fitness(individual, target)) for individual in population]
        print(f"Generation {generation}: Best string: '{best_individual}', Fitness: {best_score}")

        new_population = top_half[:]
        # Duplicate the top half to form the full population (you could also shuffle them)
        while len(new_population) < pop_size:
            new_population.append(random.choice(top_half))

        population = new_population
        #perform mutation according to mut_rate
        num_to_mutate = math.ceil(len(population) * mutation_rate)
        indices_to_mutate = random.sample(range(len(population)), num_to_mutate)
        for index in indices_to_mutate:
            population[index] = mutate(population[index], genes)
        generation += 1

evolutionary_programming(POP_SIZE, GENES, TARGET, MUT_RATE)

