
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt


# In[2]:

get_ipython().magic(u'matplotlib inline')


# In[3]:

import numpy as np


# In[4]:

graph = []
min_val = 100

for i in range(1,10000000):
    x = np.random.rand()
    y = np.random.rand()
    val1 = (x+y)/(x*1.0)
    val2 = x/(y*1.0)
    diff = abs(val1 - val2)
    if(diff<min_val):
        min_val = diff
        graph.append(val2)
        gr = val2


# In[5]:

print(gr)


# In[6]:

plt.plot(graph)
plt.show()


# In[7]:

plt.plot(graph)
plt.savefig("gr_converence.png")


# In[14]:

plt.plot(graph[16:])
plt.savefig("gr_converence_smaller.png")


# For more info visit:
#     https://www.mathsisfun.com/numbers/golden-ratio.html

# In[ ]:



