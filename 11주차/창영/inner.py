def solution(a, b):
    return sum([i[0] * i[1] for i in zip(a, b)])

if __name__ == "__main__":
    print(solution([1,2,3,4], [-3,-1,0,2]))
    print(solution([-1,0,1], [1,0,-1]))