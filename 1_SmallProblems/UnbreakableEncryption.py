from secrets import token_bytes


def random_key(length):
    tb = token_bytes(length)
    return int.from_bytes(tb, 'big')


def encrypt(original):
    """
    When two Objects are XORd an interesting property is revealed.
        A ^ B = C
        C ^ A = B
        C ^ B = A
    You can take the solution to A ^ B, In this case C, and XOR it with A or B to get the other

     int.from_bytes take two arguments, the second is the byte order. In this application, as long as the same
     'endianness' is used the method will work
    """
    if type(original) != bytes:
        original_bytes = original.encode()
    else:
        original_bytes = original
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, 'big')
    encrypted = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1, key2):
    """
        decrypted.bit_length() + 7) // 8
    is done to avoid a 1-off error
    """
    decrypted = key1 ^ key2
    return decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big').decode()


if __name__ == '__main__':
    key1, key2 = encrypt("A Secret Message")
    print(f'Key 1: {key1}, Key 2: {key2}')
    print(f'Decrypted: {decrypt(key1, key2)}')

