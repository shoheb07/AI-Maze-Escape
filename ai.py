from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            path = []
            while (r, c) in parent:
                path.append((r, c))
                r, c = parent[(r, c)]
            path.append(start)
            path.reverse()
            return path

        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    return None
