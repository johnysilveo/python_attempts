import random
import string

# Load words from the external file
def load_word_list(filename="english_words.txt"):
    """Loads English words from a file into a set."""
    try:
        with open(filename, "r") as f:
            words = set(word.strip().lower() for word in f.readlines() if word.strip().isascii())  # Only English words
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found! Make sure the file exists.")
        return set()

# Load the word list
english_words = load_word_list()

def get_random_word_of_length(length):
    """Finds a random English word with the specified length."""
    filtered_words = [word for word in english_words if len(word) == length]
    return random.choice(filtered_words) if filtered_words else "X" * length  # Fallback if no match found

def replace_words_with_real_words(sentence):
    """Replaces words with real English words while keeping punctuation."""
    words_in_sentence = sentence.split()
    replaced_words = []
    
    for word in words_in_sentence:
        stripped_word = word.strip(string.punctuation)  # Remove punctuation
        new_word = get_random_word_of_length(len(stripped_word)) if stripped_word else word
        replaced_words.append(new_word + word[len(stripped_word):])  # Preserve punctuation

    return ' '.join(replaced_words)

# Get user input
user_sentence = input("Enter a sentence: ")
modified_sentence = replace_words_with_real_words(user_sentence)

# Show results
print("\nOriginal Sentence: ", user_sentence)
print("Modified Sentence:", modified_sentence)