#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data Types 
-Numbers (integers or Float)
-Text (Strings)
-Booleans(True or False)
-List
-Tuples
-Dictionaries
-Sets


# In[1]:


# Integer -Int or integer ,is a whole number ,positive or negative without decimals,of unlimited length.
5000


# In[2]:


type(5000)


# In[3]:


5000 * 4 # To run SHIFT + ENTER sametime   // # regarded as coment.


# In[4]:


250 +250


# In[ ]:


# FLOAT : The difference between floating points and integers is decimal points.
#Floating point numbers can be represented as "1.0" and integer can be represented as "1"


# 10.5

# In[5]:


10.5


# In[6]:


type(10.5) # to figure out the data type


# In[7]:


# Basic Arithmetic
2+2


# In[8]:


16/3


# In[11]:


# Floor Division
100//9


# In[10]:


33*3


# In[12]:


# Modulo
100%9


# In[13]:


2500//40


# In[14]:


2500 % 40


# In[15]:


# Raised To Power
2**4


# In[16]:


#BODMAS
1+3/10*6


# In[17]:


(1+3)/(10*6)


# In[18]:


(1+3)/10*6


# In[19]:


# Variable Assignment
income = 2000
income


# In[20]:


income *2


# In[21]:


income **2


# In[25]:


efe = income/100
efe


# In[30]:


messi = 5000
Ronaldo = messi /2
Ronaldo


# In[32]:


# Test calculator
f_Test = float (input("what is your first test score ?"))
s_Test = float (input("what is your second test score ?"))
attendance = float (input("what is your attendance score ?"))
exam =  float (input("what is yor exam score ?"))

Total_Score = f_Test + s_Test +attendance +exam

Total_Score


# In[33]:


# Strings - Text
"hello world"


# In[34]:


"i'm 10year old"


# In[36]:


f_name = "Olawale"

f_name


# In[41]:


# Full name generator

first_name = "Olawale"
last_name = "Fatokun"
full_name = first_name + ' '+  last_name

full_name


# In[42]:


first_name =str (input ("what is your first name ?") )
last_name = str (input ("what is your last name ?"))

full_name = first_name + ' '+  last_name

full_name


# In[43]:


# Indexing and Sllicing

full_name


# In[45]:


full_name[9]


# In[50]:


# SLICING -- [START STOP STEP]

full_name[0:7]


# In[49]:


full_name[7:15]


# In[52]:


num ="123456789"

num[0:5]


# In[53]:


num[5:]


# In[54]:


# Negative Indexing 
num[-1]


# In[55]:


num[1::2]


# In[56]:


num[0::2]


# In[57]:


# Print Formatting

#.format method
#placholder
#f-string



(.FORMAT METHOD )


name = "Olawale"
age =23

print("my name is {} and i am {} years old".format(name, age))


# In[58]:


first_name = input("what is your name ?")

last_name = input("how old are you ?")

print("my name is {} and i am {} years old".format(name, age))



# In[64]:


# PLACEHOLDER 


name = input("what is your name ?")

age = int(input("how old are you ?"))



print("my name is %s and i am %s years old" %(name, age))


# In[66]:


# f -Strings


name = input("what is your name ?")

age = int(input("how old are you ?"))



print(f"my name is {name} and i am {age} years old")


# In[67]:


# LIST
#An ordered sequence of items 
#The list is the data type that is highly used in python
# It contains versertile data






names = ["Olawale","Muideen" "Fatokun"]

type(names)


# In[70]:


my_list =[1,2,3,"ok,7 ,car"]

my_list


# In[71]:


type(my_list)


# In[75]:


# Indexing and Slicing 

names = ["Olawale", "Muideen" , "Fatokun"]

names[0]


# 

# In[76]:


names[0:2]


# In[78]:


names [0:3]


# In[79]:


names.append("Olamide")


names


# In[80]:


names .append("sherif")

names


# In[82]:


names.pop()


# In[83]:


names


# In[86]:


names.reverse()


# In[87]:


names


# In[88]:


#Dictionaries
#its a data type in which collections are ordered,and values are in pairs called key value pairs.



my_dict = {"key1":"value", "key2":"value2"}
my_dict


# In[91]:



my_dict.keys()


# In[92]:


my_dict.values()


# In[93]:


my_dict["key1"]


# In[94]:


bio_data ={"name":"Olawale","Age":29,"address":"Istanbul","phone-no":40204014}

bio_data


# In[97]:


bio_data["address"]


# In[99]:


bio_data["color"] = "Black"


bio_data


# In[100]:


bio_data["sibblings"] = ["toyin","tolu","dupe","kunle"]



bio_data


# In[101]:


bio_data["sibblings"]


# In[102]:


bio_data["sibblings"][3]


# In[104]:


#Tupple
# A tupple is a sequence of items that are in order,and it is not possible to modify tupple


Age = [24,31,45,78,89,20]

Age





# In[105]:


Age[0] =70

Age


# In[108]:


Age[-5] =10

Age


# In[109]:


tup =[1,2,3,4,5,'olawale','school']
tup


# In[110]:


tup[0]


# In[111]:


tup[-1]


# In[113]:


len(tup)


# In[116]:


#SET
# collection of unique items that are not ordered.


num ={1,2,3,4,5,6,7,8,9,9,92,3,2,34,5,6,55,77}

num


# In[ ]:


# boolean
#True or False


# In[138]:


1>1


# In[ ]:




