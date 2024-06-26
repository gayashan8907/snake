from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f'Score is {self.score}', False, align='center')
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', False, align='center')


    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f'Score is {self.score}', False, align='left')

