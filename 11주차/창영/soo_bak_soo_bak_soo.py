def solution(n):
    return ''.join(["수" if i % 2 == 0 else "박" for i in range(n)])

if __name__ == "__main__":
    print(solution(0))
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))