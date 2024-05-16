
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    # 중간 값
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소 개수), target(찾고자 하는 문자) 입력    
n, target = list(map(int, input().split()))

# 전체 원소 입력
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않음")
else:
    print(result + 1)
