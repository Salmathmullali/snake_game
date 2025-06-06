import pygame
import time
import random


pygame.init()


WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


SNAKE_BLOCK_SIZE = 30  # Snake size
FOOD_BLOCK_SIZE = 20  # Food size

# Clock for controlling game speed
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    value = score_font.render(f"Your Score: {score}", True, GREEN)
    dis.blit(value, [0, 0])


def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], block_size, block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Change in position
    x1_change = SNAKE_BLOCK_SIZE
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - FOOD_BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - FOOD_BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            dis.fill(WHITE)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(WHITE)
        pygame.draw.rect(dis, BLUE, [food_x, food_y, FOOD_BLOCK_SIZE, FOOD_BLOCK_SIZE])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK_SIZE, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats the food
        if x1 < food_x + FOOD_BLOCK_SIZE and x1 + SNAKE_BLOCK_SIZE > food_x and \
                y1 < food_y + FOOD_BLOCK_SIZE and y1 + SNAKE_BLOCK_SIZE > food_y:
            food_x = round(random.randrange(0, WIDTH - FOOD_BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - FOOD_BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(5)  # Slow down the snake slightly

    pygame.quit()
    quit()


# Set up display
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Start the game
game_loop()


