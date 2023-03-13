import numpy as np

# Create a null vector of size 10 but the fifth value which is 1
def null_vector(n):
    a = np.zeros(n)
    a[4] = 1
    return a

print(null_vector(10))

# Create a vector with values ranging from 10 to 49
v = np.arange(10, 50, 1)
print(v)

# Reverse a vector (first element becomes last)
invert_v = v[::-1]
print(invert_v)

# Create a 3x3 matrix with values ranging from 0 to 8
m = np.arange(0,9,1).reshape(3,3)
print(m)

# Find indices of non-zero elements from [1,2,0,0,4,0]
v = [1, 2, 0, 0, 4, 0]
v = np.array(v)
v_non_zero = np.nonzero(v)
print(v_non_zero)

# Create a random vector of size 30 and find the mean value
r = np.random.rand(30)
print(r)
print(r.mean())

# Create a 2d array with 1 on the border and 0 inside
d = np.ones((5, 5))
d[1:-1, 1:-1] = 0
print(d)

# Create a 8x8 matrix and fill it with a checkerboard pattern
schach = np.zeros((8, 8))
schach[0::2, ::2] = 1
schach[1::2, 1::2] = 1

print(schach)

# Create a checkerboard 8x8 matrix using the tile function
s = np.array([[1, 0],[0, 1]])
h = np.tile(s, (4, 4))

print(h)

# Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
mask = np.arange(3, 10, 1)
Z = np.delete(Z, mask)
print(Z)

# Create a random vector of size 10 and sort it
Z = np.random.random(10)
print(Z)
Z = np.sort(Z)
print(Z)

# Consider two random array A anb B, check if they are equal
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.equal(A, B)
print(equal)

# How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.astype('float32')
print(Z.dtype)

# How to get the diagonal of a dot product?
A = np.arange(9).reshape(3, 3)
B = A + 1
C = np.dot(A, B)
D = np.diag(C)
print(C)
print(D)