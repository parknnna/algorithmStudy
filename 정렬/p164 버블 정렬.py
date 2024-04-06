'''
이중 for문을 이용하여 뒤에서 부터 순차적으로 큰수를 쌓는다..
'''
array = [7, 5, 0, 9, 3, 1, 2, 4]

for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    print(array)

print(array)