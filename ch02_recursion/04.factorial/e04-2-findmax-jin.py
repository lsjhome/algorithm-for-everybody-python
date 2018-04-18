# 최댓값 구하기
# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개중 최댓값

def find_max(a, n): # 리스트 a의 앞부분 n개 중 최댓값을 구하는 재귀 함수
    
    if n == 1:
        return a[0] # 종료 조건

    max_n_1 = find_max(a, n - 1) # 재귀 호출 조건

    if max_n_1 > a[n - 1]:
        return max_n_1
    
    return a[n - 1] # else 부분 없애기


if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    print (find_max(v, len(v)))
