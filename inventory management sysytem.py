#!/usr/bin/env python
# coding: utf-8

# ## display data for mobile phone
# 

# In[7]:



    
    dct={100:{'brand':'iphone',
            'count':13,
            'price':90000},
        101:{'brand':'samsung',
            'count':33,
            'price':20000},
        102:{'brand':'vivo',
            'count':25,
            'price':17000}}
    print(dct)


# ## adding an new element

# In[2]:


def add_item():
    
    reg_no=int(input('reg no : '))
    brand=str(input('enter the brand : '))
    count=int(input('enter the count : '))
    price=int(input('enter the price : '))

    temp={}
    temp['brand']=brand
    temp['count']=count
    temp['price']=price

    dct[reg_no]=temp
    
    print(dct)


# ## update the element
# 

# In[3]:


def update_item():
    

    reg_no_1=int(input('reg_no : '))

    if reg_no_1 != dct.keys():
        print('enter the brand name')
        
    
        brand_=str(input())
        print('enter the count')
        c=int(input())
        print('enter the price  change')
        price_=int(input())
        dct[reg_no_1]['brand']=brand_

        dct[reg_no_1]['count']=c
        dct[reg_no_1]['price']=price_
    
        print(dct)


# ## delete an element
# 

# In[11]:


def delete_item():
    

    ch=int(input('enter the id to be delete : '))

    if ch in dct.keys():
        dct.pop(ch)
    
    print(dct)    


# In[12]:


choice=int(input("enter your choice : "))
if (choice == 1):
    print(dct)
    
elif (choice== 2):
    add_item()
    
elif(choice == 3):
    update_item()
    
elif(choice  == 4):
    delete_item()


# In[ ]:




