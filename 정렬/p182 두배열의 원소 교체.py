
n, k = map(int, input().split()) # n,k  입력

a = list(map(int, input().split())) # a 배열
b = list(map(int, input().split())) # b 배열

a.sort()             # a 배열 오름차순 정렬
b.sort(reverse=True) # b 배열 내림차순 정렬

# 첫번째 인덱스부터 k번 비교
for i in range(k):
    
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 스왑
        a[i], b[i] = b[i],a[i]
    else: # a의 원소가 b의 원소보다 클 경우 종료.
        break

print(sum(a))


