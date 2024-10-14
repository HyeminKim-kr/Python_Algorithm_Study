def solution(absolutes, signs):
    return sum([i[0] if i[1] else -i[0] for i in zip(absolutes, signs)])

if __name__ =="__main__":
    print(solution([4, 7, 12], [True, False, True]))
    print(solution([1, 2, 3], [False, False, True]))