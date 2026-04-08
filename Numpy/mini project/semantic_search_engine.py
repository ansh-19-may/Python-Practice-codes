import numpy as np

# dataset
sentences = [
    "ai will transform the future",
    "machine learning powers ai",
    "the world of data science",
    "deep learning drives innovation"
]

#Step 1 : tokenization 

tokenized = [sentence.split() for sentence in sentences]

#Step 2 : Build vocabulary

vocab = {}

for sentence in tokenized:
    for word in sentence:
        if word not in vocab:
            vocab[word] = len(vocab)


# Step 3 : converting sentences into vectors  ( Bag of Words )

def sentence_vector(sentence,vocab):
    vec = np.zeros(len(vocab))

    for word in sentence.split():
        if word in vocab:
            vec[vocab[word]] += 1

    return vec

# creating matrix of sentence vectors for list of sentences 
list_of_vector_sentence = [sentence_vector(sent,vocab)for sent in sentences]



# Step 4 : finding COSINE SIMILARITY 
def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Step 5 : search the query

#sample sentence
query = "ai future"

# vector of sentence
query_vector = sentence_vector(query,vocab)

# scores after comparing with all the sentence vector 
scores = []

#filling the score in scores[]
for vectors in list_of_vector_sentence:
    scores.append(cosine_similarity(query_vector,vectors))

# index of highest score in scores[]
best_index = np.argmax(scores)


print("Query:",query)
print("Best match:",sentences[best_index])
print("Similarity score:",round(scores[best_index],2))




