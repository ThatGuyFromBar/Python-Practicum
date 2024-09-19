n = input()
arr = list(n)
for i in range(len(arr)):
    arr[i] = int(arr[i])
s = min(arr) + max(arr)
arr.remove(min(arr))
arr.remove(max(arr))
if s == arr[0] * 2:
    print("YES")
else:
    print("NO")