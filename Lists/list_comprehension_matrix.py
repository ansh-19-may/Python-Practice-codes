# Outer loop --> rows 
# Inner loop --> cols


#how to create identity matrix using list comp
identity = [[1 if row == col else 0 for col in range(5)] for row in range(5)]
print(identity)



#how to print diagonal element 
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

diagonal = [data[i][i] for i in range(len(data))]
print(diagonal)


#How to print anti diagonal 
anti_diag = [data[i][len(data)- 1 - i] for i in range(len(data))]
print(anti_diag)

#How to create 3X3 matrix with 0
zero_matrix = [[0 for _ in range(3)]  for _ in range(3)]
print(zero_matrix)