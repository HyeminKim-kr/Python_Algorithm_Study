angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2
print(sum_angle - (sum_angle // 360) * 360)