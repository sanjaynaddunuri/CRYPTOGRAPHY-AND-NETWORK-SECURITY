# Caesar Cipher
def caesar(text, shift):
    return ''.join(
        chr((ord(c) - b + shift) % 26 + b) if c.isalpha() else c
        for c in text
        for b in [ord('A') if c.isupper() else ord('a')]
    )

# Vigenère Cipher
def vigenere(text, key, enc=True):
    key = key.lower()
    res, k = '', 0
    for c in text:
        if c.isalpha():
            s = ord(key[k % len(key)]) - ord('a')
            if not enc: s = -s
            b = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - b + s) % 26 + b)
            k += 1
        else: res += c
    return res

name = input("Enter Name: ")
prof = input("Enter Profession: ")
bio  = input("Enter Bio: ")

# Keys
shift = int(input("Enter Caesar shift: "))
vig_key = input("Enter Vigenere key: ")

# Encrypt
ne, pe, be = caesar(name, shift), caesar(prof, shift), vigenere(bio, vig_key)
print("\nEncrypted:", ne, pe, be, sep="\n")

# Decrypt
print("\nDecrypted:",
      caesar(ne, -shift),
      caesar(pe, -shift),
      vigenere(be, vig_key, False), sep="\n")
