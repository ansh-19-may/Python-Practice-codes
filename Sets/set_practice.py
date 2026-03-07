nums =[1,2,2,3,4,4,5]
num_set = set(nums)

if 5 in num_set:
    print("5 is present")

#Finding common element
A = [1,2,3,4]
B = [3,4,5,6]

print(f' common elements are  {set(A) & set(B)}')

# Finding elements only in A
A = [1,2,3,4]
B = [3,4,5,6]

print(f' Elements only in A are   {set(A) - set(B)}')


# Finding Jaccard similarity
text1 = "machine learning is fun"
text2 = "machine learning is powerful"

M = set(text1.split())
N = set(text2.split())

similarity = len(M & N) / len(M | N)
print(f'Jaccard Similarity is  {similarity}') 

# Removing stopwords
stopwords = {"is","the","a","and"}
text = "ai is the future and ai is powerful"
words = text.split()

without_stopwords = [word for word in words if word not in stopwords]
print(set(without_stopwords))

