import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("dog")
word2 = nlp("puppy")

similarity = word1.similarity(word2)
print(f"The similarity between 'dog' and 'puppy' is: {similarity}")
