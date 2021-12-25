from turtle import Screen
from time import sleep
from typing import Callable

REFRESH_DELAY = 0.1
USABLE_RATIO = 0.93333 # Used to add offset to game screen
SCOREBOARD_OFFSET = 50 # Vacant space to be used by the scoreboard

class Game_Screen:

    def __init__(self, width=600, height=600):
        self.s_object = Screen()
        self.width = width
        self.height = height
        self.usable_ratio = USABLE_RATIO
        self.scoreb_offset = SCOREBOARD_OFFSET
        self.usable_height = self.usable_ratio*self.height
        self.usable_width = self.usable_ratio*self.width
        self.s_object.setup(width, height)
        self.s_object.bgcolor("black")
        self.s_object.title("Cobrinha Game")
        self.s_object.tracer(0)

    def refresh(self):
        sleep(REFRESH_DELAY)
        self.s_object.update()     

    def receive_commands(self, snake_object):
        commands = {
            snake_object.turn_up: "Up",
            snake_object.turn_down: "Down",
            snake_object.turn_left: "Left",
            snake_object.turn_right: "Right"
        }
        self.s_object.listen()
        for function in commands:
            self.s_object.onkey(function, commands[function])