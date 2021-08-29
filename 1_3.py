for percent in range(1, 101):
    if percent % 10 == 1 and 11 != percent % 100:
        print(percent, 'процент')
    elif 2 <= percent % 10 <= 4 and not 12 <= percent % 100 <= 14:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
