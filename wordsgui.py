import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import random
import string

# --------------------- Functions from our original code --------------------- #

def load_word_list(filename="english_words.txt"):
    """
    Loads English words from a file into a set.
    The file should have one word per line.
    """
    try:
        with open(filename, "r") as f:
            # Read each line, strip whitespace, convert to lowercase, and filter ASCII words.
            words = set(word.strip().lower() for word in f.readlines() if word.strip().isascii())
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found! Make sure the file exists.")
        return set()

# Load the word list (ensure english_words.txt is in the same folder as your script or use a full path)
english_words = load_word_list()

def get_random_word_of_length(length):
    """
    Returns a random English word of the given length.
    If no word of that length exists, returns a fallback string.
    """
    filtered_words = [word for word in english_words if len(word) == length]
    return random.choice(filtered_words) if filtered_words else "X" * length

def replace_words_with_real_words(sentence):
    """
    Replaces each word in the input sentence with a random English word of the same length.
    Punctuation at the beginning or end of a word is preserved.
    """
    words_in_sentence = sentence.split()  # Split the sentence into words based on whitespace.
    replaced_words = []
    
    for word in words_in_sentence:
        # Remove leading/trailing punctuation.
        stripped_word = word.strip(string.punctuation)
        # If there's a valid word, replace it; otherwise, keep the original.
        new_word = get_random_word_of_length(len(stripped_word)) if stripped_word else word
        # Append any trailing punctuation back to the new word.
        replaced_words.append(new_word + word[len(stripped_word):])
    
    # Reassemble the sentence.
    return ' '.join(replaced_words)

# -------------------------- GUI Code using Tkinter --------------------------- #

def process_sentence():
    """
    Retrieves the sentence from the entry widget, processes it,
    and updates the output label with the modified sentence.
    """
    sentence = entry.get()
    if not sentence:
        messagebox.showwarning("Input Error", "Please enter a sentence.")
        return
    modified = replace_words_with_real_words(sentence)
    output_label.config(text="Modified Sentence: " + modified)

def update_font():
    """
    Updates the global font size for the GUI widgets based on the spinbox value.
    """
    try:
        new_size = int(font_size_spinbox.get())
        current_font.config(size=new_size)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for font size.")

# Create the main window
root = tk.Tk()
root.title("Word Replacement GUI with Font Settings")

# Create a font object for consistent styling
current_font = tkFont.Font(family="Helvetica", size=12)

# Create a frame for padding and organization
frame = ttk.Frame(root, padding="10")
frame.grid()

# -------------------- GUI Widgets for the Sentence Replacement -------------------- #

# Input label prompting the user
input_label = ttk.Label(frame, text="Enter a sentence:", font=current_font)
input_label.grid(column=0, row=0, sticky="W")

# Entry widget for the user to type a sentence
entry = ttk.Entry(frame, width=50, font=current_font)
entry.grid(column=0, row=1, sticky="W")

# Button that triggers the word replacement process
process_button = ttk.Button(frame, text="Replace Words", command=process_sentence)
process_button.grid(column=0, row=2, pady="10")

# Label to display the modified sentence
output_label = ttk.Label(frame, text="Modified Sentence: ", font=current_font)
output_label.grid(column=0, row=3, sticky="W")

# -------------------- GUI Widgets for Font Size Settings -------------------- #

# Label for font size setting
font_size_label = ttk.Label(frame, text="Font Size:", font=current_font)
font_size_label.grid(column=0, row=4, sticky="W", pady=(20, 0))

# Spinbox for selecting font size (range 8 to 48, default 12)
font_size_spinbox = tk.Spinbox(frame, from_=8, to=48, width=5, font=current_font)
font_size_spinbox.delete(0, "end")
font_size_spinbox.insert(0, "12")
font_size_spinbox.grid(column=0, row=5, sticky="W")

# Button to apply the font size setting
apply_font_button = ttk.Button(frame, text="Apply Font", command=update_font)
apply_font_button.grid(column=0, row=6, pady=(5, 0), sticky="W")

# Start the GUI event loop
root.mainloop()
