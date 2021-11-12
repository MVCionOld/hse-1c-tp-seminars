i = 0
k = 5
S = 0  # сумма первых 100 чисел не кратных k

while i < 100:
    i += 1
    if i % k == 0:
        continue
    S += i

print(S)