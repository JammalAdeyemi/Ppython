import spacy
nlp = spacy.load('en_core_web_md')
#  Read in the movies.txt file. Each separate line is a description of a different movie
movies = open("movies.txt", encoding="utf8").read().splitlines()

# The task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the description
def watch_next():
    # Create a variable called planet_hulk and assign it the description of Planet Hulk
    planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick 
                    Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
                    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""
    # Create a variable called planet_hulk_doc and assign it the nlp version of planet_hulk
    planet_hulk_doc = nlp(planet_hulk)
    # Create a variable called similarity and assign it an empty list
    similarity = []
    # Loop through each movie in the movies list
    for movie in movies:
        movie_doc = nlp(movie)
        similarity.append(planet_hulk_doc.similarity(movie_doc))
    # Create a variable called most_similar and assign it the index of the highest value in the similarity list
    most_similar = similarity.index(max(similarity))
    # Return the movie at the index of most_similar
    return movies[most_similar]

# Call the watch_next function and print the result
print(watch_next())


