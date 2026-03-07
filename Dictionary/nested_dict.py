# Create a nested dictionary

data = [
("Ali","math",90),
("Ali","physics",80),
("Sara","math",95)
]

result = {}

for name,sub,score in data:
    if name not in result:
        result[name] = {}
    result[name][sub] = score

print(result)


'''
Similar example

data =[
("user1","movie1",5),
("user1","movie2",4),
("user2","movie1",3)
]

res = {}

for user,mov,rating in data:
    if user not in res:
       res[user] = {}
    res[user][mov] = rating

print(res)    

'''