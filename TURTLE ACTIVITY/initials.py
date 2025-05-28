import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(1)

# Function to draw the letter C
def draw_C():
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    pen.circle(50, -180)  # Draw a semicircle for 'C'

# Function to draw the letter R
def draw_R():
    pen.penup()
    pen.goto(-50, -50)
    pen.setheading(90)
    pen.pendown()
    pen.forward(100)  # Left vertical line
    pen.right(90)
    pen.circle(-25, 180)  # Upper half-circle
    pen.left(135)
    pen.forward(70)  # Diagonal leg


# Function to draw the letter A
def draw_A():
    pen.penup()
    pen.goto(100, -50)
    pen.pendown()
    pen.goto(125, 50)    # Left diagonal
    pen.goto(150, -50)   # Right diagonal
    pen.penup()
    pen.goto(112.5, 0)
    pen.pendown()
    pen.goto(137.5, 0)   # Crossbar

# Draw the letters
draw_C()
draw_R()
draw_A()

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()
