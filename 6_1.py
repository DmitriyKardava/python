result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    _num = 0
    for line in log_file:
        _num += 1
        remote_adr = (line[0: line.find(' ')])
        line = line.split('"')[1].split(' ')
        # В request может быть всё что угодно
        # Считаем, что первое поле - request_type, последнее - протокол
        if len(line) == 3:
            request_type = line.pop(0)
            line.pop()
            requested_resource = "".join(line)
        else:
            print(f"Ошибка разбора запроса в строке: {_num}")
            print(line)
        result.append((remote_adr, request_type, requested_resource))
print(result)
