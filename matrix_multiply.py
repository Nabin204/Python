a=int(input("Enter the number of rows of first matrix:"))
b=int(input("Enter the number of columns of first matrix:"))
c=int(input("Enter the number of rows of second matrix:"))
d=int(input("Enter the number of columns of second matrix:"))

if(b!=c):
    print("The matrix multiplication is not possible since the number of columns of first matrix is equal to the number of rows of second matrix.")
    exit(0)
    
def inp(x,y):
    M=[]
    for i in range (x):
        m=[]
        for j in range (y):
            m.append(int(input()))
        M.append(m)
    return M
def display(x,y,M):
    for i in range (x):
        for j in range (y):
            print(M[i][j],end=" ")
        print()
def multiply(A,B):
    M=[]
    for i in range (a):
        m=[]
        for j in range (d):
            p=0
            for k in range(b):
              p=p+A[i][k]*B[k][j]  
            m.append(p)
        M.append(m)
    display(a,d,M)
print("Enter the elements of first matrix:")
X=inp(a,b)
print("Enter the elements of second matrix:")
Y=inp(c,d)
print("The first matrix is:")
display(a,b,X)
print("The second matrix is:")
display(c,d,Y)
print("The multiplication of these matrix is:")
multiply(X,Y)

            