
def fn(str, k):
  # 'T' 문자를 기준으로 문자열을 분리하여 리스트로 만들기 
  # ITISTESTSTRING 을 T를 기준으로 나누게 되면 
  # [0] I , [1] IS, [2] ES, [3] S, [4] RING

    s = str.split('T')
    # 분리된 리스트의 k번째 요소(인덱스 k) 반환
    # 인자로 전달된 k는 3 이므로 3번째 인덱스인 S 반환 
    return s[k]


str = "ITISTESTSTRING"
k = 3

result = fn(str, k)


print(result) # S 출력 
