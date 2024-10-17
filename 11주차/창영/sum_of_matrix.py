def solution(arr1, arr2):
    answer = []
    for i in zip(arr1, arr2):
        temp = []
        for j in range(len(i[0])):
            temp.append(i[0][j] + i[1][j])
        answer.append(temp)
    return answer

if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]])) # [[4,6],[7,9]]