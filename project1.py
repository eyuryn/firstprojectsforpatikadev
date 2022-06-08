# These codes only work on max three nested lists

a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b = []

for i in a:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    if type(k) == list:
                        for l in k:
                            b.append(l)
                    else:
                        b.append(k)
            else:
                b.append(j)

    else:
        b.append(i)
print(b)
