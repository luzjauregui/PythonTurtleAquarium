"""

 Aquarium using Turtle modules

 The goal of this project is to create a visually appealing underwater aquarium scene using Python’s Turtle graphics.
 The program should generate different types of fish, bubbles, plants, and rocks, arranged in a balanced composition.
 
"""

import turtle

# ------------------ CIRCLE FISH ------------------------------------
def draw_circle_fish(x, y, size, color, pencolor):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0) 
    turtle.pendown()
    turtle.color(color)  # Set the fill color
    turtle.pencolor(pencolor)  # Set the pen color
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    # Draw eyes
    x_eye = x + size * -0.6
    y_eye = y + size * 1.2
    eye_size = size * 0.15
    draw_eyes(x_eye, y_eye, eye_size, "black", "black")
    # Draw tail
    tail_x = x + size * 2.0  
    tail_y = y + size * 0.4  
    tail_size = size * 1.2  
    draw_triangle(tail_x, tail_y, tail_size, 90, color, pencolor)
    # Draw bubbles 
    for i in range(3):
        bubble_x = x - size * (-1.0 + 0.6 * i) # -0.8
        bubble_y = y + size * (2.7 - 0.25 * i)
        bubble_size = size * (0.3 - 0.1 * i)
        draw_bubble(bubble_x, bubble_y, bubble_size, "cyan", "white")
              

# --------------------- SQUARE FISH ------------------------------------

def draw_square_fish(x, y, size, color, pencolor):
    turtle.penup()
    turtle.goto(x, y) 
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color) 
    turtle.pencolor(pencolor)
    # Draw square body
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    # Draw Face triangle
    face_x = x + size * 1.0  
    draw_triangle(face_x,y, size, 270, color, pencolor)
    # Draw fin 
    tail_x = x - size * 0.7  
    tail_y = y - size * 0.1
    tail_size = size * 0.8   
    draw_triangle(tail_x, tail_y, tail_size, 270 , color, pencolor) 
    # Draw eyes 
    x_eye = x + size * 1.2
    y_eye = y + size * -0.3
    eye_size = size * 0.06
    draw_eyes(x_eye, y_eye, eye_size, "black", "black")
    # Draw bubbles
    for i in range(3):
        bubble_x = x + size * (0.4 + 0.3 * i) # -0.8
        bubble_y = y + size * (0.7 - 0.25 * i)
        bubble_size = size * (0.13 - 0.03 * i)
        draw_bubble(bubble_x, bubble_y, bubble_size, "cyan", "white")
        
# ------------ OTHER (REUSABLE) FUNCTIONS -------------------------------
# function to draw rocks
def draw_eyes(x, y, size, color, pencolor):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown
    turtle.color(color)
    turtle.pencolor(pencolor)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill() 

# Function to draw a bubble
def draw_bubble(x, y, radius, color, pencolor):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.pencolor(pencolor)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.setheading(0)

# Function to draw a rock
def draw_rock(x, y, width, height, color, pencolor):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.pencolor(pencolor)
    
    # drawing the oval
    oval_turtle = turtle.Turtle()
    oval_turtle.penup()
    oval_turtle.goto(x, y)
    oval_turtle.shape("circle")
    oval_turtle.shapesize(stretch_wid=height/10, stretch_len=width/10)
    oval_turtle.color(color)
    oval_turtle.pencolor(pencolor)
    oval_turtle.stamp()

turtle.setheading(0)
# Function to draw a fish tail
def draw_triangle(x, y, height, orientation, color, pencolor):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(orientation)
    turtle.pendown()
    turtle.color(color)  
    turtle.pencolor(pencolor)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(height)
        turtle.left(120)
        #turtle.forward(height)
    turtle.end_fill()
    turtle.setheading(0)

def draw_plant(x, y, height, orientation, color, num_triangles, pencolor):
    for i in range(num_triangles):
        triangle_x = x
        triangle_y = y - (i * height / num_triangles)
        triangle_height = height / num_triangles
        
        draw_triangle(triangle_x, triangle_y, triangle_height, orientation, color, pencolor)
        
# ---------------- DRAWING THE AQUARIUM ------------------------------
    
    
def draw_aquarium():
    turtle.speed(8)
    turtle.bgcolor("lightblue")

    draw_square_fish(130, 70, 60, "yellow", "black")
    draw_square_fish(-130, -90, 60, "yellow", "black")
       
    draw_circle_fish(-100, 0, 30, "lightgreen", "black")
    draw_circle_fish(140, -200, 40, "orange", "black")

    draw_rock(-250, -300, 100, 30, "gray", "black")
    draw_rock(250, -360, 120, 40, "darkgray", "black")

    draw_plant(-250, -200, 100, 180, "green", 5, "black")
    draw_plant(-200, -190, 100, 180, "green", 5, "black")

    draw_plant(230, -230, 120, 180, "darkgreen", 6, "black")
    draw_plant(260, -220, 120, 180, "darkgreen", 6, "black")
    draw_plant(290, -230, 120, 180, "darkgreen", 6, "black")

# Set up the screen
turtle.setup(1000, 800)
draw_aquarium()

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
