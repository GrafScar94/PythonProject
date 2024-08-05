my_dict = {'login1': 1467268, 'login2': 6687524, 'login3': 5783314}
print('Dict:', my_dict)
print('Existing value:', my_dict['login2'])
print('Not existing value:', my_dict.get('login99'))
my_dict.update({'login4': 57945688, 'login5': 7589215})
a = my_dict.pop('login3')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print()
my_set = {1, 5.5, 9, 9, 8, 9.1, 8, 1, 5.5, 9.1, 'a', 'b', 'c', 'a', 'b', True, False}
print('Set:', my_set)
#Заметил, что логическое значение True во множестве не выводится, тогда как False спокойно вывелось. Почему так?
my_set.add('12')
my_set.add((1, 3, 8))
my_set.discard(9.1)
my_set.remove('a')
print('Modified set:', my_set)