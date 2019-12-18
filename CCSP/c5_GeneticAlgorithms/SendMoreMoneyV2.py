from GeneralGeneticAlgorithum import Chromosome, GeneticAlgorithum
from random import shuffle, sample
from copy import deepcopy


class SendMoreMoney2(Chromosome):
    def __init__(self, letters):
        self.letters = letters

    def get_smmd_vals(self):
        s = str(self.letters.index("s"))
        e = str(self.letters.index("e"))
        n = str(self.letters.index("n"))
        d = str(self.letters.index("d"))
        m = str(self.letters.index("m"))
        o = str(self.letters.index("o"))
        r = str(self.letters.index("r"))
        y = str(self.letters.index("y"))
        send = int(s + e + n + d)
        more = int(m + o + r + e)
        money = int(m + o + n + e + y)
        diff = abs(money - (send + more))
        return send, more, money, diff

    def fitness(self):
        *smm, diff = self.get_smmd_vals()
        return 1 / ( diff + 1)

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        idx1, idx2 = sample(range(len(self.letters)), k=2)
        l1, l2 = child1.letters[idx1], child2.letters[idx2]
        child1.letters[child1.letters.index(l2)], child1.letters[idx2] = child1.letters[idx2], l2
        child2.letters[child2.letters.index(l1)], child2.letters[idx1] = child2.letters[idx1], l1
        return child1, child2

    def mutate(self):
        idx1, idx2 = sample(range(len(self.letters)), k=2)
        self.letters[idx1], self.letters[idx2] = self.letters[idx2], self.letters[idx1]

    def __str__(self):
        send, more, money, diff = self.get_smmd_vals()
        return f'{send=:04d} + {more=:04d} = {money=:05d} --- {diff=}'

    @classmethod
    def random_instance(cls, letters=('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y', '', '')):
        letters = list(letters)
        shuffle(letters)
        return SendMoreMoney2(letters)

if __name__ == "__main__":
    init_pop = [SendMoreMoney2.random_instance() for _ in range(1000)]
    ga = GeneticAlgorithum(initial_population=init_pop, threshold=1.0, max_generations=1000, mutation_chance=0.2, selection_type=GeneticAlgorithum.SelectionType.ROULETTE)
    result = ga.run()
    print(result)
        
