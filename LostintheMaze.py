import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lost in the Maze")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Wymiary labiryntu
MAZE_WIDTH, MAZE_HEIGHT = 20, 15
CELL_SIZE = 40

# Klasy postaci gracza i ściany
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        if 0 <= self.x + dx < MAZE_WIDTH and 0 <= self.y + dy < MAZE_HEIGHT:
            self.x += dx
            self.y += dy

    def draw(self):
        pygame.draw.rect(WIN, WHITE, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(WIN, BLACK, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Generowanie labiryntu
def generate_maze():
    maze = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if random.random() < 0.3:  # 30% szansa na ścianę
                maze[y][x] = 1
    return maze

# Rysowanie labiryntu
def draw_maze(maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                Wall(x, y).draw()

# Inicjalizacja gracza
player = Player()

# Główna pętla gry
maze = generate_maze()
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)

    # Czyszczenie ekranu
    WIN.fill(BLACK)

    # Rysowanie labiryntu i gracza
    draw_maze(maze)
    player.draw()

    # Aktualizacja okna
    pygame.display.update()

# Wyjście z gry
pygame.quit()
