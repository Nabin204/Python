#Inverse of 2*2 Matrix

import numpy as np
arr1=np.array([[1.5,2],[3,4]])
det1=np.linalg.det(arr1)
if(det1!=0):
    inv_matrix1 = np.linalg.inv(arr1)
    print(inv_matrix1)
else:
    print("The inverse of first matrix does not exist as its determinant is zero.\n")


#Inverse of 3*3 Matrix

arr2=np.array([[2,5,8],[2,5,1],[0,4,9]])
det2=np.linalg.det(arr2)
if(det2!=0):
    inv_matrix2 = np.linalg.inv(arr2)
    print(inv_matrix2)
else:
    print("The inverse of second matrix does not exist as its determinant is zero.\n")


#Inverse of entered matrix

n=int(input("\nEnter the order of the square matrix:"))
print("Enter the elements of matrix in order:")
arr3=[]
for i in range(n):
    lst=[]
    for j in range(n):
        lst.append(int(input()))
    arr3.append(lst)
arr3 = np.array(arr3)
det3=np.linalg.det(arr3)
if(det3!=0):
    inv_matrix3=np.linalg.inv(arr3)
    print("\nThe inverse of entered matrix is:\n",inv_matrix3)
else:
    print("The inverse of entered matrix does not exist as its determinant is zero.") 