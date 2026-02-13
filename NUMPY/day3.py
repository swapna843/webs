import numpy as np

# arra1=np.array([1,2,3,4])
# arra2=np.array([5,6,7,8])
# # arra3=np.vstack((arra1,arra2)) #y axis
# # print(arra3)

# # arra4=np.hstack((arra1,arra2)) #x axis
# # print(arra4)

# arra5=np.concatenate((arra1,arra2))
# print(arra5)


# arra6=np.array([[1,2,3,4],[5,6,7,8]])
# arra7=np.array([[9,10,11,12],[13,14,15,16],[17,18,19,20]])

# # arra8=np.vstack((arra6,arra7))
# # print(arra8)
# # arrra9=np.hstack((arra6,arra7))
# # print(arrra9)

# arra10=np.concatenate((arra6,arra7))
# print(arra10)

# a1=np.vsplit(arra10,5)
# print(a1)
# a2=np.hsplit(arra10,2)
# print(a2)

# a3=np.vsplit(arra6,2)
# print(a3)
# a4=np.vsplit(arra7,2)#not possible
# a5=np.vsplit(arra7,3)

# a6=np.hsplit(arra6,2)
# a7=np.hsplit(arra6,4)
# a8=np.hsplit(arra6,3)#not possible



#spliting :
# 1.main array
# 2.no of new array
# 1.vertically :vsplit
# 2.horizentally:hsplit


# a1=np.vsplit(arra10,2)
# print(a1)

a1=np.array([[1,2,3,4],[5,6,7,8]])
print(a1)
a2=np.vsplit(a1,2)
print(a2)
a3=np.hsplit(a1,2)
print(a3)


