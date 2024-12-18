import pygame
import time
import random

pygame.init()

screen_width = 800
screen_height = 600

block_size = 20
snake_speed = 10

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Function for snake drawing
def snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, green, [block[0], block[1], block_size, block_size])

#Function for food drawing
def draw_food(x, y):
    pygame.draw.rect(game_display, red, [x, y, block_size, block_size])

#Function for Score Display
def display_score(score):
    font = pygame.font.SysFont("timesnewroman", 35)
    value = font.render(f"Score: {score}", True, white)
    game_display.blit(value, [0,0])

#Function for Game Over Screen
def message(text, color, x, y):
    font = pygame.font.SysFont("timesnewroman", 35)
    value = font.render(text, True, color)
    game_display.blit(value, [x,y])

#Main function of the game
def game_loop():
    game_over = False

    x1 = screen_width // 2
    y1 = screen_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    #Main game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # press X for closing
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        game_display.fill(black)

        display_score(snake_length-1)

        draw_food(food_x, food_y)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        while game_over:
            game_display.fill(black)
            message("Game Over! Press Q to Quit or R to Restart", red, screen_width // 8, screen_height // 2 - 50)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        game_loop()

        if x1 == food_x and y1 == food_y:
            snake_length += 1

            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

        snake(block_size, snake_list)

        pygame.display.update()

        clock.tick(snake_speed)
    pygame.quit()
    quit()
game_loop()


