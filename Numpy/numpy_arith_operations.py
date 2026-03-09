'''
we can perform below operation on numpy array 

+    : Addition 
-    : Substraction 
*    : Multiplication 
/    : Division  
**   : Exponential 
//   : Floor Division (round the result to closest integer)
%    : Modulus

without iterating any loops 
'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(f'Addition  {arr + 2}')
print(f'Substraction  {arr - 9}')
print(f'Multiplication  {arr * 5}')
print(f'Division  {arr / 2}')
print(f'Exponential  {arr ** 2}')
print(f'Floor Division  {arr // 4}')
print(f'Modulus  {arr % 6}')



'''
O/P :

Addition  [12 22 32 42 52]
Substraction  [ 1 11 21 31 41]
Multiplication  [ 50 100 150 200 250]
Division  [ 5. 10. 15. 20. 25.]
Exponential  [ 100  400  900 1600 2500]
Floor Division  [ 2  5  7 10 12]
Modulus  [4 2 0 4 2]

'''