from GeneralGeneticAlgorithum import Chromosome, GeneticAlgorithum
from random import randrange, random
from copy import deepcopy
from inspect import getsource


class SimpleEquation(Chromosome):
    def __init__(self, x, y, l=(lambda a, b: 6 * a - a * a + 4 * b - b * b)):
        self.x = x
        self.y = y
        self.equation = l

    def fitness(self):
        return self.equation(self.x, self.y)

    @classmethod
    def random_instance(cls):
        return SimpleEquation(randrange(100), randrange(100))

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2

    def mutate(self):
        if random() > 0.5:
            if random() > 0.5:
                self.x = -1
            else:
                self.x = +1
        else:
            if random() > 0.5:
                self.y = -1
            else:
                self.y = +1

    def __str__(self):
        return f"Fitness: {self.fitness()} for ({self.x}, {self.y})"


if __name__ == "__main__":
    inital_population = [SimpleEquation.random_instance() for _ in range(200)]
    ga = GeneticAlgorithum(inital_population, threshold=13.0)
    result = ga.run()
    print(result)
