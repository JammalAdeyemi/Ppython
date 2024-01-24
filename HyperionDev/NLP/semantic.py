# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from 
# the model 'en_core_web_md'.

import spacy

nlp_md = spacy.load("en_core_web_md")
nlp_sm = spacy.load("en_core_web_sm")
# Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an 
# example of your own.

notes = ["""I found it interesting that all three of these words, "cat", "monkey", and "banana", relate to the animal kingdom. 
                "Cat" and "monkey" are both common domesticated and wild animals, while "banana" is a type of fruit that is often 
                associated with primates, like monkeys. I think of a similar example with the words "dog", "wolf", and "meat"."""]

similarities = ("The cat chased the monkey, who was holding a banana.")


print("Results using en_core_web_sm:")
for similarity in similarities:
    doc_sm = nlp_sm(similarity)
    for token in doc_sm:
        print(token.text, token.pos_, token.dep_)

print("\nResults using en_core_web_md:")
for similarity in similarities:
    doc_md = nlp_md(similarity)
    for token in doc_md:
        print(token.text, token.pos_, token.dep_)

# When using the spaCy library with the "en_core_web_sm" model, the output for entity recognition was less comprehensive than 
# with the "en_core_web_md" model. The "en_core_web_sm" model is smaller and faster, but has less accuracy compared to the 
# "en_core_web_md" model, which is larger and more resource-intensive but provides a more detailed and accurate output.