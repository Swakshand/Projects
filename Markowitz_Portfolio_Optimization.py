#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(1234)

#Q1) begins here


# In[94]:


df = pd.read_excel('C:\\Users\\Dell\\OneDrive\\Desktop\\2021ME21090_Swakshand_prasad_1\\stocks_data.xlsx')
df


# In[95]:


stock1_mean = df['stock1'].mean()
stock2_mean = df['stock2'].mean()
stock3_mean = df['stock3'].mean()
stock4_mean = df['stock4'].mean()
stock5_mean = df['stock5'].mean()


# In[85]:


mean_array = np.array([stock1_mean, stock2_mean, stock3_mean, stock4_mean, stock5_mean])


# In[5]:


returns = df.pct_change()


# In[6]:


meanreturns = returns.mean()


# In[57]:


covmatrix = returns.cov()


# In[49]:


l = []

max_list = [0]
iterations = 10
for i in range(iterations):
    w = np.random.rand(5)
    sum_of_w = sum(w)
    for i in range(5):
        w[i] = w[i]/sum_of_w
        
    ww=np.matrix(w)
    w_t = ww.T
    u = np.matrix(mean_array)
    num1 = u.dot(w_t)
    temp = ww.dot(covmatrix)
    num2 = temp.dot(w_t)
    num2 = 0.2 * num2
    profit = num1 - num2
    if(profit > max_list[0]):
        max_list[0] = profit
        max_w = ww

l.append(max_list[0])
print(max_list[0])
print(ww)


max_list = [0]
iterations = 100
for i in range(iterations):
    w = np.random.rand(5)
    sum_of_w = sum(w)
    for i in range(5):
        w[i] = w[i]/sum_of_w
        
    ww=np.matrix(w)
    w_t = ww.T
    u = np.matrix(mean_array)
    num1 = u.dot(w_t)
    temp = ww.dot(covmatrix)
    num2 = temp.dot(w_t)
    num2 = 0.2 * num2
    profit = num1 - num2
    if(profit > max_list[0]):
        max_list[0] = profit
        max_w = ww

l.append(max_list[0])
print(max_list[0])
print(ww)


max_list = [0]
iterations = 1000
for i in range(iterations):
    w = np.random.rand(5)
    sum_of_w = sum(w)
    for i in range(5):
        w[i] = w[i]/sum_of_w
        
    ww=np.matrix(w)
    w_t = ww.T
    u = np.matrix(mean_array)
    num1 = u.dot(w_t)
    temp = ww.dot(covmatrix)
    num2 = temp.dot(w_t)
    num2 = 0.2 * num2
    profit = num1 - num2
    if(profit > max_list[0]):
        max_list[0] = profit
        max_w = ww

l.append(max_list[0])
print(max_list[0])
print(ww)


max_list = [0]
iterations = 10000
for i in range(iterations):
    w = np.random.rand(5)
    sum_of_w = sum(w)
    for i in range(5):
        w[i] = w[i]/sum_of_w
        
    ww=np.matrix(w)
    w_t = ww.T
    u = np.matrix(mean_array)
    num1 = u.dot(w_t)
    temp = ww.dot(covmatrix)
    num2 = temp.dot(w_t)
    num2 = 0.2 * num2
    profit = num1 - num2
    if(profit > max_list[0]):
        max_list[0] = profit
        max_w = ww
        
l.append(max_list[0])
print(max_list[0])
print(ww)


max_list = [0]
iterations = 100000
for i in range(iterations):
    w = np.random.rand(5)
    sum_of_w = sum(w)
    for i in range(5):
        w[i] =w[i]/sum_of_w
        
    ww=np.matrix(w)
    w_t = ww.T
    u = np.matrix(mean_array)
    num1 = u.dot(w_t)
    temp = ww.dot(covmatrix)
    num2 = temp.dot(w_t)
    num2 = 0.2 * num2
    profit = num1 - num2
    if(profit > max_list[0]):
        max_list[0] = profit
        max_w = ww

l.append(max_list[0])
print(max_list[0])
print(ww)


max_list = [0]
iterations = 500000
for i in range(iterations):
    w = np.random.rand(5)
    sum_of_w = sum(w)
    for i in range(5):
        w[i] = w[i]/sum_of_w
        
    ww=np.matrix(w)
    w_t = ww.T
    u = np.matrix(mean_array)
    num1 = u.dot(w_t)
    temp = ww.dot(covmatrix)
    num2 = temp.dot(w_t)
    num2 = 0.2 * num2
    profit = num1 - num2
    if(profit > max_list[0]):
        max_list[0] = profit
        max_w = ww

l.append(max_list[0])
print(max_list[0])
print(ww)

print(l)


# In[63]:


#Q2) begins here

from scipy.optimize import minimize


# In[88]:


def objective(ww, mean_array, covmatrix):
    return -((np.dot(mean_array, ww)) - (0.2 * (np.dot(ww.T, np.dot(covmatrix, ww)))))
n = len(mean_array)
guesses = np.ones(n) / n #we assume 0.2 for every stock in the begenning
cons = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bound = (0, 1)
total_bounds = ([bound]*n)
optimal_ans = minimize(objective, guesses, args=(mean_array, covmatrix), bounds=total_bounds, constraints=cons)
optimal_distribution = optimal_ans.x
optimal_returns_obtained = -optimal_ans.fun

print('The optimal parameter values:')
print(optimal_distribution)
print(optimal_returns_obtained)


# In[59]:


percentage = []
for i in range(6):
    num = (optimal_portfolio_return - l[i]) / optimal_portfolio_return
    num = num*100
    percentage.append(num.item())
    


# In[87]:


plt.ylabel('y axis')
plt.xlabel('x axis')
plt.title('percentage difference vs. no. of iterations of Monte Carlo Simulations')
plt.plot(percentage, color='r', marker='o')
plt.show()