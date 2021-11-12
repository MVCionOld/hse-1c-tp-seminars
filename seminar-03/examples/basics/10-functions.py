#
# fact5 = 1
# for i in range(1, 6):
#     fact5 *= i
#
# print(fact5)
#
# fact10 = 1
# for i in range(1, 11):
#     fact10 *= i
#
# print(fact10)
#
# fact100 = 1
# for i in range(1, 101):
#     fact100 *= i
#
# print(fact100)

def calculate_factorial(factorial_base):
    fact = 1
    for i in range(1, factorial_base + 1):
        fact *= i
    return fact

print(calculate_factorial(5))
print(calculate_factorial(10))
print(calculate_factorial(100))