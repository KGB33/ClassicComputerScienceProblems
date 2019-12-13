from abc import ABC, abstractmethod
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean


class Chromosome(ABC):
    @abstractmethod
    def fitness(self):
        pass

    @classmethod
    @abstractmethod
    def random_instance(cls):
        pass

    @abstractmethod
    def crossover(self, other):
        pass

    @abstractmethod
    def mutate(self):
        pass


class GeneticAlgorithum:
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(
        self,
        initial_population,
        threshold,
        max_generations=100,
        mutation_chance=0.01,
        crossover_chance=0.7,
        selection_type=SelectionType.TOURNAMENT,
    ):
        self._population = initial_population
        self._threshold = threshold
        self._max_generations = max_generations
        self._mutation_chance = mutation_chance
        self._crossover_chance = crossover_chance
        self._selection_type = selection_type
        self._fitness_key = type(self._population[0]).fitness

    def _pick_roulette(self, wheel):
        return tuple(choices(self._population, weights=wheel, k=2))

    def _pick_tournament(self, num_participants):
        participants = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    def _reproduce_and_replace(self):
        new_population = []
        while len(new_population) < len(self._population):

            if self._selection_type == GeneticAlgorithum.SelectionType.ROULETTE:
                parents = self._pick_roulette([x.fitness() for x in self._population])
            else:
                parents = self._pick_tournament(len(self._population) // 2)

            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)

        if len(new_population) > len(self._population):
            new_population.pop()

        self._population = new_population

    def _mutate(self):
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    def run(self):
        best = max(self._population, key=self._fitness_key)
        for generation in range(self._max_generations):
            if best.fitness() >= self._threshold:
                return best

            print(
                f"Generation {generation}; Best {best}; Avg {mean(map(self._fitness_key, self._population))}"
            )

            self._reproduce_and_replace()
            self._mutate()
            highest = max(self._population, key=self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest

        return best
