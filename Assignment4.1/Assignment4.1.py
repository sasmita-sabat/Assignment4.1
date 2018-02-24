
# coding: utf-8

# In[113]:


#Calculate the area of triangle
#Assign the dimension of the triangle
class Dimension:
    def __init__(self,s,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.s=s
        
#Subclass calling the super constructor and calculate area
class Calculate(Dimension):
    def __init__(self,*args):
        super(Calculate,self).__init__(*args)
        
    def area(self):
        self.area=(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)) ** 0.5
        return self.area

side=input("Enter the dimension of side  of the triangle: ")
a=input("Enter the dimension of  a side  of the triangle: ")
b=input("Enter the dimension of b side  of the triangle: ")
c=input("Enter the dimension of c side  of the triangle: ")
s=int(side)
a=int(a)
b=int(b)
c=int(c)
calculate= Calculate(s,a,b,c)
total_area=calculate.area()
print("The total area is "+ str(total_area))


# In[114]:


#class with Filter long words 
     
def filter_long_words(list,n):
        templist=[]
        for word in list:
            if(len(word) > n):
                templist.append(word)
        return templist  

l=input("Enter the list of words: ")
x=input("Enter the number by which the words needs to be compared: ")
k=filter_long_words(l.split(','), int(x))
k
        


# #### 
