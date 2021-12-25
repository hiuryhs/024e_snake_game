from turtle import Turtle
from typing import List, Tuple
from time import sleep

SPEED = 0 # Animation speed
WALK_DIST = 20 # Moving distance per frame
HEAD_COLOR = "orange"
BODY_COLOR = ("orange", "white")
BODY_SHAPE = "square"
STARTING_SIZE = 3
COLISION_DISTANCE = 19

class Snake_Segment(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BODY_SHAPE)
        self.penup()
        self.speed(SPEED)


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.starting_segments = STARTING_SIZE
        self.walk_dist = WALK_DIST
        self.body_color = BODY_COLOR[0]
        self.segments = [] # self.segment[0] becomes the snake "head"
        self.start_pos = [
            (-x * 1 * 20, 0) for x in range(self.starting_segments)
        ]
        self.segs_pos = [seg.pos() for seg in self.segments]

    def color_alternate(self):
        if self.body_color == BODY_COLOR[0]:
            self.body_color = BODY_COLOR[1]
        else:
            self.body_color = BODY_COLOR[0]

    def set_starting_conditions(self):
        self.shape(BODY_SHAPE)
        self.color(HEAD_COLOR)
        self.penup()
        self.speed(SPEED)
        self.body_color = BODY_COLOR[0]
        snake_head = self
        self.segments.append(snake_head) # self.segments[0] is the snake "head"
        for segment in range(1, self.starting_segments):
            snake_piece = Snake_Segment()
            self.color_alternate()
            snake_piece.color(self.body_color)
            self.segments.append(snake_piece)

        for seg_index in range(len(self.segments)):
            self.segments[seg_index].goto(self.start_pos[seg_index])

    def move(self):
        vacant_1 = self.segments[0].pos() # self.segments[0] is the snake "head"
        self.segments[0].forward(self.walk_dist)
       
        for segment in self.segments[1:]:
            vacant_2 = segment.pos()
            segment.goto(vacant_1)
            vacant_1 = vacant_2

    def turn_up(self):
        if not self.heading() == 270:
            self.setheading(90)

    def turn_down(self):
        if not self.heading() == 90:
            self.setheading(270)

    def turn_left(self):
        if not self.heading() == 0:
            self.setheading(180)

    def turn_right(self):
        if not self.heading() == 180:
            self.setheading(0)

    def udpate_segs_pos(self):
        self.segs_pos = [seg.pos() for seg in self.segments]
    
    def grow(self):
        for x in range(10):
            new_segment = Snake_Segment()
            self.color_alternate()
            new_segment.color(self.body_color)
            self.segments.append(new_segment)
            new_segment.goto(self.segs_pos[-1])

    def reset_state(self):
        for segment in self.segments:
            segment.reset()
        self.segments = []
        self.set_starting_conditions()

    def colision_itself(self, score_obj):
        for segment_pos in self.segs_pos[1:]:
            # ! This colision detection method has false positives !
            if (
                self.segments[0].distance(segment_pos)
                < COLISION_DISTANCE
            ):

            # ! This colision detection method has false negatives !
            # if self.segs_pos[0] == segment_pos:
            #     score_obj.write_high_score()
            #     score_obj.reset_score()
                self.reset_state()
    
    def colision_walls(self, screen_obj):
        if ( # + x coordinate 
            self.segs_pos[0][0]
            > screen_obj.usable_width // 2
        ):
            self.segments[0].goto(
                -screen_obj.usable_width // 2,
                self.segs_pos[0][1]
                )

        elif ( # - x coordinate 
            self.segs_pos[0][0]
            < -screen_obj.usable_width // 2
        ):
            self.segments[0].goto(
                screen_obj.usable_width // 2,
                self.segs_pos[0][1]
                )
        elif ( # + y coordinate 
            self.segs_pos[0][1]
            > screen_obj.usable_height // 2 - screen_obj.scoreb_offset
        ):
            self.segments[0].goto(
                self.segs_pos[0][0],
                -screen_obj.usable_height // 2
                )

        elif ( # - y coordinate 
            self.segs_pos[0][1]
            < -screen_obj.usable_height // 2
        ):
            self.segments[0].goto(
                self.segs_pos[0][0],
                screen_obj.usable_height // 2 - screen_obj.scoreb_offset
                )
