import random
def random_numb():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(numbers)
    return n

n = random_numb()
password = []

for i in range(1, n):
    for j in range(i + 1, n):
        k = i + j
        if n % k == 0:
            password.append(i)
            password.append(j)
print(n, '-', *password)