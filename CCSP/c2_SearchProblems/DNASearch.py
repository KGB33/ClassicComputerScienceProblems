from enum import IntEnum
from itertools import zip_longest

"""
Glossary:
    Nucleotide: A, C, G, or T
    Codon: 3 Nucleotides
    Gene: Multiple Codons
"""
Nucleotide = IntEnum("Nucleotide", ("A", "C", "G", "T"))


def main():
    gene_str = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC"
    my_gene = string_to_gene(gene_str)
    sorted_gene = sorted(my_gene)
    in_gene = (Nucleotide.C, Nucleotide.C, Nucleotide.C)
    not_in_gene = (Nucleotide.A, Nucleotide.C, Nucleotide.T)
    print(f"Linear Search (pass): {linear_contains(my_gene, in_gene)}")
    print(f"Linear Search (fail): {linear_contains(my_gene, not_in_gene)}")
    print()
    print(f"Binary Search (pass): {binary_contains(sorted_gene, in_gene)}")
    print(f"Binary Search (fail): {binary_contains(sorted_gene, not_in_gene)}")
    print()


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def string_to_gene(s):
    gene = []
    for i in grouper(s, 3, "X"):
        if "X" in i:
            return gene
        codon = tuple([Nucleotide[n] for n in i])
        gene.append(codon)
    return gene


def linear_contains(gene, key_codon):
    """
    Equivalent to
        key_codon in gene
    """
    for codon in gene:
        if codon == key_codon:
            return True
    return False


def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low <= high:  # While there is still a search space
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


if __name__ == "__main__":
    main()
