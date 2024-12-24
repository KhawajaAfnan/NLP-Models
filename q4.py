import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize


nltk.download('punkt')


text = "Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word."

tokens = word_tokenize(text)

porter = PorterStemmer()
lancaster = LancasterStemmer()

porter_stems = [porter.stem(word) for word in tokens]

lancaster_stems = [lancaster.stem(word) for word in tokens]

print(" tokens:", tokens)
print("Porter Stemmer:", porter_stems)
print("Lancaster Stemmer:", lancaster_stems)
