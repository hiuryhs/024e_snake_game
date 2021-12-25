from food_generator import Food_Generator
from game_screen import Game_Screen
from scoreboard import Scoreboard
from snake import Snake
from dj import Dj


game_screen = Game_Screen()
snake = Snake()
food_gen = Food_Generator()
main_scoreb = Scoreboard()
song_player = Dj()

# TODO Control the Snake


running = True

snake.set_starting_conditions()

game_screen.receive_commands(snake)

main_scoreb.create_and_position_scoreb(game_screen)

song_player.play_intro()


while running:
    song_player.play_background_music()
    snake.udpate_segs_pos()
    snake.colision_itself(main_scoreb)
    snake.colision_walls(game_screen)
    snake.move()
    food_gen.gen_food(snake.segs_pos, game_screen)
    food_gen.eat_food(snake, game_screen, main_scoreb)
    
    game_screen.refresh()
    
game_screen.s_object.exitonclick()
