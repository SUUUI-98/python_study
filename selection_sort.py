# 배열 초기화
a = [4, 2, 3, 5, 1]
# 자리 바꿀 요소를 담을 임시 변수
temp = 0

# 선택 정렬 구현
# len(a) = 5 즉 선택정렬 4회전 실행 
for i in range(len(a) - 1): 
    # 정렬되지 않은 부분에서 가장 작은 값의 인덱스를 찾음
    min_index = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_index]:
            min_index = j

# i = 0 일 경우 , a[0] 과 나머지 요소들의 크기를 비교하여 위치를 교환 
# 1회전 후 : [2, 3, 1, 5, 4]  

    # 가장 작은 값을 현재 위치와 교환
    temp = a[min_index]
    a[min_index] = a[i]
    a[i] = temp

# 4회전 후 정렬된 배열 출력
# [1, 2, 3, 4, 5] 
print(a)
