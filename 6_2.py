_req_list = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        remote_ip = line[0:line.find(' ')]
        if _req_list.get(remote_ip):
            _req_list[remote_ip] += 1
        else:
            _req_list[remote_ip] = 1

spammer_ip = ''
spammer_req_cnt = 0
for _ip, _req_cnt in _req_list.items():
    if spammer_req_cnt < _req_cnt:
        spammer_ip = _ip
        spammer_req_cnt = _req_cnt

print(f"Адрес спамера: {spammer_ip}, количество запросов: {spammer_req_cnt}")
