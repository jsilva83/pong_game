# Importing external packages.
import turtle

SCOREBOARD_ALIGNMENT = 'center'
SCOREBOARD_FONT = ('courier', 80, 'normal')
SCOREBOARD_COLOR = 'white'
SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 280


class Fish(turtle.Turtle):

    def __int__(self):
        """Creates the scoreboard object inheriting from Turtle."""
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.text = f'{self.left_score}                 {self.right_score}'
        print(self.text)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_display()
        return

    def update_display(self) -> None:
        """Updates the score when a paddle wins."""
        self.clear()
        self.write(f'{self.text}', align='center', font=('courier', 80, 'normal'))
        print(self.text)
        return
