from collections import deque

def solution(order):
    stack = []
    idx = 0
    for box in range(1, len(order) + 1):
        if box == order[idx]:
            idx += 1
        else:
            stack.append(box)

        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1

    return idx

if __name__ == "__main__":
    print(solution([4, 3, 1, 2, 5]))
    print(solution([5, 4, 3, 2, 1]))
    print(solution([1, 2, 4, 3, 5]))