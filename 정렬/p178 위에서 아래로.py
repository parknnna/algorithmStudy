
cnt = int(input())

arr = []

for _ in range(cnt):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i, sep=' ')
