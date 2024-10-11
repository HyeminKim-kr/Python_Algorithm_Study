def solution(x, n):
    answer = []
    i = x
    while True:
        if n == 0:
            return answer
        answer.append(i)
        i += x
        n -= 1
        

if __name__ == "__main__":
    print(solution(2, 5))
    print(solution(4, 3))
    print(solution(-4, 2))
    print(solution(0, 1))