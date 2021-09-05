

def thesaurus_adv(*args):
    result = {}
    for arg in args:
        name, s_name = arg.split()
        result.setdefault(s_name[0], {})
        if arg not in result[s_name[0]].setdefault(name[0], [arg]):
            result[s_name[0]][name[0]].append(arg)
    return result


my_thesaurus = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(my_thesaurus)
