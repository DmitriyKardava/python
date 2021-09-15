import sys
if len(sys.argv) != 4:
    print("Задайте файлы для обработки:\n")
    quit()
with open(sys.argv[1], 'r', encoding='utf-8') as users_file, \
     open(sys.argv[2], 'r', encoding='utf-8') as hobbies_file, \
     open(sys.argv[3], 'w', encoding='utf-8') as result_file:
    while True:
        user = (users_file.readline().strip())
        hobby = hobbies_file.readline().strip()
        if hobby and not user:
            quit(1)
        if not user:
            break
        result_file.write(f"{user}: {hobby}\n")
