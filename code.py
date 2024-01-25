from random import randint

genes = bytearray(b'abcdefghijklmnopqrstuvwxyz ')

final_chromo = bytearray(b'the quick brown fox jumps over the lazy dog')
chromo_size = len(final_chromo)
population_size = 20

def create_random_chromo(size, genes):
    chromo = bytearray(size)
    genes_size = len(genes)
    for i in range(size):
        rand_pos = randint(0, genes_size - 1)
        chromo[i] = genes[rand_pos]

    return chromo
    
def create_population(pop_size, chromo_size, genes):
    population = [None] * pop_size
    for i in range(pop_size):
        population[i] = create_random_chromo(chromo_size, genes)

    return population

population = create_population(population_size, chromo_size, genes)
print (population)