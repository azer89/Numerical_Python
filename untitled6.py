#fibonacci

f = [1]
f.append(1)

for i in range(2, 100):
    f.append(f[-1] + f[-2])
