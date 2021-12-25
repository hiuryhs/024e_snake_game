from os import set_inheritable
from turtle import Turtle, Screen
from typing import List, Tuple
from random import choice, randrange
from PIL import Image
from math import dist

EAT_FOOD_DISTANCE = 15


# Resizes images to be used as shapes by Food class:
pics = ["gui.gif", "ju.gif", "le.gif", "uri.gif"]
resized_pics = []

for pic in pics:
    with Image.open(pic) as image:
        resized_im = image.resize(size=(30, 30))
        new_pic_name = "res" + pic #pic.removesuffix(".gif") + "_rs"
        resized_im.save(new_pic_name)
    resized_pics.append(new_pic_name)
    

class Food_Generator(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.s_object = Screen()
        self.shapes = resized_pics
        for shape in self.shapes:
            self.s_object.register_shape(shape)
        self.maximum_food = 1
        self.active_food = []

    def random_coord_generator(self, screen_object) -> Tuple[int, int]:
        xcor = randrange(
            -screen_object.usable_width
            // 2,
            +screen_object.usable_width
            // 2,
            step=20
        )

        ycor = randrange(
            -screen_object.usable_height
            // 2,
            screen_object.usable_height
            // 2 - screen_object.scoreb_offset, # accounts for scoreboard space
            step=20
        )

        return (xcor, ycor)

    def gen_food(self, snake_positions: List[Tuple,], screen_object):

        if len(self.active_food) < self.maximum_food:
            food_shape = choice(self.shapes)
            food_coord = (
                self.random_coord_generator(screen_object)
            )

            spawn_in_snake = True

            while spawn_in_snake:
                spawn_in_snake = False

                for snake_coord in snake_positions:
                    print(dist(food_coord, snake_coord))
                    if dist(food_coord, snake_coord)/10 <= EAT_FOOD_DISTANCE:
                        food_coord = (
                            self.random_coord_generator(screen_object)
                        )
                        spawn_in_snake = True

            # while food_coord in snake_positions:
            #     food_coord = (
            #         self.random_coord_generator(screen_object)
            #     )

            food = Turtle()
            food.penup()
            food.shape(food_shape)
            food.speed(0)
            food.goto(food_coord)
            self.active_food.append(food)

    def eat_food(self, snake_object, screen_object, scoreb_obj):
        for food_ind in range(len(self.active_food)):
            if(
                snake_object.segments[0].distance(
                self.active_food[food_ind]) < EAT_FOOD_DISTANCE
            ):
                spawn_in_snake = True

                food_coord = (
                    self.random_coord_generator(screen_object)
                )
                while spawn_in_snake:
                    spawn_in_snake = False
                    for snake_coord in snake_object.segs_pos:
                        if dist(food_coord, snake_coord)/10 <= EAT_FOOD_DISTANCE:
                            food_coord = (
                                self.random_coord_generator(screen_object)
                            )
                            spawn_in_snake = True
                        print(dist(food_coord, snake_coord))

                food_shape = choice(self.shapes)
                self.active_food[food_ind].shape(food_shape)
                self.active_food[food_ind].goto(food_coord)

                snake_object.grow()

                scoreb_obj.increase_score()
