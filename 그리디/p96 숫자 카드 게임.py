import sys

input = sys.stdin.readline


n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)

