#!/usr/bin/env python
# coding: utf-8

# Credit card validation

# In[1]:


def c_validation(a,b):
    c=[]
    for i in range(len(a)):
        a[i] *= 2
    for i in range(len(a)):
        if(a[i] > 9):
            x = str(a[i])
            sum1 = 0
            for j in x:           
                sum1 += int(j)       
            c.append(sum1)
        else:
            c.append(a[i])
    c.extend(b)
    d = sum(c)
    if(d%10 == 0):
        print('The credit card is valid')
    else:
        print('The credit card is invalid')
        


# In[2]:


validate = True
while validate:
    user_input = input('Enter the credit card number')
    if(user_input.isdigit()):
        list_1 = []
        list_2 = []
        list_3 = []
        for i in user_input:
            list_1.append(int(i))
        for i in range(len(list_1)-2,-1,-2):
            list_2.append(list_1[i])
        for i in range(len(list_1)-1,-1,-2):
            list_3.append(list_1[i])
        c_validation(list_2, list_3)
        validate = False
    else:
        print('enter a valid credit card')


# In[ ]:




