'''
Created on 2018年3月21日

@author: dell
'''

import turtle, time
t = turtle.Pen()
turtle.Turtle().screen.delay(0)

def curveMove():
    for i in range(200):
        t.right(1)
        t.forward(1)

def drawHeart():
    t.hideturtle()
    t.color('red','pink')        
    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    curveMove()
    t.left(120)
    curveMove()
    t.forward(111.65)
    t.end_fill()
    t.goto(0, 0)
    time.sleep(2)

def deleteHeart():
    t.hideturtle()
    t.left(140)
    t.color('white','white')        
    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    curveMove()
    t.left(120)
    curveMove()
    t.forward(111.65)
    t.end_fill()
    t.goto(0, 0)
    time.sleep(2)
    
def writeWord():
    t.hideturtle()
    t.color("red")  
    t.penup()  
    t.goto(-30,200)  
    t.pendown()  
    t.write("Love U",font=("Times",18,"bold"))
    turtle.done()

def main():  
    drawHeart()
    #deleteHeart()
    writeWord()
   
if __name__ == "__main__":  
    main()  