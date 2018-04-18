# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd(a, b):

    i = min(a, b) # 두 수 중에서 최솟값

    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1


if __name__ == '__main__':

    print (gcd(1, 5))
    print (gcd(3, 6))
    print (gcd(60, 24))
    print (gcd(81, 27))
    print (5%2)
