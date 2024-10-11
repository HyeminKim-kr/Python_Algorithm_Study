def solution(n):
    return [int(i) for i in reversed(str(n))]

if __name__ == "__main__":
    print(solution(12345))