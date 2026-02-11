import pygame
import sys
from maze import generate_maze
from player import Player
from ai import bfs

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Maze Escape")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

maze = generate_maze(ROWS, COLS)
player = Player(0, 0)
enemy = Player(ROWS - 1, COLS - 1)

def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            color = (40, 40, 40) if maze[r][c] == 1 else (200, 200, 200)
            pygame.draw.rect(screen, color, (c*CELL, r*CELL, CELL, CELL))

def draw_text(text):
    img = font.render(text, True, (255, 0, 0))
    screen.blit(img, (200, 250))

running = True
game_over = False
win = False

while running:
    clock.tick(10)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not game_over:
        player.move(keys, maze)

        path = bfs(maze, (enemy.row, enemy.col), (player.row, player.col))
        if path and len(path) > 1:
            enemy.row, enemy.col = path[1]

        if enemy.row == player.row and enemy.col == player.col:
            game_over = True

        if player.row == ROWS-1 and player.col == COLS-1:
            win = True
            game_over = True

    draw_maze()
    player.draw(screen, CELL, (0, 200, 0))
    enemy.draw(screen, CELL, (200, 0, 0))

    if game_over:
        if win:
            draw_text("YOU WIN")
        else:
            draw_text("CAUGHT!")

    pygame.display.flip()

pygame.quit()
sys.exit()
