import os
import json

folder = r'some_data'

if not os.path.isdir(folder):
    exit(1)

files_stat = {}

for file in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, file)):
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        key = 10 ** len(str(os.stat(os.path.join(folder, file)).st_size))
        val = files_stat.setdefault(key, (1, [ext]))
        if val != (1, [ext]):
            cnt, ext_list = val
            cnt += 1
            if ext not in ext_list:
                ext_list.append(ext)
            files_stat[key] = (cnt, ext_list)

for k in sorted(files_stat.keys()):
    print(k, ':', files_stat[k])

json_name = os.path.split(folder)[1]
if not json_name:
    json_name = folder

with open(f"{json_name}_summary.json", 'w', encoding='utf-8') as file:
    json.dump(files_stat, file)
