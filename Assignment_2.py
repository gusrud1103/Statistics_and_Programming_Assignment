
# coding: utf-8

# <img src="assignment_2.png">

# In[3]:


import numpy as np
U=np.random.uniform(0,1,10)
X1=-np.log(1-U); X2=-np.log(U)
rand_expo1=np.exp(-X1); rand_expo2=np.exp(-X2)
print(np.mean(rand_expo1)); print(np.mean(rand_expo2))

