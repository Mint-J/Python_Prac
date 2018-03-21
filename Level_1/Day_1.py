'''
Created on 2018年3月21日

@author: dell
'''
import turtle

print("HelloWorld!")
user_name=input("Please enter your name: ")
print("Welcome to the NEW world! " + user_name)
print("Let's draw a squre!")
t = turtle.Pen()
for x in range(1,20):
    t.forward(100)
    t.left(95)
print("3Q 4 C'ming!")