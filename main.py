# Importing external packages.
import time
import turtle

import ball
# Importing internal packages.
import dash
import paddle

# Constants.
GAME_WINDOW_WIDTH = 800
GAME_WINDOW_HEIGHT = 600
GAME_WINDOW_BACKGROUND_COLOR = 'black'
GAME_WINDOW_TITLE = 'My Pong Game'
GAME_WINDOW_MAX_Y_POSITION = 280
GAME_WINDOW_MIN_Y_POSITION = -280
GAME_WINDOW_MAX_X_POSITION = 340
GAME_WINDOW_MIN_X_POSITION = -340
PADDLE_SPEED = 0.1
PADDLE_TOLERANCE = 50
R_PADDLE_INITIAL_POSITION = (370, 0)
L_PADDLE_INITIAL_POSITION = (-380, 0)
INITIAL_SCORE = (0, 0)

# Game initialization.
game_window = turtle.Screen()
game_window.setup(width=GAME_WINDOW_WIDTH, height=GAME_WINDOW_HEIGHT)
game_window.bgcolor(GAME_WINDOW_BACKGROUND_COLOR)
game_window.title(GAME_WINDOW_TITLE)
# Hide the details of setting the turtles in position and moving to initial position.
game_window.tracer(0)
# Create scoreboard.
print('Calling scoreboard class')
my_score = dash.Dash()
# Create right paddle.
r_paddle = paddle.Paddle(R_PADDLE_INITIAL_POSITION, game_window)
l_paddle = paddle.Paddle(L_PADDLE_INITIAL_POSITION, game_window)
# Create ball.
my_ball = ball.Ball()
# Listen to keystrokes.
game_window.listen()
game_window.onkeypress(key='q', fun=l_paddle.move_up)
game_window.onkeypress(key='a', fun=l_paddle.move_down)
game_window.onkeypress(key='p', fun=r_paddle.move_up)
game_window.onkeypress(key='l', fun=r_paddle.move_down)
# Start the game.
game_is_on = True
while game_is_on:
    # Update the window with the last movements.
    game_window.update()
    time.sleep(PADDLE_SPEED)
    my_ball.move(10)
    # Detect collision with wall.
    if my_ball.ycor() > GAME_WINDOW_MAX_Y_POSITION or my_ball.ycor() < GAME_WINDOW_MIN_Y_POSITION:
        my_ball.bounce_y()
    # Detect collisions with the right and left paddles.
    if (my_ball.distance(r_paddle) < PADDLE_TOLERANCE and my_ball.xcor() > GAME_WINDOW_MAX_X_POSITION) \
            or (my_ball.distance(l_paddle) < PADDLE_TOLERANCE and my_ball.xcor() < GAME_WINDOW_MIN_X_POSITION):
        my_ball.bounce_x()
    # Detect when the right paddle misses.
    if my_ball.xcor() > GAME_WINDOW_MAX_X_POSITION + 40:
        my_ball.reset_position()
    # Detect when the left paddle misses.
    if my_ball.xcor() < GAME_WINDOW_MIN_X_POSITION - 40:
        my_ball.reset_position()
# Exit window on click.
game_window.exitonclick()
