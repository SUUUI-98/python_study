lst = [1,2,3]
# lst 의 요소들을 하나씩 꺼내어 *2 를 하고 딕셔너리로 만듦 
# dst = {1: 2, 2: 4, 3: 6}

dst = {i : i* 2 for i in lst}
# dst 의 값들을 set 으로 만듦 
s = set(dst.values()) # s = {2,4,6}

lst[0] = 99 # [99,2,3]
dst[2]= 7 # dst = {1: 2, 2: 7, 3: 6}
s.add(99) # {2,4,6,99}

print(len(s & set(dst.values()))) 
# set(dst.values()) = {2,7,6}
# 교집합 연산 & 로 인해 중복 요소 {2, 6} 만 가져옴 
# 2 출력 
