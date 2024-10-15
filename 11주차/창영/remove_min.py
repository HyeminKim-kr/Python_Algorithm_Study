def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr if arr != [] else [-1]

if __name__ == "__main__":
    print(solution([4,3,2,1]))
    print(solution([10]))