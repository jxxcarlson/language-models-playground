from nltk.corpus import reuters

# Print the total number of documents in the corpus
print(len(reuters.fileids()))

# Print the text of the first document in the corpus
print(reuters.raw(fileids=reuters.fileids()[0]))

