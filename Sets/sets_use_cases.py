#To remove duplicates 

words = ["ai","ml","ai","data"]
unique_words = set(words)


# Fast stopward filtering. 

stopwords = {"is","the","a","and"}
text = "ai is powerful and useful"
words = text.split()
filtered = [w for w in words if w not in stopwords]
print(filtered)

# Jaccard Similarity (Important)

sent1 = "machine learning is fun"
sent2 = "machine learning is powerful"

A = set(sent1.split())
B = set(sent2.split())

similarity = len(A & B) / len(A | B)
print(similarity)

#Set comprehension

nums = [1,2,2,3,3,4]
unique_squares = {x*x for x in nums}
print(unique_squares)


#To check Superset OR Subset
X = {1,2,3}
Y = {1,2,3,4}

X.issubset(Y)
Y.issuperset(X)






