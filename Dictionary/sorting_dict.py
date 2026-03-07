scores = {
"A":90,
"B":70,
"C":85
}

#ascending order 

sorted_scores = sorted(scores.items(), key=lambda x: x[1])
print(sorted_scores) #list of tuples
print(dict(sorted_scores))

# Descending order

sorted_scores_desc = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores_desc) #list of tuples
print(f'desc ->  {dict(sorted_scores_desc)}')


# using heapq library
import heapq

top_k = heapq.nlargest(2, freq.items(), key=lambda x:x[1])