# Importing external packages.
import turtle

SCOREBOARD_ALIGNMENT = 'center'
SCOREBOARD_FONT = ('courier', 80, 'normal')
SCOREBOARD_COLOR = 'white'
SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 280


class Dash(turtle.Turtle):

    def __int__(self, initial_score):
        """Creates the scoreboard object inheriting from Turtle."""
        super().__init__()
        self.left_score = initial_score[0]
        self.right_score = initial_score[1]
        self.text = f'{self.left_score}                 {self.right_score}'
        print(self.text)
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.update_display()
        return

    def update_display(self) -> None:
        """Updates the score when a paddle wins."""
        self.clear()
        self.write(f'{self.text}', align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        print(self.text)
        return
