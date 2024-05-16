'''
sorted() 함수는 병렬정렬 기반으로 만들어짐 
O(NlogN) 시간복잡도를 가짐
'''
array = [7, 5, 0, 9, 3, 1, 2, 4]

result1 = sorted(array)
print(result1)

array.sort()
print(array)

def setting(data):
    return data[1]

'''
딕셔너리의 키를 지정해서 사용가능
'''
array2 = [('바나나', 2), ('당근', 3), ('사과', 1)]
result2 = sorted(array2, key=setting)
print(result2)