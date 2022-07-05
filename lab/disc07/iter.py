s = [[1, 2, 3, 4]]
i = iter(s)
j = iter(next(i))
print(next(j))
s.append(5)
print(next(i))
print(next(j))
print(list(j))
print(next(i))