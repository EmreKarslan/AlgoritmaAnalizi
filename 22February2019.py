#!/usr/bin/env python
# coding: utf-8

# In[17]:


def findmax(my_list):
    max=my_list[0]
    s=0
    for i in range(len(my_list)):
        if(max<my_list[i]):
            max=my_list[i]
            s=i
    return max,s
list_1=[1,2,3,4,5,56,71,77,566,234,377,5442,2678]
findmax(list_1)


# In[30]:


import random
def generate_numbers(n):
    numbers=[]
    for i in range(n):
        s=random.randint(0,1000000000)
        numbers.append(s)
    return numbers
n_s=generate_numbers(1000000)
n_s


# In[29]:


findmax(n_s)


# In[31]:


def recursive_fib(n):
    if(n<2):
        return n
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)


# In[39]:


import time
start=time.time()
for i in range(35):
    
    s=recursive_fib(i)
    print(s)
end=time.time()
print(end-start)


# In[43]:


start=time.time()
for i in range(41):
    
    s=recursive_fib(i)
    print(s)
end=time.time()
print(end-start)


# In[1]:


def power_1(m,n):
    t=1
    global sayac
    for i in range(n):
        sayac=sayac+1
        t=t*m
    return t,sayac


# In[41]:


def call_report(x,y):
    global sayac
    sayac=0
    r=power_1(x,y)
    print(x," üzeri",y," degeri",r[0],"çağrım sayısı : ",r[1])


# In[38]:


def power_2(x,n):
    global sayac
    sayac=sayac+1
    if(n==0):
        return 1,sayac
    elif(n==1):
        return x,sayac
    elif(n%2==0):
        return (power_2(x*x,n//2)[0],power_2(x*x,n//2)[1])
    elif(n%2==1):
        return (power_2(x*x,n//2)[0]*x,power_2(x*x,n//2)[1])


# In[39]:


def call_report_recursive(x,y):
    global sayac
    sayac=0
    r=power_2(x,y)
    print(x," üzeri",y," degeri",r[0],"çağrım sayısı : ",r[1])


# In[40]:


call_report_recursive(2,6)


# In[42]:


call_report(2,5)


# In[ ]:




