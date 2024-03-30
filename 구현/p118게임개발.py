import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0로 초기화
d = [[0] * m for _ in range(n)]

# 현재 케릭터의 위치 x,y 좌표, 방향 받기
x, y, direction = map(int, input().split())
# 현재 위치 방문 표시
d[x][y] = 1

# 맵 정보 받기, 1: 바다, 0: 육지
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 왼, 위, 오른, 아래
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전 함수
def turn_left():
    global direction

    direction -= 1 # 왼쪽으로 방향 전환
    if direction == -1: # 왼쪽을 보고 있는데 전환 시 아래 방향으로(언더 플로시 아래방향)
        direction = 3

# 시뮬레이션 시작
count = 1

turn_time = 0
while True:
    # 왼쪽 회전
    turn_left()

    # 이동 위치 값 저장
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 이동 가능하면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1   # 이동 flag
        x = nx          # x축 수정
        y = ny          # y축 수정
        count += 1      # 이동 거리
        turn_time = 0   # 회전 수 초기화
        continue

    else: # 이동 불가 시
        turn_time += 1
    
    # 4방향 이동 불가(바다 거나 이미 가본 구역)
    if turn_time == 4:
        # 뒤 방향 좌표
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤 방향이 바다가 아닌경우 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else: # 뒤가 바다로 막힘
            break
        
        turn_time = 0
        
print(count)

