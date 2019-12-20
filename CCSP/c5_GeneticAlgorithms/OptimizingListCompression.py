from GeneralGeneticAlgorithum import Chromosome, GeneticAlgorithum
from random import shuffle, sample
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps

PEOPLE = [
    "Michael",
    "Sarah",
    "Joshua",
    "Narine",
    "David",
    "Sajid",
    "Melanie",
    "Daniel",
    "Wei",
    "Dean",
    "Brian",
    "Murat",
    "Lisa",
]


class ListCompression(Chromosome):
    def __init__(self, lst):
        self.lst = lst

    @property
    def bytes_compressed(self):
        return getsizeof(compress(dumps(self.lst)))

    def fitness(self):
        return 1 / (self.bytes_compressed)

    @classmethod
    def random_instance(cls):
        mylst = deepcopy(PEOPLE)
        shuffle(mylst)
        return ListCompression(mylst)

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        idx1, idx2 = sample(range(len(self.lst)), k=2)
        l1, l2 = child1.lst[idx1], child2.lst[idx2]
        child1.lst[child1.lst.index(l2)], child1.lst[idx2] = (
            child1.lst[idx2],
            l2,
        )
        child2.lst[child2.lst.index(l1)], child2.lst[idx1] = (
            child2.lst[idx1],
            l1,
        )
        return child1, child2

    def mutate(self):
        idx1, idx2 = sample(range(len(self.lst)), k=2)
        self.lst[idx1], self.lst[idx2] = self.lst[idx2], self.lst[idx1]

    def __str__(self):
        return f"Order: {self.lst}, Bytes: {self.bytes_compressed}"


if __name__ == "__main__":
    init_pop = [ListCompression.random_instance() for _ in range(100)]
    ga = GeneticAlgorithum(
        initial_population=init_pop,
        threshold=1,
        max_generations=1000,
        mutation_chance=0.2,
    )
    result = ga.run()
    print(f"\n{result}")
    print(f"Bytes to Beat: {getsizeof(compress(dumps(PEOPLE)))}")
