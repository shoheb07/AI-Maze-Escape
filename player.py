import pygame

class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, keys, maze):
        if keys[pygame.K_UP] and self.valid(maze, self.row-1, self.col):
            self.row -= 1
        if keys[pygame.K_DOWN] and self.valid(maze, self.row+1, self.col):
            self.row += 1
        if keys[pygame.K_LEFT] and self.valid(maze, self.row, self.col-1):
            self.col -= 1
        if keys[pygame.K_RIGHT] and self.valid(maze, self.row, self.col+1):
            self.col += 1

    def valid(self, maze, r, c):
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]):
            return maze[r][c] == 0
        return False

    def draw(self, screen, cell, color):
        pygame.draw.rect(screen, color, (self.col*cell, self.row*cell, cell, cell))
