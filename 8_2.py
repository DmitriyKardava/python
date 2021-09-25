import re

with open('nginx_logs.txt') as log_file:
    re_line = re.compile(r'^(\S+).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) .*$|^$')

    for line in log_file:
        print(re.findall(re_line, line))
