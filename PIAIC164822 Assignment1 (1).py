#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
a=np.array([1,2,3,4])
a


# In[ ]:


b=np.array([[5,6,7,8],[9,10,11,12]])
b


# In[ ]:


array([[ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
b.shape


# In[ ]:


b.shape=(1,2,4)
b


# In[ ]:


b.shape=(2,1,4)
b


# In[ ]:


y=b.reshape((2,2,1,2))
y


# In[ ]:


f=np.array([1,2,3,4,5,6,7,8,9,10])
f


# In[ ]:


f.shape=(5,2)
f


# In[ ]:


f.shape=(2,5)
f


# In[ ]:


c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
c


# In[ ]:


get_ipython().run_line_magic('pinfo', 'g.shape')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'g.shape')


# In[ ]:


h=np.random.randint(10,size=5)
h


# In[ ]:


g=np.random.randint(55,size=10)
g


# In[ ]:


g[0]


# In[ ]:


g[-1]


# In[ ]:


g[5]


# In[ ]:


g>10


# In[ ]:


g<30


# In[ ]:


g*2


# In[ ]:


g/2


# In[ ]:


g[0:3]


# In[ ]:


g*g


# In[ ]:


import numpy as np
a=np.zeros(3)
a


# In[ ]:


a=np.zeros((5,5,5))
a


# In[ ]:


type(a)


# In[ ]:


type(a[0])


# In[ ]:


import numpy as np
y=np.array([5,6,3,5,3,2])
y


# In[ ]:


y@y


# In[ ]:


a=np.array([5,9,3,4])
a


# In[ ]:


a.cumsum()


# In[ ]:


a.cumprod()


# In[ ]:


a.sum()


# In[ ]:


b=a>5
b


# In[ ]:


v=np.array([5,4,3,24,55,9])
v


# In[ ]:


v<5


# In[ ]:


v.any()


# In[ ]:


v.all()


# In[ ]:


v.sort()
v


# In[ ]:


x=np.array([3,2,5,5,7,8,7,7,0,55,5,5])
x


# In[ ]:


c=np.unique(x)
c


# In[ ]:


a=np.array([1,2,3,4,5,6,7,8])
b=np.array([5,4,3,6,2,8,6,7])
np.where(a>b,a,b)


# In[ ]:


result=np.array([55,44,32,11,67])
np.where(result>40,"pass","fail")


# In[ ]:


import numpy as np
f=np.array([5,3,5,66,3,5,4,6,2])
f


# In[ ]:


f.ndim
1


# In[ ]:


f.size


# In[ ]:


f.shape


# In[ ]:


a.ndim


# In[ ]:


a.size


# In[ ]:


a.shape


# In[ ]:


a=np.arange(15).reshape(3,5)
a


# In[ ]:


b=np.arange(55).reshape(11,5)
b


# In[ ]:


import numpy as np
h=np.arange (4,77)
h


# In[ ]:


h.ndim


# In[ ]:


h.size


# In[ ]:


import numpy as np
a=["asil","basil","faisal"]
b=["tariq","shah","bilal"]


# In[ ]:


np.save("sub1.npy",a)
l1=np.load("sub1.npy")
l1


# In[ ]:


np.savez("sub2",a=a,b=b)
l2=np.load("sub2.npz")
l2


# In[ ]:


a


# In[ ]:


b


# In[ ]:


x=np.array([1,2,3])
y=np.array([4,5,6])
np.dot(x,y)


# In[ ]:


import numpy as np
a=np.array([1,2,3,4,5,6,8])
a


# In[ ]:


a.max()


# In[ ]:


a.min()


# In[ ]:


a.sum()


# In[ ]:


b=np.arange(12).reshape(3,4)
b


# In[ ]:


b.sum(axis=0)


# In[ ]:


b.sum(axis=1)


# In[1]:


import numpy as np
t=np.arange(1000)
t
 


# In[2]:


t[2:6]


# In[3]:


t[0:6:2]=1000


# In[4]:


t[::-1]


# In[ ]:




