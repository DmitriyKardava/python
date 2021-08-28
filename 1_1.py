durations_list = [1, 61, -1, 86399, 86401, -86401, 600,  234345345, 11345545, 999999999]
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
for duration in durations_list:
    _duration_sign = 1
    seconds_to_hstr = ''
    if duration < 0:
        duration = abs(duration)
        _duration_sign = -1
    if duration >= SECONDS_IN_DAY:
        days = duration // SECONDS_IN_DAY
        duration = duration % SECONDS_IN_DAY
        days = days * _duration_sign
        seconds_to_hstr += str(days) + ' дн '
    if duration >= SECONDS_IN_HOUR or seconds_to_hstr:
        hours = duration // SECONDS_IN_HOUR
        duration = duration % SECONDS_IN_HOUR
        hours = hours * _duration_sign
        seconds_to_hstr += str(hours) + ' час '
    if duration >= SECONDS_IN_MINUTE or seconds_to_hstr:
        minutes = duration // SECONDS_IN_MINUTE
        duration = duration % SECONDS_IN_MINUTE
        minutes = minutes * _duration_sign
        seconds_to_hstr += str(minutes) + ' мин '
    seconds = duration * _duration_sign
    seconds_to_hstr += str(seconds) + ' сек'
    print(seconds_to_hstr)
