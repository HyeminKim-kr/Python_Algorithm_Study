data = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]

data_dict = {}

for i in data:
    for j in i:
        if j in data_dict:
            data_dict[j] += 1
        else:
            data_dict[j] = 1

print(max(data_dict, key = data_dict.get))
