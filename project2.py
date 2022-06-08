a = [[1, 2], [3, 4], [5, 6, 7]]

a.reverse()

for i in range(len(a)):
    if isinstance(a[i], list):
        a[i].reverse()

print(a)