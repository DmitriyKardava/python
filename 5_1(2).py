def odd_nums(n):
    # for _i in range(1, n + 1, 2):
    #     yield _i
    return (n for n in range(1, n + 1, 2))


print(*odd_nums(101))
