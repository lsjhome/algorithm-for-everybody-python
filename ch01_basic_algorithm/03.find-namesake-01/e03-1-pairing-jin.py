# n명에서 두명을 뽑아 짝으로 만드는 모든 경우를 찾는 알고리즘
# 입력: n명의 일므이 들어 있는 리스트
# 출력: 두 명을 뽑아 만들수 있는 모든 짝
# 동명이인 찾기 문제에서 비교 부분을 출력 문장으로

def print_pairs(a):
    n = len(a)

    for i in range(0, n-1):
        for j in range(i+1, n):
            print (a[i], "-", a[j])

name = ["Tom", "Jerry", "Mike"]

name2 = ["Tom", "Jerry", "Mike", "Tom"]

if __name__ == '__main__':

    print (print_pairs(name))
    print ()
    print (print_pairs(name2))

