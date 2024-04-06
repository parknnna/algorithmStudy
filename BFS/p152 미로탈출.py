'''
5 6
101010
111111
000001
111111
111111
'''

from collections import deque
import sys

# input = sys.stdin.readline

# N, M를 공백으로 구분하여 입력
n, m = map(int, input().split())

# 2차원 리스트 맵 정보
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            # 이동할 수 있을 경우 현재 이동 거리 + 1 저장
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))

for i in range(n):
    print(graph[i])
    