def num_translate(num):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if num and num[0].isupper() and numbers.get(num.lower()):
        return numbers.get(num.lower()).capitalize()
    else:
        return numbers.get(num)


print('One ', num_translate('One'))
print('two ', num_translate('two'))
