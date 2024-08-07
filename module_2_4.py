numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in (numbers):
  if i > 1:
    k = 0
    n = i
    for j in range(1, n + 1):
      if n % j == 0:
        k += 1
    if k == 2:
      primes.append(i)
    else:
      not_primes.append(i)
print("Простые числа: ", primes)
print("Сложные числа: ", not_primes)