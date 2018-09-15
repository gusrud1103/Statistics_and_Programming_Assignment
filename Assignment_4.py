
# coding: utf-8

# <img src="assignment_4.png">

# In[5]:


import numpy as np
np.random.seed(10)
x = np.random.randint(0, 50, 1000)     # 0~49 range 1000개
y = x + np.random.normal(0, 10, 1000)  # x + 0~9 range 1000개
np.corrcoef(x, y)       # 상관계수: 0.82493013

