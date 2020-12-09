import pygame
import random

pygame.init()

# Colors
bg_color = (175, 155, 235)
red = (25, 10, 164)
black = (0, 0, 0)

# Creating window
screen_width = 1380
screen_height = 763
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("MiniSnakesTsubek")
pygame.display.update()

# Game variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width-10)
food_y = random.randint(20, screen_height-50)
score = 0
init_velocity = 5
snake_size = 30
fps = 90

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


snk_list = []
snk_length = 1

# Game Loop
while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x)<30 and abs(snake_y - food_y)<30:
        score +=1
        food_x = random.randint(20, screen_width )
        food_y = random.randint(20, screen_height )
        snk_length +=5

    gameWindow.fill(bg_color)
    text_screen("POINTS: " + str(score * 10), red, 5, 5)
    pygame.draw.circle(gameWindow, red, [food_x, food_y], 15)
    pygame.draw.circle(gameWindow, black, [food_x-6, food_y-4], 5)
    pygame.draw.circle(gameWindow, black, [food_x+6, food_y-4], 5)
    pygame.draw.rect(gameWindow,bg_color, [food_x-3, food_y+4, 7, 2])




    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]

    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()