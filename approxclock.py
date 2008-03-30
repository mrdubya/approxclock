
import time

def hour_str(hour, minutes):
    if minutes == 0 and hour == 12:
        return 'Midday'
    if hour == 0:
        return 'Midnight'
    if hour > 12:
        hour -= 12
    return str(hour)

def approx_time(hour, minute):
    per_5_mins = [
                'XXX',
                'Five',
                'Ten',
                'Quarter',
                'Twenty',
                'Twenty five',
                'Half',
            ]
    mins = int((minute + 2.5)/5)
    if mins == 0 or mins == 12:
        return '%s o\'clock.' % hour_str(hour, mins)
    elif mins < 7:
        return '%s minutes past %d.' % (per_5_mins[mins], hour_str(hour, mins))
    else:
        return '%s minutes to %s.' % (per_5_mins[12 - mins], hour_str((hour + 1)%23, mins))

hour, minute, secs = time.localtime()[3:6]
if secs >= 30:
    minute += 1
print approx_time(hour, minute)

#eof
