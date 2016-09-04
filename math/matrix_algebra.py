# Matrix Algebra


# coding: utf-8

# In[72]:

import numpy as np

# Matrix exercises

# Declare variables and matrices
A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix([6,2,-3,5])
v = np.matrix([3,5,-1,4])
w = np.matrix([[1],[8],[0],[5]])
alpha = 6

# Display matrices
matrices = {"A":A,"B":B,"C":C,"D":D,"u":u,"v":v,"w":w}

for name,matrix in matrices.iteritems():
    print(name+" ="+"\n"+str(matrix)+"\n")


# ## Exercises 1

# In[74]:

for name,matrix in matrices.iteritems():
    print(name+"'s is a "+str(matrix.shape)+" matrix")

"""
A's is a (2, 3) matrix
C's is a (3, 2) matrix
B's is a (2, 2) matrix
D's is a (2, 3) matrix
u's is a (1, 4) matrix
w's is a (4, 1) matrix
v's is a (1, 4) matrix
"""

# ## Exercises 2

# In[75]:

print("u+v equals "+str(u+v))
# u+v equals [[ 9  7 -4  9]]

# In[76]:

print("u-v equals "+str(u-v))
# u-v equals [[ 3 -3 -2  1]]


# In[78]:

print("alpha*u equals "+str(alpha*u))
# alpha*u equals [[ 36  12 -18  30]]


# In[92]:

print("u.v equals "+str(np.inner(u,v)))
# u.v equals [[51]]

# In[93]:

print("||u|| equals "+str(np.sqrt(np.sum(np.power(u,2)))))
# ||u|| equals 8.60232526704

# ## Exercises 3

# In[94]:

print("A+C is undefined")


# In[98]:

print("A-C.T equals \n"+str(A-C.T))
"""
A-C.T equals
[[-4 -7 -3]
 [ 3  6  4]]
"""

# In[100]:

print("C.T+3*D equals \n"+str(C.T+3*D))
"""
C.T+3*D equals
[[14  3  3]
 [ 2  7  9]]
 """

# In[101]:

print("B*A equals \n"+str(B*A))
"""
B*A equals
[[-1 -5 -1]
 [ 2  7  4]]
"""

# In[102]:

print("B*A.T is undefined")


# In[103]:

print("B*C is undefined")


# In[105]:

print("C*B equals \n"+str(C*B))
"""
C*B equals
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
"""

# In[106]:

print("B**4 equals \n"+str(B**4))
""""
B**4 equals
[[ 1 -4]
 [ 0  1]]
"""

# In[107]:

print ("A*A.T equals \n"+str(A*A.T))
"""
A*A.T equals
[[14 28]
 [28 69]]
"""
# In[108]:

print("D.T*D equals \n"+str(D.T*D))

"""
D.T*D equals
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
"""



