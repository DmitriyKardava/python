def currency_rates(cur):
    from requests import get, utils
    from decimal import Decimal
    import datetime as dt
    if not cur:
        return None
    cur = cur.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    _start = content.find('<Value>', content.find(cur))
    if _start < 0:
        return None
    else:
        _start += 7
    _stop = content.find('</Value>', content.find(cur))
    _date_str = content[content.find('ValCurs Date="') + 14:content.find('ValCurs Date="') + 24]
    result = Decimal(content[_start:_stop].replace(',', '.')).quantize(Decimal("1.00"))
    return result, dt.datetime.strptime(_date_str, '%d.%m.%Y').date()
