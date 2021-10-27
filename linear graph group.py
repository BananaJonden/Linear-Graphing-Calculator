# members: Justin, Jay, Isaac, & Jonden
import math
import turtle as trtl
t = trtl.Turtle()
t.speed(0)

# Move function
def move(a,b):
    t.penup()
    t.setposition(a,b)
    t.pendown()



# X & Y AXES (Isaac) :
def axes():
    # Set up x-axis
    t.pensize(2)
    move(0,0) 
    t.setheading(0)
    # Drawing x-axis
    t.forward(200)
    t.backward(400)
    # Set up y-axis
    t.forward(200)
    t.left(90)
    # Drawing y-axis
    t.forward(200)
    t.backward(400)
    t.forward(200)
    t.right(90)
  
axes()



# COORDINATE PLANE (Jonden) :

t.pensize(1)
x = -200
y = -200
t.speed(0)
t.left(90)
# Vertical Plane
for i in range(41):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.forward(400)
  x = x + 10

u = -200
p = 200
t.right(90)
# Horizontal Plane
for i in range(41):
  t.penup()
  t.goto(u,p)
  t.pendown()
  t.forward(400)
  p = p - 10  

# X and Y label

t.penup()
t.goto(-5, -220)
t.write(-20)
t.penup()
t.goto(-5, 205)
t.write("20  (y)")
t.goto(210,-5)
t.write("20  (x)")
t.goto(-220,-5)
t.write(-20)



# LINE FUNCTION (Justin & Jay) :

t.pensize(3)

# User input for the slope and y-intercept
user_input = ("What is the line? (Say in form 'y=mx+b' with no spaces) -> ")
m = int(user_input[2])
b = int(user_input[4])

# Calculating the angle of the line (for arrows)
x1 = 10.0
y1 = abs(m*10) + b
pos1 = (0, b)
pos2 = (x1, y1)
direction = math.degrees(math.atan((y1 - b)/x1))

t.color("blue")
t.setposition(0, b)
t.pendown()
t.setheading(0)
x1 = 0
y1 = b

# Positive slope
if m > 0:

    # First half of the line
    t.left(direction)
    while x1 <= 200 and y1 <= 200:
        t.setposition(x1, y1)
        x1 += 1
        y1 += m*1
    t.stamp()

    # Second half of the line
    t.setposition(0, b)
    x1 = 0
    y1 = b
    while x1 >= -200 and y1 >= -200:
        t.setposition(x1, y1)
        x1 -= 1
        y1 -= m*1
    t.left(180)
    t.stamp()

# Negative slope
elif m < 0:

    # First half of the line
    t.left(180)
    t.right(direction)
    while x1 >= -200 and y1 <= 200:
        t.setposition(x1, y1)
        x1 -= 1
        y1 -= m*1
    t.stamp()

    # Second half of the line
    t.setposition(0, b)
    x1 = 0
    y1 = b
    while x1 <= 200 and y1 >= -200:
        t.setposition(x1, y1)
        x1 += 1
        y1 += m*1
    t.left(180)
    t.stamp()
    
wn = trtl.Screen()
wn.mainloop()