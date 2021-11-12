i = 0
k = 5
S = 0  # сумма первых 100 чисел

while True:
    i += 1
    S += i
    if not i < 100:
        break

print(S) 