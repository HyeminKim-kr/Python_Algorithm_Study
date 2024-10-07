import sys
input = sys.stdin.readline

data = input().strip().split()
data_dict = {}

for i in data:
    if i in data_dict:
        data_dict[i] += 1
    else:
        data_dict[i] = 1

for i in data_dict.keys():
    print(f"{i}:{data_dict[i]}개", end=' ')