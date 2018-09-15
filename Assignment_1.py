
# coding: utf-8

# <img src="assignment_1.png">

# In[1]:


from random import *
import numpy as np

unif_X_list=[]

for i in range(10):
    unif_X_list.append(random())  # 0부터 1 사이의 임의의 float
    
print(unif_X_list) # 10개의 X값
print("답: "+str(np.mean(unif_X_list))) # 10개의 X값에 대한 평균 ### 답

