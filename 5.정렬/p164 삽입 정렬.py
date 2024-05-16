'''
현재 원소로 부터 앞에 존재하는 원소들을 정렬
'''
array = [7, 5, 0, 9, 3, 1, 2, 4]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i부터 --1 for...
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break    
    print(array)

print(array)