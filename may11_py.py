# -*- coding: utf-8 -*-
"""May11.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IboO8brgozmdp-DF-fEzo_FWqCYCgNMr
"""

for i in range(0,4):
  for j in range(0,4,-1):
    print("$")

for i in range(1,6):
  for k in range(i,5):
    print(" ",end=" ")
  for j in

#while loop
i=1
while(i<5):
  print("hello",i)
  i+=1

#list,tuple,dictionary,set

#list: collection of elements,which has index position
#mutable datatype
#ordered collection of elements
#never use list as it it already a datatype
#use another name such as mylist
mylist=[10,20,'naina']
print(type(mylist))

mylist[0:15]

mylist[0]=100
print(mylist)

mylist.append(50)
print(mylist)

#only one element could be inserted at a time using append
#for this we use a function extend that is used to enter multiple elements in the list

mylist.extend("hey")
print(mylist)

mylist.extend(["hey",99])
print(mylist)

help( mylist )

print(mylist)
mylist.pop()
print(mylist)

print(mylist)
mylist.remove("naina")
print(mylist)

print(mylist)
del mylist[1]
print(mylist)

new1=[]
alist=[1,2,3,4,"Arjita","apple","@"]
for i in alist:
  if (type(i) is int) :
    new1.append(i**2)
print(new1)

#armstrong number
'''num=153
x=num%10
num=num//10
print(num)
y=num%10
num=num//10
print(num)
z=num%10
num=num//10
print(num)'''
num=int(input("enter a number: "))
x=num
total=0
while(num>0):
  rem=num%10
  total+=rem**3
  num=num//10
print(total)
if total==x:
  print("armstrong number")
else:
  print("not a armstrong number")

#TUPLE
#immutable in nature
#if we alredy have fixed number of values for e.g. email-id
#use() not compulsory they are optional
#tuples are faster as compared to lists
#if we want to insert only one element in it then we should seperate it by a comma.

mytuple=(10,23)
print(type(mytuple))

mytuple=(10,20)
print("before",id(mytuple))
mytuple=mytuple+(60,70)
print("after",id(mytuple))
print(mytuple)

#DICTIONARY
#is also a ordered collection of objects in the form of key:value.
#key is an identifier,value is a data.
#key can never be same whereas value can be.
mydict={1:"arjita",2:"apple",9:34,3:11}
print(type(mydict))
print(mydict)

#update
mydict[9]="aman"
print(mydict)

#insert
mydict[30]="aman"
print(mydict)

print(mydict)
x=mydict.pop(30)
print(mydict)
print(x)

#helloo
mydict={}
value="hello"
for char in value:
  mydict[char]=1
print(mydict)

mydict1={10:"tushar",20:"aman",10:"ujjawal"}
print(mydict1)

'''#hey tushar hello
mydict={}
value="heytusharhello"
for char in value:
  mydict[char]=1
 if mydict[char]==value:
    mydict[char]+=1
print(mydict)'''

mydict={}
for char in "hello hey tushar":
  if (char in "aeiou"):
    if char not in mydict:
      mydict[char]=1
    else:
      mydict[char]+=1
print(mydict)
