#!/usr/bin/env python
# coding: utf-8

# ### Homogenous List

# In[43]:


list1=[1,2,3,4,5,6,7,8,9,10]             # create list (creates obj of list class)
print(list1)

print(type(list1))                       # Type of var list1

print(list1[8]==list1[-2])               # +ve and -ve indexing

print(list1[2:6])                        # Slicing

print(len(list1))                        # Length Function

print(list1[15])                         #Indexing (Throws error due to index out of range)


# ### Heterogenous List

# In[14]:


list2=[1,5,9.5,'VB',[3,6.5,'AB']]       

print(list2)
print(list2[-1])
print(list2[-1][2])
print(len(list2))
print(list2[0:10])


# In[20]:


print(list2[:])
print(list2[::-1])
print(list2[0:4:-1])
print(list1[:5])
print(list1[5:])


# In[21]:


list2[:]
list2[::-1]


# ## Functions

# In[27]:


list1.append(25)   # adds elements at the end of list
list1


# In[28]:


list1.insert(3,50) # Inserts element at particular index


# In[29]:


list1


# In[31]:


list1.extend(['1','3','5'])            #adds multiple elements/list at the end


# In[42]:


list1


# In[34]:


new=[]
for i in range(1,len(list1)+1):
    new.append(list1[-i])
print(new)


# In[35]:


list1.pop(3)            #removes 3rd index element
list1


# In[36]:


list1.pop()             # removes last element
list1


# In[37]:


list1.remove(9)         # removes the element from list
list1


# In[38]:


del list1[3]            # deletes the indexed element from list
list1


# In[39]:


del list1[1:4]
list1


# In[40]:


del list1    # removes list1 from memory location


# In[41]:


list1


# In[49]:


list1.clear()          #Empties the list, but variable remains in memory location


# In[50]:


list1


# In[52]:


# WAP to separate even and odd elements

lst=[1,2,3,4,5,6,7,8,9,10]

even=[]
odd=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


# In[53]:


even=lst[1::2]
odd=lst[0::2]
print(even)
print(odd)


# In[2]:


list1=[1,3,5,3.6,'A','B','53']


# In[3]:


el_1=eval(input('Enter 1st element to swap '))
el_2=eval(input('Enter 2nd element to swap '))
tmp,tp,j,m=0,0,0,0
for i in range(len(list1)):
    if list1[i]==el_1:
        tmp=list1[i]
        j=i
        print(tmp)
    if list1[i]==el_2:
        tp=list1[i]
        m=i
        print(tp)
list1[j]=tp
list1[m]=tmp


# In[4]:


list1


# In[6]:


list1=[23,76,8,12,83,69,53,90,24,35,68,37]

minn=list1[0]
maxx=0

for i in range(len(list1)):
    if list1[i]>maxx:
        maxx=list1[i]
        
    if list1[i]<minn:
        minn=list1[i]
print('Maximum Element ',maxx)
print('Minimum Element ',minn)


# In[ ]:




