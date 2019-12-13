class CompressedGene:
    def __init__(self, gene):
        self.gene = self.compress(gene)

    def __str__(self):
        return self.decompress()

    def decompress(self):
        g = ""
        for i in range(0, self.gene.bit_length() - 1, 2):  # -1 to exclude sentinal Val
            bits = self.gene >> i & 0b11  # gets 2 bits at a time
            if bits == 0b00:
                g += "A"
            elif bits == 0b01:
                g += "C"
            elif bits == 0b10:
                g += "G"
            elif bits == 0b11:
                g += "T"
            else:
                raise ValueError(f"Invalid Bits {bits}")
        return g[::-1]  # [::-1] reverses the string by slicing backwards

    @staticmethod
    def compress(gene_in):
        """
        Compresses a gene into a bit string

        stats with
            0b1
        Shift Left Two Bits
            0b100
        OR's the Last Two Bits
            0b100 = 0b100 || 0bxx
        """
        bit_string = 1  # start with a sentinel
        for nucleotide in gene_in.upper():
            bit_string <<= 2  # Shift left two bits
            if nucleotide == "A":
                bit_string |= 0b00
            elif nucleotide == "C":
                bit_string |= 0b01
            elif nucleotide == "G":
                bit_string |= 0b10
            elif nucleotide == "T":
                bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide {nucleotide}")
        return bit_string


if __name__ == "__main__":
    from sys import getsizeof

    original = (
        "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC" * 100
    )
    print(f"Original is {getsizeof(original)} Bytes")
    compressed = CompressedGene(original)
    print(f"Compressed is {getsizeof(compressed.gene)} Bytes")
    print(
        f"Original and Compressed are the same: {original == compressed.decompress()}"
    )
