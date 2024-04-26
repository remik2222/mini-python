import pygame
import random
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Defender")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Gracz
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 10

# Obce statki
enemy_size = 50
enemy_speed = 5
enemy_list = []
enemy_spawn_delay = 100
enemy_spawn_counter = 0

# Punkty
score = 0
font = pygame.font.SysFont(None, 36)

# Funkcja do rysowania gracza
def draw_player():
    pygame.draw.rect(WINDOW, WHITE, [player_pos[0], player_pos[1], player_size, player_size])

# Funkcja do rysowania obcych statków
def draw_enemies():
    for enemy_pos in enemy_list:
        pygame.draw.rect(WINDOW, RED, [enemy_pos[0], enemy_pos[1], enemy_size, enemy_size])

# Funkcja do ruchu gracza
def move_player(direction):
    if direction == "LEFT" and player_pos[0] > 0:
        player_pos[0] -= player_speed
    elif direction == "RIGHT" and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

# Funkcja do tworzenia obcych statków
def create_enemy():
    enemy_x = random.randrange(0, WIDTH - enemy_size)
    enemy_y = random.randrange(-HEIGHT, 0)
    enemy_list.append([enemy_x, enemy_y])

# Funkcja do ruchu obcych statków i ich kolizji z graczem
def move_enemies():
    global score
    for enemy_pos in enemy_list:
        enemy_pos[1] += enemy_speed
        if enemy_pos[1] > HEIGHT:
            enemy_list.remove(enemy_pos)
            score += 1
        if detect_collision(player_pos, enemy_pos):
            game_over()

# Funkcja do wykrywania kolizji między graczem a obcymi statkami
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Funkcja do wyświetlania wyniku
def display_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    WINDOW.blit(score_text, [10, 10])

# Funkcja do wyświetlania ekranu końca gry
def game_over():
    game_over_text = font.render("Game Over! Your Score: " + str(score), True, WHITE)
    WINDOW.blit(game_over_text, [WIDTH // 2 - 200, HEIGHT // 2])
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Główna pętla gry
clock = pygame.time.Clock()
running = True
while running:
    WINDOW.fill(BLACK)

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player("LEFT")
            elif event.key == pygame.K_RIGHT:
                move_player("RIGHT")

    # Tworzenie obcych statków
    if enemy_spawn_counter == enemy_spawn_delay:
        create_enem
