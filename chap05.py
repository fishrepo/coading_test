# (dfs)=======================================

# def dfs(graph, v, visited):

#     visited[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#     print('pop')


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# dfs(graph, 1, visited)

# (bfs)=============================================

# from collections import deque


# def bfs(graph, start, visited):

#     queue = deque([start])

#     visited[start] = True

#     while queue:

#         print('pop')
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# bfs(graph, 1, visited)

#====================================================

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
    
#     if graph[x][y] == 0:
        
#         graph[x][y] = 1
        
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True

#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1
            
# print(result)

#=======================================
from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]
    
print(bfs(0,0))
                
            