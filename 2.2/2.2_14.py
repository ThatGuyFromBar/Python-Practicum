n = input()
arr = list(n)
min1 = 11
min2 = 11
max1 = -1
max2 = -1
for i in range(len(arr)):
    arr[i] = int(arr[i])
    if arr[i] < min1:
        min2 = min1
        min1 = arr[i]
    elif arr[i] < min2:
        min2 = arr[i]
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2:
        max2 = arr[i]
if min1 == 0:
    print(f"{min2}{min1} {max1}{max2}")
else:
    print(f"{min1}{min2} {max1}{max2}")
