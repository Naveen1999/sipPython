# -*- coding: utf-8 -*-
#Numpy - which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. Using NumPy, mathematical and logical operations on arrays can be performed

#library for numpy : default as part of anaconda
import numpy as np
#np is alias now can be used for various functions 

#Seq : start at 0, end at 10-1
np.arange(10)
np.arange(0,10)

#start at 10, end at 20-1
x=np.arange(10,20)
x

#filter
x[0]  #first value of an array
x[2], x[5], x[-1]  #multiple values seperated by comma
#x[-1]  #last element
x[0:5]  #first 5 elements
x[0:8:2]  #first 8 elements, skip by 1
x[10:0:-1]  #start from 10th position, reverse directions to 0th
x
x[1::3]  #every 3rd element from 2nd element


#random values :
np.random.random(size=10)  #10 numbers between 0 and 1
np.random.randint(10, size=6)  #6 random integer numbers bet 0 and 9 (incl)
x=np.random.randint(60,100, size=100)
np.ptp(x)
range(x)
np.random.randint(10, size=(3,4)) #two Dim random int values betw 0 and 9 (incl) : 3 rows X 4 columns

# save this array in x2 and filter elements
x2=np.random.randint(10, size=(3,4))

x2[1,1]  #first row, first col
x2[:2,] #upto  1st row
 x2[:1,:2]  #intersection of 1st row, upto 2 columns
x2  #see it 
x2[::2,::1]  #alternate row, all columns
x2[::-1,::-1]  #reverse rows an columns #understand

#3 dim
x3=np.random.randint(10, size=(3,4,5))
x3
#check features
np.ndim(x3)  # 3 Dim
np.shape(x3)  # 3 matrix, 4 rows, 5 columns : MRC order
np.size(x3)  # 3 * 4 * 5  = 60

#more numpy
np.random.randint(1, 10, size=10) #10 nos between 1 and 10, 1 dim
np.random.randint(10,20, size=(3,5)) # 3Rows * 5Columns = 15 nos between 10 and 20, 2 dim
xn1=np.random.normal(0,1,(3,3)) #3Rows * 3Columns = 9 normal distributed nos mean=0, stddev=1, 2 Dim array
xn1=np.random.normal(0,1,100)
len(xn1), xn1.mean(), xn1.std()
xn2=np.random.normal(0,1,1000000)
len(xn2), xn2.mean(), xn2.std()
#as sample size becomes large, they follow normal distribution
import seaborn as sns
sns.kdeplot(xn1)
sns.kdeplot(xn2)
#divide points between 10 to 15 into 9 equal spaces
np.linspace(10,15,9)
np.linspace(0,10,5)
xn1.round(2)
np.floor([1.2, 1.6])
np.ceil([1.2, 1.6])
np.trunc([1.2, 1.6])
np.trunc([-1.2, -1.6])
np.floor([-1.2, -1.6])
np.round([1.23434, 1.654455],2)
#fill 10 positions with empty values 0
xe= np.empty(10)  #almost 0; way of initialising; in memory data return
xe#empty, unlike zeros, does not set the array values to zero, and may therefore be marginally faster. On the other hand, it requires the user to manually set all the values in the array, and should be used with caution.
#identity array
np.eye(4)
#all zeros: values already there. need to give numbers or shape
np.zeros([10])
np.zeros(shape=(3,5))
#all ones
np.ones([12])
#all with particular value
np.full((3,4),[3.14])
np.full((3,4), np.pi)
np.full((3,3),'Dhiraj')
#changing shape
ns1=np.array([1,2,3,4])
ns1.shape, ns1.size

np.array([1,2,3,4,5,6,7]).reshape(2,3)
x=np.array([1,2,3,4,5,6]).reshape(2,3)
x
#changing axis
ns1=np.array([1,2,3,4])
ns1a=ns1[:,np.newaxis]
ns1a
#ns2 = np.array([[1],[2],[3],[4],[5]])
#ns2
#ns2[:np.newaxis,]
#%%
#concatenate arrays
x4=np.array([1,2,3,4,5,6,7])
x4.size
#3 x 4
x4b=np.concatenate([x4,np.zeros(5)])
x4c=np.concatenate([x4,np.zeros(3 * 4 - x4.size)])
x4c
x4b.reshape(3,4)


x=np.array([1,2,3])
y=np.array([4,5,6])
x,y
np.concatenate([x,y])
#2dim
x=np.arange(6).reshape(2,3)
x
y=np.arange(10,16).reshape(2,3)
y
np.concatenate([x,y], axis=0)
np.concatenate([x,y], axis=1)
#vertical and horizontal stack
np.vstack([x,y])  #axis =0, rowbind
np.hstack([x,y])  #axis=1, colbind

#split : break the array at particular position
x=np.arange(10,19)
x
np.linspace(10,19,3)
np.split(x,3)
x1,x2,x3 = np.split(x,[3,5])  #3rd, 5th : 3 subarrays
x1,x2,x3
#split in multi dim array
y=x.reshape([3,3])
y
#upper and lower
upper, lower = np.vsplit(y,[2])
upper  #first 2 rows
lower # last row
#left and right : hsplit line : 1st col
left, right = np.hsplit(y,[1])
left
right

#%%
#Ufuncs
x=np.arange(5)
x
x + 5
#using functions of np
np.add(x,5)  #add 5 to values
np.multiply(x,10)  #multiply values by 10
y=np.empty(5)
y  #almost zero/ intialisation o f array
np.multiply(x,5, out=y )  
y  #multiply x by 5 and save it in y
#%%
#more np methods
x=np.random.randint(10,100, size=(3,6))
x 
x.shape  #shape - 3 rows, 6 columns
np.shape(x)
np.size(x)   #how many values
x.sum()  #sum of the values
np.sum(x)
x.mean()  #mean of values
x.sum(axis=0)  #sum of the values : columns  : 6 columns
x.sum(axis=1)  # sum of row values : 3 rows 
x
x.min()
x.min(axis=1) #min in each row
x.max(axis=0) #min in each col
x
np.median(x)  #median values in full dataset
np.max(x)  #max
max(x)  #will not work, as it is multi
max([1,2,3])  #this will work
np.min(x) #min

#%%  More Functions
x=np.random.randint(30,50, size=200000)
x=np.array([30,49,50,60, 49])
np.equal(x, 49) #all values equal to 48
np.sum(np.equal(x,49))
np.greater(x, 40) #values greater than 40
np.sum(np.greater(x,40))  #how many values > 40
sum(np.greater(x,40))
np.less(x, 50)  #values < 50
np.greater_equal(x, 40)  #values >= 40
x < 40 #another way T/ F
np.sum(x < 49)  #how many values < 40
x
np.sum(x < 40, axis=0)  #in each col, values < 40

x=np.random.randint(10, size=(3,4))
x
np.all(x > 4)
np.any(x > 4)
np.sum(x > 1)
np.sum(x > 3, axis=1)
np.sum(x > 3, axis=0)
np.sum( (x> 3) & (x < 7), axis=0)
np.sum( ~((x> 3) & (x < 7)), axis=0)


#sort
#%%
x = np.random.randint(100,size=50)
x
np.sort(x)
np.sort(x)[::-1]
x1 = np.sort(x)
x1[::-1]
#np.sort(-x) 
np.argsort(x) #position of sorted arrays
x[np.argsort(-x)]

#row or column major
np.arange(1,13)
np.arange(1,13).reshape(3,4)
np.arange(1,13).reshape(3,4, order='C')
np.arange(1,13).reshape(3,4, order='F')

#transpose
x=np.arange(1,13).reshape(3,4)
x
x.T
#x.T.view()  #view without modifying

