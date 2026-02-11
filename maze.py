import random

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def carve(r, c):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)
        maze[r][c] = 0

        for dr, dc in directions:
            nr, nc = r + dr*2, c + dc*2
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1:
                maze[r+dr][c+dc] = 0
                carve(nr, nc)

    carve(0, 0)
    maze[rows-1][cols-1] = 0
    return maze
