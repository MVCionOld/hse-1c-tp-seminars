s = 'abcdef'                # str
l = [1, 2, 2.5, 'abc', [1, 2, 3]]      # list
t = (42, 41, True)          # tuple
S = {1, 2, 3}               # set
D = {1: 2, 'key': 'value'}  # dict

print(D['key'])

print(type(s))
print(type(l))
print(type(t))
print(type(S))
print(len(D))

print('=' * 20)

D['key'] = [{}, {1: 1}, False]
D['another_key'] = "=))"
print(D)