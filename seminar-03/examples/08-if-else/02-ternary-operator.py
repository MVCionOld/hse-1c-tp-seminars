# a if condition else b

print('true' if True else 'false')
print('true' if False else 'false')

print('-'*20)

# можно использовать в выражениях

x, y = 5, 3  # да, так можно
x, y = y, x  # и так тоже!

z = (3 + x) if x > y else y

print(z)

z = 3 + (x if x > y else y) # внимательнее с порядком вычислений

print(z)