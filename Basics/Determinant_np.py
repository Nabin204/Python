#Determinant of 2*2 Matrix

import numpy as np
arr1=np.array([[1,2],[3,4]])
determinant1 = np.linalg.det(arr1)
print(determinant1)


#Determinant of 3*3 Matrix

arr2=np.array([[2,5,8],[2,5,1],[0,4,9]])
determinant2 = np.linalg.det(arr2)
print(determinant2)


#Determinant of entered matrix

n=int(input("Enter the order of the square matrix:"))
print("Enter the elements of matrix in order:")
arr3=[]
for i in range(n):
    lst=[]
    for j in range(n):
        lst.append(int(input()))
    arr3.append(lst)
arr3 = np.array(arr3)
determinant3=np.linalg.det(arr3)
print("The determinant of entered matrix is:",determinant3)