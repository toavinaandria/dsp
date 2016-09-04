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


# ## Exercises 2

# In[75]:

print("u+v equals "+str(u+v))


# In[76]:

print("u-v equals "+str(u-v))


# In[78]:

print("alpha*u equals "+str(alpha*u))


# In[92]:

print("u.v equals "+str(np.inner(u,v)))


# In[93]:

print("||u|| equals "+str(np.sqrt(np.sum(np.power(u,2)))))


# ## Exercises 3

# In[94]:

print("A+C is undefined")


# In[98]:

print("A-C.T equals \n"+str(A-C.T))


# In[100]:

print("C.T+3*D equals \n"+str(C.T+3*D))


# In[101]:

print("B*A equals \n"+str(B*A))


# In[102]:

print("B*A.T is undefined")


# In[103]:

print("B*C is undefined")


# In[105]:

print("C*B equals "+str(C*B))


# In[106]:

print("B**4 equals "+str(B**4))


# In[107]:

print ("A*A.T equals "+str(A*A.T))


# In[108]:

print("D.T*D equals "+str(D.T*D))



