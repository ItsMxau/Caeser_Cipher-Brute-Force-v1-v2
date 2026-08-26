import nltk
from caesar_cipher import encrypt, decrypt

# Import the words corpus from NLTK to get a list of English words
nltk.download('words')  # one-time download
from nltk.corpus import words
english_words = set(words.words())  # a set of ~236,000 English words


def brute_force_v1(ciphertext):
    # Try all possible keys (1-75) for the Caesar cipher
    for key in range(1, 76):
        decrypted_text = decrypt(ciphertext, key)
        # Split the decrypted text into words and check how many are valid English words
        word_list = decrypted_text.split()
        valid_word_count = sum(1 for word in word_list if word.lower() in english_words)

        # If a significant number of words are valid, print the result
        if valid_word_count > len(word_list) / 2:  # more than half of the words are valid
            print(f"Possible decryption with key {key}: {decrypted_text} (Valid words: {valid_word_count}/{len(word_list)})")

def brute_force_v2(ciphertext, plaintext):
    # Try all possible keys (1-75) for the Caesar cipher v2 (simulating real world scenarios)
    for key in range(1, 76):
        decrypted_text = decrypt(ciphertext, key)
        if decrypted_text == plaintext:
            print(f"Exact match found with key {key}: {decrypted_text}")



if __name__ == "__main__":
    # Make a known ciphertext to test against
    original_text = "hello how are you"
    test_key = 5
    test_ciphertext = encrypt(original_text, test_key)

    print(f"Original: {original_text}")
    print(f"Encrypted with key {test_key}: {test_ciphertext}") 
    print()

    print("--- Running brute_force_v1 (word-matching) ---")
    brute_force_v1(test_ciphertext) 
    # Actually recieved two possible keys, 5 and 31, because of the capitalization of the 
    # text (characters contains both uppercase and lowercase letters, so the decryption can 
    # yield different results based on the case of the letters). Key 5 would be best practice
    # as it gets the message faster. For such a small message, the brute force method is quick 
    # either way, but for larger messages, time complexity would be a concern.  

    print()
    print("--- Running brute_force_v2 (exact match) ---")
    brute_force_v2(test_ciphertext, original_text)
