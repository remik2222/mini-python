import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake variables
block_size = 20
snake_speed = 10
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 40)

def message(msg, color):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [WIDTH/2 - screen_text.get_width()/2, HEIGHT/2 - screen_text.get_height()/2])

def gameLoop():
    # Game variables
    game_over = False
    game_close = False
    score = 0

    # Snake initial position
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size

    # Main game loop
    while not game_over:

        while game_close:
            win.fill(WHITE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = block_size
                    snake_x_change = 0

        # Update snake position
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Boundary conditions
        if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
            game_close = True

        # Snake body mechanics
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Display food
        win.fill(WHITE)
        pygame.draw.rect(win, GREEN, [food_x, food_y, block_size, block_size])

        # Display snake
        for segment in snake_list:
            pygame.draw.rect(win, BLACK, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        # Snake eats food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
