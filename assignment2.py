# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hnAhzbdEUCeOfdd9Wc0bFcX44FaxG-H-
"""

#ques1)Make a pattern
1
12
123
1234
12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print("")

#Ques2)Make a pattern:
'''1
2 3
4 5 6
7 8 9 10'''
count=1
for i in range(1, 5):
    for j in range(0,i):
        print(count, end=" ")
        count+= 1
    print("")

#Ques3)Make a pattern:
'''10
9 8
7 6 5
4 3 2 1'''
num = 10
for i in range(0,4):
    for j in range(0,i+1):
        print(num, end=' ')
        num-=1
    print("\r")

#Ques4)Make a pattern
'''A
A B
A B C
A B C D'''
for i in range(1, 5):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()

#Ques5)Make a pattern:
'''A
B C
D E F
G H I J'''
count=65
for i in range(1,5):
    for j in range(i):
        print(chr(count), end=" ")
        count+= 1
    print()

#Ques6)Make a pattern:
'''Z
X V
T R P'''
count=90
for i in range(0,3):
    for j in range(0,i+1):
        print(chr(count), end=" ")
        count=count-2
    print()

#Ques7)Make a pattern
'''*
* *
*   *
*     *
* * * * *'''

for i in range (0,4):
  for j in range(0,i+1):
    if i==j or j==0 or i==3:
      print('*',end=" ")
    else:
      print(" ",end=" ")
  print("")

