

def thesaurus(*args):
    result = {}
    for arg in args:
        if arg not in result.setdefault(arg[0], [arg]):
            result[arg[0]].append(arg)
    return result


my_thesaurus = thesaurus("Иван", "Мария", "Петр", "Илья")
# сортировка по ключам
list_keys = list(my_thesaurus.keys())
list_keys.sort()
for _i in list_keys:
    print(_i, ':', my_thesaurus[_i])
