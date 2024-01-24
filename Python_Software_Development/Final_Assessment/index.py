import string

# Read the main words from the mainWords.txt file
with open('mainWords.txt', 'r') as file:
    main_words = set(word.strip() for word in file)

# Initialize an empty dictionary for the index
index = {}

# Open the article.txt file for reading
with open('article.txt', 'r') as file:
    # Keep track of the current line number
    line_number = 1
    # Read the file line by line
    for line in file:
        # Remove punctuation from the line
        line = line.translate(line.maketrans('', '', string.punctuation))
        # Convert the line to lowercase
        line = line.lower()
        # Split the line into words
        words = line.split()
        # Iterate through the words
        for word in words:
            # Check if the word is a main word
            if word in main_words:
                # If the word is not already in the index, add it
                if word not in index:
                    index[word] = set()
                # Add the current line number to the set of line numbers for the word
                index[word].add(line_number)
        # Increment the line number
        line_number += 1

# Print the index in alphabetical order
for word in sorted(index.keys()):
    print(f"{word}: {sorted(index[word])}")
