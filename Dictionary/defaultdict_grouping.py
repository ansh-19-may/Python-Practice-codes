'''
Grouping appears in:
log aggregation
dataset batching
recommender systems
graph adjacency lists4

'''

from collections import defaultdict

students = [
("Ali","Math"),
("Sara","Physics"),
("John","Math"),
("Emma","Physics")
]

result = defaultdict(list)

for name,subject in students:
    result[subject].append(name)

print(result)