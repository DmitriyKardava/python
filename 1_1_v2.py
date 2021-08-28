durations_list = [87452, 60, 3601, 1, 600, 0, 601, -1, -200, 65536, 65535, 32768, -32767, 59, 23, 62]
time_intervals = {86400: ' дн ', 3600: ' час ', 60: ' мин ', 1: ' сек'}
for duration in durations_list:
    seconds_to_hstr = ''
    for seconds in time_intervals:
        if duration >= seconds or seconds_to_hstr:
            seconds_to_hstr += str(duration // seconds) + time_intervals[seconds]
            duration = duration % seconds
    if not seconds_to_hstr:
        seconds_to_hstr = '0 сек'
    print(seconds_to_hstr)
