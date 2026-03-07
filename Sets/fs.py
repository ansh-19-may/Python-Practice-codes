corpus = [
"ai loves data science",
"data science powers ai",
"ai transforms industries"
]

vocab = {}

for sentence in corpus:
    for word in sentence.split():
        if word not in vocab:
            vocab[word] = len(vocab)

print(vocab)     

encoded = [[vocab[word] for word in sentence.split()] for sentence in corpus]
print(encoded)