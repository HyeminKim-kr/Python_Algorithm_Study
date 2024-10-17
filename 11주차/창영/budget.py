def solution(d, budget):
    answer = 0
    for i in sorted(d):
        if budget - i >= 0:
            budget -= i
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9))