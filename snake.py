import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("🐍 Snake Game 🐍")
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off automatic updates

# Snake setup
snake = []
for i in range(3):
    segment = turtle.Turtle("square")
    segment.color("limegreen")
    segment.penup()
    segment.goto(x=-20 * i, y=0)
    snake.append(segment)

# Food setup
food = turtle.Turtle("circle")
food.color("gold")
food.penup()
food.shapesize(stretch_wid=0.8, stretch_len=0.8)  # Make the food slightly smaller
food.goto(0, 100)

# Border setup
border = turtle.Turtle()
border.color("white")
border.penup()
border.hideturtle()
border.goto(-290, 290)
border.pendown()
border.pensize(3)
for _ in range(4):
    border.forward(580)
    border.right(90)

# Score setup
score = 0
high_score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)

# Function to update score display
def update_score():
    global high_score
    if score > high_score:
        high_score = score  # Update high score if necessary
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

update_score()

# Game mechanics
direction = "stop"

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

def move():
    if direction == "up":
        snake[0].sety(snake[0].ycor() + 20)
    if direction == "down":
        snake[0].sety(snake[0].ycor() - 20)
    if direction == "left":
        snake[0].setx(snake[0].xcor() - 20)
    if direction == "right":
        snake[0].setx(snake[0].xcor() + 20)

# Game over display
def game_over():
    game_over_display = turtle.Turtle()
    game_over_display.color("red")
    game_over_display.hideturtle()
    game_over_display.write("GAME OVER!", align="center", font=("Arial", 36, "bold"))
    time.sleep(2)
    game_over_display.clear()

# Reset the game
def reset_game():
    global score, direction
    game_over()
    score = 0
    update_score()

    # Move all segments off-screen
    for segment in snake[1:]:
        segment.goto(1000, 1000)  
    snake.clear()

    # Recreate the snake with 3 segments
    for i in range(3):
        segment = turtle.Turtle("square")
        segment.color("limegreen")
        segment.penup()
        segment.goto(x=-20 * i, y=0)
        snake.append(segment)
    
    direction = "stop"

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # Move the snake body
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)
    move()

    # Check collision with food
    if snake[0].distance(food) < 15:
        # Move food to a new random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle("square")
        new_segment.color("limegreen")
        new_segment.penup()
        snake.append(new_segment)

        # Update score
        score += 10
        update_score()

    # Check collision with wall
    if (snake[0].xcor() > 280 or snake[0].xcor() < -280 or
        snake[0].ycor() > 280 or snake[0].ycor() < -280):
        reset_game()

    # Check collision with itself
    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            reset_game()

screen.mainloop()
