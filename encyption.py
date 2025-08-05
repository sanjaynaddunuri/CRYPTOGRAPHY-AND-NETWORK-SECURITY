text = "HELLO"
encrypted = ""

for char in text:
    encrypted += chr(ord(char) + 3)

print("Encrypted:", encrypted)
