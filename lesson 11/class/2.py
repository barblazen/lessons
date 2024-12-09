x = [[1, 2, 3]]*3
y = [[1,2,3] for _ in range(3)]
print(x[0][0])
print(y[0][0])
x[0][0] = 5
y[0][0] = 5
print(x)
print(y)