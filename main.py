arr = [12, 45, 1, 89, 45, 89, 34]
max1 = max2 = float('-inf')

for num in arr:
    if num > max1:
        max2 = max1
        max1 = num
    elif max1 > num > max2:
        max2 = num

if max2 == float('-inf'):
    print("There is no second maximum element.")
else:
    print("Second maximum element is:", max2)


