from collections import defaultdict
import heapq
text = "ai is fun ai is powerful ai"

# word frequency dictionary
freq = defaultdict(int)
words = text.split()

for word in words:
    freq[word] += 1

print(freq)   


# vocabulary dictionary
vocab = {}
for w in words:
    if w not in vocab:
        vocab[w] = len(vocab)

print(vocab)    


#encoded sentence
tokens = text.split()
encoded = [vocab[word] for word in tokens]
print(encoded)


#top 2 word

top_k = heapq.nlargest(2,freq.items(),key=lambda x:x[1])
print(dict(top_k).keys()) 
