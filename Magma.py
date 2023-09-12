print("Welcome to Magma!! Full release") # says hello to user
print("©Pylearner1234567890")
# Function to encrypt text using a Caesar cipher
def encrypt_text(key, plaintext):
    encrypted_text = []
    for char in plaintext:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

# Function to decrypt text using a Caesar cipher
def decrypt_text(key, ciphertext):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

# Input text
text = input("Enter the text to encrypt: ")

# Choose an encryption key (integer)
key = int(input("Enter the encryption key (an integer): "))

# Encrypt the text
encrypted_text = encrypt_text(key, text)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the text
decrypted_text = decrypt_text(key, encrypted_text)
print(f"Decrypted Text: {decrypted_text}")
