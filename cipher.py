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

name, profession, bio = "Sanjay", "Computer Science Engineer", \
"I am a passionate developer who loves AI, cloud computing, and creating innovative solutions."

# Encrypt
name_enc = caesar(name, 3)
profession_enc = caesar(profession, 3)
bio_enc = vigenere(bio, "portfolio")

# Decrypt
print("Encrypted:", name_enc, profession_enc, bio_enc, sep="\n")
print("\nDecrypted:",
      caesar(name_enc, -3),
      caesar(profession_enc, -3),
      vigenere(bio_enc, "portfolio", enc=False), sep="\n")
