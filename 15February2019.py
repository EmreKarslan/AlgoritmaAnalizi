
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


# In[ ]:



