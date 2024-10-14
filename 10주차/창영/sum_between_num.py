def solution(a, b):
    return sum(([i for i in range(a, b - 1 if a > b else b + 1, -1 if a > b else 1)]))

if __name__ == "__main__":
    print(solution(3, 5))
    print(solution(3, 3))
    print(solution(5, 3))