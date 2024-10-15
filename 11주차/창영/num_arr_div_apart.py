def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) if [i for i in arr if i % divisor == 0] != [] else [-1]

if __name__ == "__main__":
    print(solution([5, 9, 7, 10], 5))
    print(solution([2, 36, 1, 3], 1))
    print(solution([3,2,6], 10))