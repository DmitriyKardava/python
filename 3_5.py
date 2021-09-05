

def get_jokes(num: int, is_unique=False):
    """
    возвращает список из num шуток [существительное, подлежащее, сказуемое],
    выбрынных случайным образом из 3-х словарей
    :param num: количество шуток
    :param is_unique: повторять или нет слова в шутках
    :return: список из num шуток
             если is_unique True и num больше длины списка слов,
             возвращается максимально возможное количество шуток
    """
    from random import sample, choices
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if is_unique:
        num = len(nouns) if num > len(nouns) else num
        noun, adverb, adjective = sample(nouns, num), sample(adverbs, num), sample(adjectives, num)
    else:
        noun, adverb,  adjective = choices(nouns, k=num), choices(adverbs, k=num), choices(adjectives, k=num)
    return list(' '.join(_s) for _s in zip(noun, adverb, adjective))


print(get_jokes(4, True))
print(get_jokes(-1))
print(get_jokes(is_unique=False, num=4))
print(get_jokes(6, True))
