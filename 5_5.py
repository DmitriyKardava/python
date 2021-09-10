src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dst = [_i for _i in src if src.count(_i) == 1]
print(dst)

dst = []
_tmp = set()
for _i in src:
    if _i not in _tmp:
        dst.append(_i)
    elif _i in dst:
        dst.remove(_i)
    _tmp.add(_i)
print(dst)

_tmp = {}
for _i in src:
    _tmp[_i] = 1 if not _tmp.get(_i) else _tmp[_i] + 1
dst = [key for key, val in _tmp.items() if val == 1]
print(dst)
