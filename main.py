arr = [12, 45, 1, 89, 45, 89, 34]
first = second= float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first> num > second:
        second = num

if second == float('-inf'):
    print("There is no second maximum element.")
else:
    print("Second maximum element is:", second)


