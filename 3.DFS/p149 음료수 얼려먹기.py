import sys

input = sys.stdin.readline

# 가로 세로 입력
n, m = map(int, input().split())

graph = [] 

# 맵 입력 받기
for i in range(n):
    graph.append(list(map(int, input().split())))

# DFS로 특정한 노드를 방문 뒤 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 pass
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 아직 방문을 안했다면
    if graph[x][y] == 0:
        # 방문 처리 후
        graph[x][y] = 1
        
        # 상하좌우 모두 재귀 호출..
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)