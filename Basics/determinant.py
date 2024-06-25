import math
matrix=[]
determinant=0
print("Enter the elements of matrix in rowwise:")
for i in range (3):
    a=[]
    for j in range (3):
        a.append(int(input()))
    matrix.append(a)
def display33(A):
 for i in range (3):
    for j in range (3):
        print(A[i][j],end="  ")
    print()
print("The entered matrix is:\n")
def display22(B):
    for i in range (2):
     for j in range (2):
        print(B[i][j],end="  ")
     print()
display33(matrix)
def det(C):
    return C[0][0]*C[1][1]-C[0][1]*C[1][0]
for i in range (3):
    M=[]
    for j in range (3):
        m=[]
        for k in range (3):
         if(j!=0 and k!=i):
          m.append(matrix[j][k])
        M.append(m)
    M.pop(0)
    determinant=determinant+pow(-1,i)*det(M)*matrix[0][i]
print("The determinant of given matrix is:",determinant)