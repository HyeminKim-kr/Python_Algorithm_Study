import sys
input = sys.stdin.readline

data = []
temp = ""
for i in range(3):
    temp += input()

data = temp.strip().split()

data_dict = {str(i) : 0 for i in range(1, 10)}

for i in data:
    data_dict[i] += 1

answer = []
for i in data_dict.items():
    if i[1] == 0:
        answer.append(i[0])

print(' '.join(answer))