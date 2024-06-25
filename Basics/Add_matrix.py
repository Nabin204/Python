a=int(input("Enter the number of rows of first matrix:"))
b=int(input("Enter the number of columns of first matrix:"))
c=int(input("Enter the number of rows of second matrix:"))
d=int(input("Enter the number of columns of second matrix:"))

if(a!=c or b!=d):
    print("Addition is not possible since the order of two matrices is different.")
    exit(0)
def inp():
    M=[]
    for i in range(a):
        m=[]
        for j in range(b):
            m.append(int(input()))
        M.append(m)
    return M
def display(Z):
    for i in range (a):
        for j in range (b):
            print(Z[i][j],end=" ")
        print()
def add(A,B):
    S=[]
    for i in range(a):
        s=[]
        for j in range(b):
            s.append(A[i][j]+B[i][j])
        S.append(s)
    display(S)
            
print("Enter the elements of first matrix:")
A=inp()
print("Enter the elements of second matrix:")
B=inp()
print("The first matrix is:")
display(A)
print("The second matrix is:")
display(B)
print("The addition matrix is:")
add(A,B)