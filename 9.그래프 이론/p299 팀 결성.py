
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

for i in range(0, n + 1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")


'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1 
0 3 7 
0 4 2
0 1 1
1 1 1

'''