def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

if __name__ == "__main__":
    print(solution(13, 17)) # 43
    print(solution(24, 27)) # 52