from collections import defaultdict

# Example corpus
corpus = [
    "machine learning is powerful",
    "ai and machine learning are the future",
    "ai is transforming the world"
]

# Step 1: Tokenization
tokenized = [sentence.split() for sentence in corpus]

# Step 2: Stopword removal
stopwords = {"is", "the", "and", "are"}

filtered_tokens = [
    [word for word in sentence if word not in stopwords]
    for sentence in tokenized
]

# Step 3: Build vocabulary (word -> index)
vocab = {}

for sentence in filtered_tokens:
    for word in sentence:
        if word not in vocab:
            vocab[word] = len(vocab)

# Step 4: Word frequency
freq = defaultdict(int)

for sentence in filtered_tokens:
    for word in sentence:
        freq[word] += 1

# Step 5: Encode sentences
encoded_sentences = [
    [vocab[word] for word in sentence]
    for sentence in filtered_tokens
]

# Step 6: Jaccard similarity between first two sentences
s1 = set(filtered_tokens[0])
s2 = set(filtered_tokens[1])

similarity = len(s1 & s2) / len(s1 | s2)

# Print results
print("Tokenized:", tokenized)
print("Filtered tokens:", filtered_tokens)
print("Vocabulary:", vocab)
print("Word frequency:", dict(freq))
print("Encoded sentences:", encoded_sentences)
print("Jaccard similarity:", similarity)