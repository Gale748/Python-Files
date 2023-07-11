import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Random Shape")
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2)  # Adjust the speed of drawing

# Generate a random shape
def draw_random_shape():
    sides = random.randint(3, 10)  # Random number of sides (between 3 and 10)
    angle = 360 / sides

    # Set a random pen color
    pen.color(random.random(), random.random(), random.random())

    # Draw the shape
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(50)  # Adjust the size of the shape
        pen.right(angle)
    pen.end_fill()

# Call the function to draw a random shape
draw_random_shape()

# Exit the program when the turtle window is clicked
screen.exitonclick()
