def print_values_of(dictionary, keys):
    # Fix1 : changed the k to key to avoid keyerror
    for key in keys:
        print(dictionary[key])

# Fix2 : corrected the identifier 
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd\'oh', "maggie": " (Pacifier Suck)"}

# Fix3 : changed the arguments to a list to match the function signature
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])




