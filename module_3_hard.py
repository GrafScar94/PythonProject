def calculate_structure_sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
            summa += calculate_structure_sum(*arg)
        if isinstance(arg, dict):
            arg = list(arg.items())
            summa += calculate_structure_sum(*arg)
        if isinstance(arg, int):
            summa += arg
        if isinstance(arg, str):
            summa += len(arg)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

res = calculate_structure_sum(*data_structure)
print(res)
