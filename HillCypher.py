def preprocess_message(message, block_size):
    message = ''.join([c for c in message.upper() if c.isalpha()])
    while len(message) % block_size != 0:
        message += "X"
    return message

def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def mat_vec_mul(matrix, vector):
    result = []
    for row in matrix:
        val = sum(row[i] * vector[i] for i in range(len(vector))) % 26
        result.append(val)
    return result

def encrypt(message, key_matrix):
    block_size = len(key_matrix)
    message = preprocess_message(message, block_size)
    ciphertext = ""
    for i in range(0, len(message), block_size):
        block = message[i:i + block_size]
        vector = [char_to_num(c) for c in block]
        encrypted_vector = mat_vec_mul(key_matrix, vector)
        ciphertext += ''.join(num_to_char(num) for num in encrypted_vector)
    return ciphertext

if __name__ == "__main__":
    msg = input("Enter the message to encrypt: ")
    size = int(input("Enter key matrix size (2 or 3): "))
    if size not in (2, 3):
        raise ValueError("Only 2x2 or 3x3 key matrices are supported.")
    print(f"Enter the {size}x{size} key matrix row by row (space-separated numbers):")
    key_matrix = []
    for i in range(size):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != size:
            raise ValueError("Each row must have the same number of elements as the matrix size.")
        key_matrix.append(row)
    encrypted = encrypt(msg, key_matrix)
    print(f"\nPlaintext: {msg}")
    print(f"Ciphertext: {encrypted}")
