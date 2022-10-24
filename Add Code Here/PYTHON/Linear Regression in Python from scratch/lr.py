# LINEAR REGRESSION IN PYTHON (single features)

import numpy as np
from matplotlib import pyplot as plt

# Loading data:
data = np.genfromtxt("week_1.csv", delimiter=",")
data_x = data[:,0]
data_y = data[:,1]

# Constants:
prev_costfunc_y = -999
istrained = 0
alpha = 0.01
n = len(data_x)

# Initializint the parameters:
m = 1
c = 1

# Hypothesis Function:
def hypo_func(x):
    return m*x + c

# Cost Function
def cost_func():
    global istrained, prev_costfunc_y
    sum = 0

    for i in range(n):
        sum += (hypo_func(data_x[i]) - data_y[i])**2
    jy = (1/(2*n)) * sum

    if jy == prev_costfunc_y:
        istrained = 1
        return jy
    else:
        prev_costfunc_y = jy
        return jy

# Derivative cost_func(m ,c) w.r.t m:
def d_cost_func_m():
    sum = 0

    for i in range(n):
        sum += (hypo_func(data_x[i]) - data_y[i])*data_x[i]
    der_y = (1/n) * sum

    return der_y

# Derivative cost_func(m ,c) w.r.t c:
def d_cost_func_c():
    sum = 0

    for i in range(n):
        sum += (hypo_func(data_x[i]) - data_y[i])
    der_y = (1/n) * sum

    return der_y

# Gradient Descent Function:
def update_m_c():
    global m, c
    temp1 = m - alpha*d_cost_func_m()
    temp0 = c - alpha*d_cost_func_c()
    m = temp1
    c = temp0

# Training:
for i in range(10**6):
    update_m_c()
    print("Pass:", i)
    print("Cost function value:", cost_func())
    print("m = {}, c = {}".format(m, c))
    print()
    if istrained:
        print("Model fully trained at pass = {} with alpha = {}".format(i-1, alpha))
        break

# Overtrained data result (took few mins):
'''Pass: 683681
   Cost function value: 4.4769713762249435
   m = 1.1930283822835892 , c = -3.895728500632679
   Model fully trained at pass = 683681 with alpha = 0.0001'''

# Good trained data result (took around 6 sec):
'''Pass: 8300
   Cost function value: 4.476971375976421
   m = 1.1930332734380062 , c = -3.895777187803569
   Model fully trained at pass = 8299 with alpha = 0.01'''

predict_y = list(map(hypo_func, data_x))

# plotting the prediction:
#plt.plot([min(data_x), max(data_x)], [min(data_y), max(data_y)], label='Original Plot')
plt.scatter(data_x, data_y, s=5)
plt.plot(data_x, predict_y, label='Prediction Plot', color='red')
plt.xticks([i for i in range(5, int(max(data_x))+1, 2)])
plt.legend()
plt.xlabel('X Data (Av. no. of rooms) -->')
plt.ylabel('Y Data (Price of house in 100k) -->')
plt.title('Linear Regression in Python')

plt.show()
