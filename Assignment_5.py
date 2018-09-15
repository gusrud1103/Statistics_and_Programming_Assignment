
# coding: utf-8

# <img src="assignment_5.png">

# In[6]:


from scipy.special import gamma, beta  # 주의: from scipy.stats import gamma에는 gamma function없음
a=3; b=7
f=gamma(a)*gamma(b); g=gamma(a+b)
print(f/g)             # 답: 0.003968253968253968
print(beta(a, b))      # 답: 0.003968253968253968

