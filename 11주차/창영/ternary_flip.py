def solution(n):
    if n == 0:
        return "0"
    
    ternary = ""
    while n > 0:
        remainder = n % 3
        ternary = ternary + str(remainder)
        n = n // 3
    
    return int(ternary, 3)

if __name__ == "__main__":
    print(solution(45))
    print(solution(125))