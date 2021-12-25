from turtle import Turtle

FOOD_VALUE = 5
SCORE_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.pencolor(SCORE_COLOR)
        self.current_score = 0
        with open("high_score.txt", 'r') as stored_high_score:
            self.high_score = int(stored_high_score.readline())

    def create_and_position_scoreb(self, screen_obj):        
        # Positions the scoreboard on the screen:
        xcor = 0
        ycor = screen_obj.usable_height//2 - screen_obj.scoreb_offset//2
        self.goto(xcor, ycor)

        self.write(
            f"SCORE: {self.current_score}   HIGHEST: {self.high_score}",
            move=False,
            align="center",
            font=("Arial", 12, "italic")
            )

    def increase_score(self):
        self.current_score += FOOD_VALUE

        # Check if current score is the new highest score:
        if self.current_score >= self.high_score:
            self.high_score = self.current_score

        # Clears scoreboard and writes new values:
        self.clear()
        self.write(
            f"SCORE: {self.current_score}   HIGHEST: {self.high_score}",
            move=False,
            align="center",
            font=("Arial", 12, "italic")
            )

    def write_high_score(self):
        with open("high_score.txt", "w") as stored_high_score:
            stored_high_score.write(str(self.high_score))
    
    def reset_score(self):
        self.current_score = 0