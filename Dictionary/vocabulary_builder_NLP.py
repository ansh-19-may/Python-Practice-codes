# build a word → id mapping.
# Step 1 - We create a vocab dictionary for word id mapping 

text = "machine learning is fun machine learning"
words = text.split()
vocab = {}

for word in words:
    if word not in vocab:
        vocab[word] = len(vocab)

print(vocab)

'''
Why this matters:
Neural networks cannot process words, they process numbers.
So tokenizers convert:

this -> machine learning is fun      to this -> [0,1,2,3]

once we have vocabulary then we convert sentences to numbers 
'''

#Step 2 - Index encoder (Tokenization step)
sentence = "machine learning is fun"
tokens = sentence.split()

encoded = [vocab[word] for word in tokens]
print(encoded)

'''
This is exactly how LLM tokenization pipelines begin
'''

# Step 3 - Sparse Vector builder (frequency vector)
'''
In classical ML and some NLP pipelines we represent text as frequency vectors.

For ex : 

plaintext -> machine learning machine

our vocab {
'machine':0,
'learning':1,
'is':2,
'fun':3
}

sparse vector representation -> 

{
0:2   ( 0 -> id for 'machine' ,  2 -> times 'machine' comes in the sentence )
1:1   (same as above)
}

'''

freq_vector = {}
for word in words:
    idx =vocab[word]    # taking id of word from vocab dict , 
    freq_vector[idx] = freq_vector.get(idx,0) + 1     # creating sparse vector for freq

print(freq_vector)    

'''  This structure is heavily used in bag-of-words models.   '''



