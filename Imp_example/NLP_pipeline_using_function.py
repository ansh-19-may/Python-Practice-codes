def build_vocab(corpus):
    vocab = {}
    for sentence in corpus:
        for word in sentence.split():
            if word not in vocab:
                vocab[word] = len(vocab)

    return vocab

def encode_sentence(sentence,vocab):
    encoded = [vocab[word] for word in sentence.split()]
    return encoded

c = ["ai loves data", "data powers ai"]
vocab = build_vocab(c) 
print(vocab)           

sentence = "ai loves data"

encoded = encode_sentence(sentence,vocab)
print(encoded)