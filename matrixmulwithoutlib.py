A=[[1,2],[3,2]]
B=[[3,4],[4,3]]
result=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(B[i])):
        for k in range(len(A)):
            result[i][j]=result[i][j]+(A[i][k]*B[k][j])

for row in result:
    print(row)


