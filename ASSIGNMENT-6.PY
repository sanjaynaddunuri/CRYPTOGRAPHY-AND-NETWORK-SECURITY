from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(secret):
    """
    Generate a valid Fernet key from a user-provided secret.
    Fernet requires a 32-byte base64-encoded key.
    """
    # Hash the secret key using SHA-256 to ensure 32 bytes
    hash_key = hashlib.sha256(secret.encode()).digest()
    # Base64-encode the key for Fernet
    return base64.urlsafe_b64encode(hash_key)

def encrypt_message(key, plaintext):
    """
    Encrypt the plaintext message using the generated key.
    Returns the ciphertext in Base64 format.
    """
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    return encrypted.decode()

def main():
    print("=== AES Encryption Utility ===")
    
    # Get plaintext input
    plaintext = input("Enter the plaintext message: ").strip()
    if not plaintext:
        print("Error: Plaintext cannot be empty.")
        return

    # Get secret key input
    secret_key = input("Enter the secret key (16, 24, or 32 characters): ").strip()
    if len(secret_key) not in [16, 24, 32]:
        print("Error: Secret key must be 16, 24, or 32 characters long.")
        return

    # Generate a valid Fernet key
    key = generate_key(secret_key)

    # Encrypt the plaintext
    ciphertext = encrypt_message(key, plaintext)

    # Display results
    print("\n--- Encryption Result ---")
    print(f"Plaintext : {plaintext}")
    print(f"Ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()