# n번째 피보나치 수열 찾기
# 입력: n값(0부터 시작)
# 출력: n번째 피보나치 수열 값

def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)


class Fibonacci():

    def __init__(self):

        self.fibo_dict = {}


    def fibo_return(self, n):
        if n <= 1:
            return n

        else:

            if n in self.fibo_dict:
                return self.fibo_dict[n]

            self.fibo_dict[n] = self.fibo_return(n-2) + self.fibo_return(n-1)
            return self.fibo_dict[n]

if __name__ == '__main__':

    fibo_class = Fibonacci()
    
    from time import time

    start_time = time()
    print (fibo_class.fibo_return(100))
    end_time = time()
    print (end_time - start_time)

    start_time = time()
    print (fibo_class.fibo_return(100))
    end_time = time()
    print (end_time - start_time)
