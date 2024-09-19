x = input()
y = input()
while len(x) < len(y):
    x = "0" + x
while len(y) < len(x):
    y = "0" + y
for i in range(len(x)):
    x = x[:i] + f'{(int(x[i]) + int(y[i])) % 10}' + x[i + 1:]
print(int(x))