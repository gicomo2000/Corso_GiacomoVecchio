import numpy as np
arr=np.arange(10,50)
print(arr)
print(arr.dtype)
arr=np.array(arr,dtype="float64")
print(arr.dtype)
print(arr.shape)


arr1d=np.random.randint(10,50,20)
print(arr1d)
print(arr1d[:10])
print(arr1d[-5:])
print(arr1d[5:15])
print(arr1d[2::3])
arr1d[5:10]=99
print(arr1d)
