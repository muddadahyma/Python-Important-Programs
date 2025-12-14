A=[[6,2,1],[4,1,2],[9,2,1]]
B=[[1,2,3],[4,6,7],[3,7,4]]
C=[[0,0,0],[0,0,0],[0,0,0]]
print("print A matrix")
print(A)
print("print B matrix")
print(B)
for i in range(3):
    for j in range(3):
        C[i][j]=A[i][j]+B[i][j]
print("addition of A,B matrix")
for row in C:
    print(row)