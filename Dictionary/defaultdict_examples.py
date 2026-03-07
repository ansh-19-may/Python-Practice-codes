# we have already use this pattern to check whether the key is present or not , but using defaultdict it automatically 
#create a default value with missing keys.
'''
here we check for key existence
freq = {}

for word in words:
    freq[word] = freq.get(word,0) + 1
'''    

# now we use defaultdict
'''
from collections import defaultdict
from collections import defaultdict

freq = defaultdict(int)

for word in words:
    freq[word] += 1
'''
# some defaultdict types are
# defaultdict(list) - when values are list
# defaultdict(float) - when values are float
# defaultdict(set) - when values are set()

from collections import defaultdict
text = "ai is fun ai"
words = text.split()

freq = defaultdict(int)

for word in words:
    freq[word] += 1

print(freq)    