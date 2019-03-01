#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


import random
def generate_numbers(n):
    numbers=[]
    for i in range(n):
        s=random.randint(0,1000000000)
        numbers.append(s)
    return numbers
n_s=generate_numbers(1000000)
n_s


# In[3]:


findmax(n_s)


# In[4]:


def recursive_fib(n):
    if(n<2):
        return n
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)


# In[5]:


import time
start=time.time()
for i in range(35):
    
    s=recursive_fib(i)
    print(s)
end=time.time()
print(end-start)


# In[6]:


start=time.time()
for i in range(41):
    
    s=recursive_fib(i)
    print(s)
end=time.time()
print(end-start)


# In[7]:


def power_1(m,n):
    t=1
    global sayac
    for i in range(n):
        sayac=sayac+1
        t=t*m
    return t,sayac


# In[8]:


def call_report(x,y):
    global sayac
    sayac=0
    r=power_1(x,y)
    print(x," üzeri",y," degeri",r[0],"çağrım sayısı : ",r[1])


# In[9]:


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


# In[10]:


def call_report_recursive(x,y):
    global sayac
    sayac=0
    r=power_2(x,y)
    print(x," üzeri",y," degeri",r[0],"çağrım sayısı : ",r[1])


# In[11]:


call_report_recursive(2,6)


# In[12]:


call_report(2,5)


# In[57]:


import ctypes

class DynamicArray:
    #A dynamic array class akin to a simplified Python list.”””
    def __init__(self):
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A=self._make_array(self._capacity) # low-level array

    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0<=k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        print(obj,"Listeye Eklendi")
        self._n+=1
    
    def _resize(self,c):
        print("worst-case list full")
        print("n*2lik yerden tasima yapilacak")
        B = self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self,c):
        return(c*ctypes.py_object)()


# In[58]:


c = DynamicArray()
for i in range(10):
    c.append(str(i))
#print("length: ", c.getLength())
c.append("qasdasd")
c.append("qasasd")
c.append("qassd")
c.append("qasda")
print("length: ", c.__len__())


# In[51]:


for i in range(c.__len__()):
    print(c[i])


# In[ ]:


DynamicArray yapısı karmaşıklığı nedir? Hangi durumlarda o(n) olur
Karmaşıklığı birdir.

