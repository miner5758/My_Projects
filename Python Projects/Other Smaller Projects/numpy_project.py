import numpy as np

arr = np.array([1,2,3,4,5]) #1-D Array
#print(arr)
#print(type(arr))
#print(np.__version__)

arr2 = np.array((1,2,3,4,5))
#print(arr2)

arr3 = np.array(42) #0-D Array
#print(arr3)

arr4 = np.array([[1,2,3],[4,5,6]]) #2-D Array
#print(arr4)

arr5 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) #3-D Array
#print(arr5)

print(arr.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
