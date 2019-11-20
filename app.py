#!/usr/bin/env python
# coding: utf-8

# In[27]:


#run 1st
import numpy as np 
import streamlit as st
luxury = 0
def model1(x):
    x = np.array(x)
    coeff = np.array([-5.449e-06, 0.0044, 0.0133, -0.0489, -0.0569, 0.3272])
    y = 11.3940+(np.sum(np.multiply(x, coeff)))
    return round(np.exp(y),0)


# In[ ]:


st.title('Used Car Price Estimator')
st.write('By Omar Qusos and Hamilton Chang')


# In[ ]:


mileage = st.slider('Max Mileage', 0, 80000, 0, 20)


# In[ ]:


city_mpg = st.slider('City MPG', 11, 54, 11, 1)


# In[ ]:


highway_mpg = st.slider('Highway MPG', 16, 50, 16, 1)


# In[ ]:


year = st.slider('Model Year', 2014, 2018, 2014, 1)


# In[ ]:


lux = st.checkbox('Luxury')
if lux:
    luxury = 1


# In[ ]:


x = [mileage, city_mpg, highway_mpg, year, luxury]


# In[32]:


#run 3rd

x.insert(1, 'replace me!')
x[0] = int(x[0])
x[1] = 1 if x[0] <= 7500 else 0
x[2] = int(x[2])
x[3] = int(x[3])
x[4] = 2019 - int(x[4])
x[5] = int(x[5])


# In[35]:


#run last for results
st.write('Your Car is worth Approximately')
st.write(model1(x))


# In[ ]:




