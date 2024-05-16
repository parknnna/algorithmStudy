'''
순차적으로 앞에서 부터 나머지 원소들과 비교하여 제일 작은 수와 스왑하여 정렬
'''
array = [7, 5, 0, 9, 3, 1, 2, 4]

for i in range(len(array)):

    # 제일 작은 원소 인덱스
    min_idx = i

    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    
    # 스왑
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)