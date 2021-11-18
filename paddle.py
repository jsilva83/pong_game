# Imports.
import turtle

# Constants.
PADDLE_SHAPE = 'square'
PADDLE_COLOR = 'white'
PADDLE_UP = 90
PADDLE_DOWN = -90
PADDLE_DISTANCE_MOVE = 20
WINDOW_MAX_HEIGHT_POSITION = 300
WINDOW_MIN_HEIGHT_POSITION = -280
PROXIMITY_TOLERANCE = 50


class Paddle(turtle.Turtle):
    """This class extends the turtle class"""

    def __init__(self, initial_position, obj_window):
        """
        Creates paddle.
        Param:initial_position, stands for initial position of the paddle
        Param: obj_window, stands for the object that controls the screen.
        """
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(initial_position)
        return

    def move_up(self) -> None:
        """Moves the paddle up until it hits the wall."""
        if (WINDOW_MAX_HEIGHT_POSITION - self.ycor()) <= PROXIMITY_TOLERANCE:
            return
        new_y_coordinate = self.ycor() + 20
        self.goto(self.xcor(), new_y_coordinate)
        return

    def move_down(self) -> None:
        """Moves the paddle down until it hits the wall."""
        if (self.ycor() - WINDOW_MIN_HEIGHT_POSITION) <= PROXIMITY_TOLERANCE:
            return
        new_y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), new_y_coordinate)
        return
