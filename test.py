import spacy

nlp = spacy.load("E:\work\Daily/2_19\classification\out\model-best")
text = ""
re = nlp(text)
print(re.cats)