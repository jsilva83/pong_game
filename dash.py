import turtle


class Dash(turtle.Turtle):

    def __int__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.text = f'{self.l_score}                   {self.r_score}'
        self.color('white')
        # self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_display()
        return

    def update_display(self):
        self.clear()
        self.write(f'{self.text}', align='center', font=('courier', 80, 'normal'))
        return
