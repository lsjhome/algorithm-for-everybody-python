# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자가 n개중 최댓값


def find_max(a):
    n = len(a)
    max_v = a[0]

    for i in range(1, n): # 인덱스를 생각해서 n-1까지 비교해야 한다.
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]

print (find_max(v))
