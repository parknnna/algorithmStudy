import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[N - 1]
second = data[N - 2]

ret = 0

while True:

    for i in range(K):
        if M == 0:
            break
        ret += first
        M -= 1
    
    if M == 0:
        break

    ret += second
    M -= 1

print(ret)