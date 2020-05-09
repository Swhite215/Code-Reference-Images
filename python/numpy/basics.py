import numpy as np
import math

# Create An Array #1
a = np.arange(15).reshape(3, 5)

# Print Basic Information of Array
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a)

# Create an Array #2
b = np.array([2,3,4])
print(b)

# Create an Array #3
c = np.array([(1.5, 2, 3), (4, 5, 6)])
print(c)

# Create an Array #4
d = np.array([[1,2], [3,4]], dtype=complex)
print(d)

# Create an Array #5
e = np.zeros((3, 4))
print(e)

# Create an Array #6
f = np.ones((2,3,4), dtype=np.int16 )
print(f)

# Create an Array #7 _ Values Can Vary
g = np.empty((2,3))
print(g)

# Create a Sequence of Numbers - (Start, Stop, Increment)
seq = np.arange(10, 30, 5)
print(seq)

seq2 = np.arange(0, 100, 10)
print(seq2)

# Create A Sequence of Floating Numbers
seq3 = np.linspace(0, 2, 13)
print(seq3)

# Print 1D Array - Last Axis Left to Right, Second to Last Top to Bottom, Rest Top to Bottom
h = np.arange(6)
print(h)

# Print 2D Array
i = np.arange(12).reshape(4,3)
print(i)

# Print3D Array
j = np.arange(24).reshape(2, 3, 4)
print(j)

# IMPORTANT _ BELOW ARE NOT EQUAL
k = np.arange(4149600).reshape(798, 1300, 4)
print(k)

l = np.arange(1037400).reshape(798, 1300)
print(l)

# Basic Operations - Subtraction - Each Element of N - Each Element of N
m = np.array([20,30,40,50])
n = np.arange(4)
o = m - n
print(m)
print(n)
print(o)

# Basic Operations - Multiplication - Each Element of N * #
p = m * 2
print(p)

# Basic Operations - Division - Each Element of N / #
q = m / 2
print(q)

# Basic Operations - Comparison
r = m < 35
print(r)

# Matrix Operations - Element Wise - 60 x100, 70 * 110, etc...
s = np.array([[60, 70], [80, 90]])
t = np.array([[100, 110], [120, 130]])
print(s)
print(t)
print(s * t)

# Matrix Operations - Matrix Product
print(s @ t)

# In Place Operations
u = np.ones((2, 3), dtype=int)
u *= 3
print(u)

# Upcasting - Resulting Array is More General or Precise One
v = np.ones(3, dtype=np.int32)
w = np.linspace(0, math.pi, 3)
print(v)
print(w)

print(v * w)

# Unary Operations
x = np.arange(10)
print(x)
print(x.sum())
print(x.min())
print(x.max())

# Unary Operations By Axis
y = np.arange(12).reshape(3,4)
print(y)
print(y.sum(axis=0))
print(y.sum(axis=1))

# Universal Functions
z = np.arange(3)
print(z)
print(np.exp(z))
print(np.sqrt(z))

# Indexing
aa = np.arange(10)**3
print(aa)
print(aa[2])

# Slicing - [Start:End]
print(aa[2:5])

# Slicing - [Start:End:Increment
print(aa[:6:2])
print(aa[:len(aa):3])

# Slicing - Reverse
print(aa[::-1])

# Iterating
for i in aa:
    print(i)

# Indexing - Pairs bb[row,column] or bb[startRow:endRow,startColumn:endColumn]
def f(x,y):
    print(10 * x + y)
    return 10*x+y

bb = np.fromfunction(f, (5,4), dtype=int)
print(bb)
print(bb[2,3]) # 3rd Row - 4th Cell
print(bb[0:5,1]) # 0 - 5th Value of Second Column
print(bb[:,1]) # All Values of Second Column
print(bb[1:3, :]) # From 2nd to 3rd Row Every Column
print(bb[3:5, 2]) # From 4th to 5th Row Every Third Column
print(bb[:-3]) # Every Row Besides the Last Three
print(bb[:-1]) # Every Row Besides the Last
print(bb[:,:2]) # Every Row, Values from Column One and Two
print(bb[:,-1]) # Every Row, Values from the Last Column

# Iterating - Rows
for row in bb:
    print(row)

# iterating - Every Element
for element in bb.flat:
    print(element)

print(k[0])
# Errors

# Common Error #1 - Calling .array() with multiple arguments
# b = np.array(1,2,3)

