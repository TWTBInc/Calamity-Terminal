#CODE COMMENTS MEANT TO BE READ WITH WORD WRAP
#CODE COMMENTS MEANT TO BE
#READ WITH WORD WRAP

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import random
#Hide the pygame prompt

#Snakes per second
snake_speed = 12.5

prevSnakeSpeed = 0

score = 0

pause = False

#I thought I was up to the task of not updating this but NOOOOOOO I failed I tried.

showScore = True
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(57, 255, 20) #Changed to be neon green
blue = pygame.Color(0, 0, 255)

#Most of these are unused.

# Initialising pygame
pygame.init()
 
# Initialise game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Calamity Snake Score: {}'.format(score))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
#Changed to not initialize score variable here but at the top for other reasons.
 
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'

            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'

            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

            if event.key == pygame.K_w:
                change_to = "UP"

            if event.key == pygame.K_s:
                change_to = "DOWN"

            if event.key == pygame.K_a:
                change_to = "LEFT"

            if event.key == pygame.K_d:
                change_to = "RIGHT"

            if event.key == pygame.K_b:
                if showScore == True:
                    showScore = False

                elif showScore == False:
                     showScore = True

                else:
                    showScore = True

            if event.key == pygame.K_p:
                if pause == True:
                    pause = False

                else :
                    pause = True

    while pause == True:
        for event in pygame.event.get():

            if event.key == pygame.K_p:
                pause = False

 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

#Snake growing he grows when he collides with an apple.
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        pygame.display.set_caption('Calamity Snake Score:{}'.format(score))
        snake_speed += 0.25
        fruit_spawn = False
        #We make it harder to win with higher snake speed.

    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score countinuously
    if showScore == True:
        show_score(1, white, 'comicsansms', 50)
    else:
        pass
        #Doesnt do shit.

 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)
