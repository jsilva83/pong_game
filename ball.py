# Importing external packages.
import random
import turtle

# Constants.
BALL_SHAPE = 'circle'
BALL_COLOR = 'white'
WINDOW_MAX_HEIGHT_POSITION = 300
WINDOW_MIN_HEIGHT_POSITION = -300
WINDOW_MAX_WIDTH_POSITION = 300
WINDOW_MIN_WIDTH_POSITION = -300
DISTANCE_TOLERANCE = 10


class Ball(turtle.Turtle):

    def __init__(self):
        """Creates a turtle ball at the center of the screen"""
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.goto(x=0, y=0)
        # Set the ratio between x displacement and y displacement (not used).
        self.ratio_xy = random.uniform(0.3, 0.7)
        # Set attribute for displacement for x and y axes.
        self.x_move = 10
        self.y_move = 10
        return

    def move_right_up_corner(self, n_steps) -> None:
        """Moves the ball in a 45 degrees angle towards the up right corner."""
        new_x = self.xcor() + n_steps
        new_y = self.ycor() + n_steps
        print(f'({new_x}, {new_y})')
        if ((WINDOW_MIN_WIDTH_POSITION + DISTANCE_TOLERANCE) <= new_x
            <= (WINDOW_MAX_WIDTH_POSITION - DISTANCE_TOLERANCE)) \
                and ((WINDOW_MIN_HEIGHT_POSITION + DISTANCE_TOLERANCE) <= new_y
                     <= (WINDOW_MAX_HEIGHT_POSITION - DISTANCE_TOLERANCE)):
            self.goto(x=new_x, y=new_y)
        return

    def move(self, n_steps) -> None:
        """Moves the ball in all directions."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        return

    def bounce_y(self) -> None:
        """Bounces the ball if hits the wall."""
        self.y_move *= -1
        return

    def bounce_x(self) -> None:
        """Bounces the ball if hits the wall."""
        self.x_move *= -1
        return

    def reset_position(self) -> None:
        """Reset position of ball to center."""
        self.goto(0, 0)
        self.bounce_x()
        return
