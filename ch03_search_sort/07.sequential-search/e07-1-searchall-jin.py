# 리스트에서 특정 숫자의 위치를 전부 찾기
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾는 값의 위치 번호가 담긴 리스트 ,찾는 갑싱 벗으면 빈 리스트[]

def search_list(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if x == a[i]:
            result.append(i)
    return result

if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    print (search_list(v, 18))
    print (search_list(v, 33))
    print (search_list(v, 900))
