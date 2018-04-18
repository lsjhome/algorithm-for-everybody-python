# 연속한 숫자의 합을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 더한 값

def sum_n(n):
    
    if n == 0:
        return 0
    
    # else 부분 없이 바로
    return sum_n(n-1) + n



if __name__ == '__main__':

    print (sum_n(10))
    print (sum_n(100))
