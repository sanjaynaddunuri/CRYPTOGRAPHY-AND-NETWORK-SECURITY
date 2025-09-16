import math

# Round function: XOR and map to printable ASCII
def round_function(right, key):
    result = ''
    key_len = len(key)
    for i, char in enumerate(right):
        xor_result = ord(char) ^ ord(key[i % key_len])
        # Map to printable ASCII range (33 to 126)
        printable_char = chr((xor_result % 94) + 33)
        result += printable_char
    return result

# Perform one Feistel round
def feistel_round(left, right, key):
    new_right = ''
    round_res = round_function(right, key)
    for l, rf in zip(left, round_res):
        xor_char = (ord(l) ^ ord(rf)) % 94 + 33
        new_right += chr(xor_char)
    return right, new_right  # Swap halves

# Pad plaintext to multiple of block size (8 chars)
def pad_plaintext(plaintext, block_size):
    padding_len = block_size - (len(plaintext) % block_size)
    return plaintext + (' ' * padding_len)

# Main Feistel encryption function
def feistel_encrypt(plaintext, key, rounds=4):
    block_size = 8  # Fixed block size
    plaintext = pad_plaintext(plaintext, block_size)

    encrypted_text = ''

    # Process block by block
    for block_start in range(0, len(plaintext), block_size):
        block = plaintext[block_start:block_start + block_size]

        # Split block into Left and Right halves
        mid = block_size // 2
        left = block[:mid]
        right = block[mid:]

        # Perform multiple Feistel rounds
        for _ in range(rounds):
            left, right = feistel_round(left, right, key)

        # Combine final halves
        encrypted_block = left + right
        encrypted_text += encrypted_block

    return encrypted_text  # Return as readable string


if _name_ == "_main_":
    plaintext = input("Enter the plaintext message: ")
    key = input("Enter the key: ")

    encrypted_message = feistel_encrypt(plaintext, key)
    print("\nEncrypted message:", encrypted_message)
