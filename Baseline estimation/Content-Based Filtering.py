
# coding: utf-8

# In[11]:

# All imports go here

import numpy as np
from numpy import genfromtxt
import csv


# In[ ]:

# Step 1 : Loading the User x Restaurant matrix.
# Y = np.transpose(genfromtxt('user_restr_mat_csv.csv', delimiter=','))
user_restr_arr = []
with open('user_restr_mat_csv.csv','r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        user_restr_arr.append(row)

Y = np.transpose(np.asarray(user_restr_arr))

# Checking shape of Y
print "Something"
print Y.shape


# In[6]:

# Step 2 : Loading the Restaurant feature matrix

X = genfromtxt('restr_feature_matrix.csv', delimiter=',')
print X.shape


# In[9]:

test_arr = np.asarray([[1,2,3,4,6,7,8,9],[4,5,6,4,6,7,8,9],[7,8,9,4,6,7,8,9]])
np.savetxt('test.csv',test_arr, delimiter=',')


# In[ ]:



