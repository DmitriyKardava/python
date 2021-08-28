numbers = []
summa_1 = 0
summa_2 = 0
for number in range(1, 1001):
    if number % 2:
        numbers.append(number ** 3)
for number in numbers:
    _sum = 0
    _num = number
    while _num > 0:
        digit = _num % 10
        _sum += digit
        _num = _num // 10
    if _sum % 7 == 0:
        summa_1 += number
    number += 17
    _num = number
    _sum = 0
    while _num > 0:
        digit = _num % 10
        _sum += digit
        _num = _num // 10
    if _sum % 7 == 0:
        summa_2 += number
print(summa_1)
print(summa_2)
