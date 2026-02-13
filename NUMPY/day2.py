import numpy as np 
import time

# size=6000000
# l1=range(size)
# l2=range(size)

# a1=np.arange(size)
# a2=np.arange(size)

# start=time.time()
# result = [(x + y) for x, y in zip(l1, l2)] 
# print("python list took time ",(time.time() - start)*1000)

# start=time.time()
# result=a1+a2
# print("numpy array  took time ",(time.time()-start)*1000)

# a=[1,2,3,4,5]
# a=np.array([1,2,3,4,5])
# print(a.dtype)

# z=np.empty(9)
# print(z)

# aray1=np.zeros(6)
# print(aray1)

# arra2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arra2.sum(axis=1)) #axis 1=1+5+9 axis 0=1+2+3+4

# 10/02/2026
# sum(),sqrt(),power(),dot(),ravel()

#indexing and slicing of numpy array
a2=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(a2[0:2,0:2])
print(a2[1:,2:])
print(a2[:,2:])
print(a2[0,1])



# arr1=np.empty([3,2],dtype=float,order='F')
# print(arr1)

# arra2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arra2.sum(axis=1))


# arra3=np.array([1,2,3,4])
# arra4=np.array([5,6,7,8])

# # arra5=arra3+arra4
# # print(arra5)

# d1=np.dot(arra3,arra4)
# print(d1)

# p1=np.power(arra3,arra4)
# print(p1)
#boolean indexing 
# a3=np.array([[4,2,5,4,5],[16,7,8,49,10],[141,124,143,144,15]])
# print(a3[a3>5])
# print(a3>10)

#import numpy as np
arr1= np.empty([3, 2], dtype=float, order='F')
# print(arr1)

arr2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr2.sum())
print(arr2.sum(axis=1))
print(arr2.sum(axis=0))

# n1 = np.sqrt(arr2)
# print(n1)

# print(arr2[2][3]+10)
# print(arr2[2][3]-10)
# print(arr2[2][3]*10)
# print(arr2[2][3]/10)

arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

# arr5 = arr3 + arr4
# print(arr5)



#sir

d1 = np.dot(arr3, arr4)
# print(d1)

p1 = np.power(arr4, arr3)
# print(p1)

flatArr1 = np.ravel(arr2)
# print(flatArr1)
newArr = flatArr1.reshape(4,3)
# print(newArr)

arr5 = np.array([[1,2,3], [4,5,6], [7,8,9]])
flatArr2 = np.ravel(arr5)
# print(flatArr2)



# Indexing and Slicing in NumPy
# 1. Single Dimensional Array
a1 = np.array([1,2,3,4,5])
# print(a1[2])
# print(a1[-1])
# print(a1[2:4])
# print(a1[2:])
# print(a1[:4])

# 2. Multidimensional Array
a2 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(a2[1])
# print(a2[1][2])
# print(a2[0,1])
# print(a2[0:2, 1:4])
# print(a2[1:, 2:])
# print(a2[:, 2:])

# 3. Boolean Indexing
a3 = np.array([[4,2,5,4,5], [16,7,8,49,10], [141,124,143,144,15]])
# print(a3[a3>5])
# print(a3> 10)

# Iteration in Numpy
# a3 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# for i in a3:
#     print(i)
#     for j in i:
#         print(j)