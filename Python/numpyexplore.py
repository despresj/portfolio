import numpy as np
from numpy.core.defchararray import array

a = np.array([1,2,3])

b = np.array([[9.0,8.0,7.0], [6.0,5.0,4.0]], dtype="int32")
a.ndim
a.shape
b.shape
b.ndim
a.dtype
b.dtype
a.itemsize

a = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])
a[1,5]

a[:,2]
a[0,1:6:2]

for apple in a:
    print(apple)

# 3d example 

b = np.array([[[1,2], [3,4]],[[5,6],[7,8]]])
b.ndim

b[0,1,:]
b[:,0,0]
b[:,1,0]

b[:,1,:] = [[9,9], [8,8]]

np.zeros((2,3,))

np.ones([4,2])

np.full([2,2], 99)

b = 
np.full([6,5], b)



b
# make an array the same shape as b
np.full_like(a, 6.5, dtype=float)
a = np.zeros([4,4])

p = np.random.randint(700, size = (3,3))
np.linalg.det(p)

np.identity(5)

arr = np.array([1,2,3])
r1 = np.repeat(arr, 3, axis=0)

r1

A = np.zeros([5,5])
A[2,2] = 9
A[:,0] = np.ones([1,5])
A[:,4] = np.ones([1,5])
A[0,:] = np.ones([1,5])
A[4,:] = np.ones([1,5])
A

out = np.ones([5,5])
z = np.zeros((3,3))
z[1,1] = 9
out[1:4,1:4] = z
out

a = np.array([1,2,3])
b = a

b[0] = 100
a

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
a

a = np.array([1,2,3,4])
print(a)
a + 2
a += 2
a / 2

b = np.array([1,2,3,1])

np.cos(a)

np.empty([3,3], float)



np.exp(a)

a = np.ones([5,1])

np.linalg.svd(a)

# Linear

a = np.full([2,3], 1)
b = np.full([3,2], 2)

np.matmul(a,b)
np.matmul(b,a)

c = np.identity(3)

np.linalg.det(c)

# Statistics

stats = np.array([[1,2,3],[4,5,6]])
np.min(stats, axis=0)

np.max(stats)
np.sum(stats)


before = np.array([[1,2,3,4],[5,6,7,8]])
before.reshape((2,2,2))
v1 = np.array([1,2,3,4])
v2 = np.array([4,5,6,7])

np.vstack([v1,v2,v2,v1])

np.hstack([v1, v2])

file = np.genfromtxt("eggs.txt", delimiter=",")
file.astype('int32')
file
file > 50

file[file>50]

a = np.array([1,2,3,4,5,6,7,8,9])
a[[1,2,6]]

np.any(file > 50, axis = 0)

np.all(file>50)

((file > 50) & (file < 100))

a = np.arange(1,31,1)
a = np.reshape(a, [6,5])

