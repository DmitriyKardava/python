prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
          48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
for price in prices:
    rub = int(price)
    kop = round((price - rub) * 100)
    if kop < 0:
        kop *= -1
    if kop < 10:
        kop = '0' + str(kop)
    print(f"{rub} руб {kop} коп")
print("-" * 32)
print(f"id списка до сортировки: {id(prices)}")
print(prices)
prices.sort()
print(f"id списка после сортировки: {id(prices)}")
print(prices)
print("-" * 32)

prices_2 = list(reversed(prices))
print(f"id списка, отсортированного по убыванию: {id(prices_2)}")
print(prices_2)
print("5 самых дорогих товаров по возрастанию цены")
for price in reversed(prices_2[0:5]):
    print(price, ' ', end='')
