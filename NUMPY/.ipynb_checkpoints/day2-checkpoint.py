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
a=np.array([1,2,3,4,5])
print(a.dtype)

z=np.empty(9)
print(z)



