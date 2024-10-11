def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))

if __name__ == "__main__":
    print(solution(118372))