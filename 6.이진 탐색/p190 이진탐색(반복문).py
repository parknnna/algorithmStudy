
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else :
            start = mid + 1

    return None

# n(원소 개수), target(찾고자 하는 문자) 입력    
n, target = list(map(int, input().split()))

# 전체 원소 입력
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않음")
else:
    print(result + 1)
