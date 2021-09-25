# Проверок может быть и несколько сразу:

age = int(input("Enter your age: "))  # Удобно использовать int(input()), если вы запрашиваете число

country = 'Russia'
#country = 'USA'

if age >= 16 and country == 'USA':  # Если вам есть 16 и вы живете в США
    answer = 'Yes, you can drive'
else:
    if age >= 18 and country == 'Russia':  # Если условие выше неверно, но вам есть 18 и вы живете в России
        answer = 'Yes, you can drive'
    else: # Иначе
        answer = "No, you can't drive"

print(answer)