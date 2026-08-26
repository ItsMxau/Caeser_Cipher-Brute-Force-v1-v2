characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=-"

def encrypt(plaintext, key):
    ciphertext = ""
    key = key % len(characters)

    for letter in plaintext:
        if letter in characters:
            index = characters.find(letter)
            new_index = (index + key) % len(characters)
            ciphertext += characters[new_index]
        else:
            ciphertext += letter

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    key = key % len(characters)

    for letter in ciphertext:
        if letter in characters:
            index = characters.find(letter)
            new_index = (index - key) % len(characters)
            plaintext += characters[new_index]
        else:
            plaintext += letter

    return plaintext

if __name__ == "__main__":
    while True:
        print("\nWelcome to the Caesar Cipher Program!")
        print("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit")
        user_input = input("Enter your choice: ").lower()
    
        if user_input == 'q':
            print("Goodbye!")
            break   # <-- exits the while loop immediately, skips everything below
        elif user_input == "e":
            print("*** ENCRYPTION MODE SELECTED ***")
            print()
            key = int(input("Enter a key (1-75): "))
            text = input("Enter the message to encrypt : ")
            ciphertext = encrypt(text, key)
            print('CIPHERTEXT: ' + ciphertext)
        elif user_input == "d":
            print("*** DECRYPTION MODE SELECTED ***")
            print()
            key = int(input("Enter a key (1-75): "))
            text = input("Enter the message to decrypt : ")
            plaintext = decrypt(text, key)
            print('PLAINTEXT: ' + plaintext)
        else:
            print("Invalid choice. Please try again.")