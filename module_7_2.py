import io
from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    n = 0
    for s in strings:
        file = open(file_name, 'a', encoding='utf-8')
        b = file.tell()
        file.write(f'{s}\n')
        file.close()
        n += 1
        strings_positions.update({(n, b): s})
    return strings_positions


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)