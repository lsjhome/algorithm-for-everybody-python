# 최솟값 구하기
# 입력: 숫자 n개 들어 있는 리스트
# 출력: 숫자 n개중 최솟값

def find_min(a):
    n = len(a)
    min_v = a[0]

    for i in range(1, n):
        if a[0] > a[i]:
            min_v = a[i]

    return min_v

v = [17, 92, 18, 33, 58, 7, 33, 42]

print (find_min(v))
