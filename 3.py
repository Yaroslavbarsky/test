data = [1, 2, ['234', 2], [34, [12, '3452'], 12], [123]]
data2 = []
for x in range(2):
    for i in data:
        if isinstance(i,list):
            data2.extend(i)
        else:
            data2.append(i)
    data = data2
    data2 = []
print(data)
