import turtle

SCOREBOARD_ALIGNMENT = 'center'
SCOREBOARD_FONT = ('courier', 20, 'normal')
SCOREBOARD_COLOR = 'white'
SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 265


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.update_display()
        return

    def update_display(self) -> None:
        """Updates the score when a paddle wins."""
        self.clear()
        self.color(SCOREBOARD_COLOR)
        self.write(f'{self.left_score}                 {self.right_score}',
                   align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        return

    def increase_l_score(self) -> None:
        self.left_score += 1
        self.update_display()
        return

    def increase_r_score(self) -> None:
        self.right_score += 1
        self.update_display()
        return
