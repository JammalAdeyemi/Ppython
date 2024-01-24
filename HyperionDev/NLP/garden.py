import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["The old man the boat.", "The complex houses married and single soldiers and their families.", "The horse raced past the barn fell."
                        "The cotton clothing is made of grows in Mississippi.", "The mango ate the ripe pear with gusto.The horse raced past the barn fell.",  
                        "Time flies like an arrow; fruit flies like a banana"]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    #  Tokenise each sentence
    print("Tokenise each sentence")
    print([(token, token.orth_, token.orth) for token in doc])
    print()
    #  Remove punctuation and white space
    print("Remove punctuation and white space")
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    print()
    # Get labels and entities and print them
    print("Get labels and entities and print them")
    print([(i, i.label_, i.label) for i in doc.ents])
    print()
    # Get an explanation of an entity and print it
    print("Get an explanation of an entity and print it")
    print([(i, i.label_, spacy.explain(i.label_)) for i in doc.ents])
    print()      


# Entity "GPE":
# Explanation: Countries, cities, states.
# It makes sense in terms of the word associated with it, as GPE stands for "Geo-Political Entity" and is used to identify geographical locations.

# Entity "FAC":
# Explanation: Buildings, airports, highways, bridges, etc.
# It makes sense in terms of the word associated with it, as FAC stands for "Facility" and is used to identify different types of structures or establishments.  
