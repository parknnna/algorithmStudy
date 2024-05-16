import sys

input = sys.stdin.readline

n, k = map(int, input().split())

result = 0

while True:
    while True:
        if (n % k) == 0:
            break
        n -= 1
    
    n /= k 
    result += 1
    if n == 1:
        break

print(result)