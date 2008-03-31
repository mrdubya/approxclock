import time

import approxclock

hour, minute, secs = time.localtime()[3:6]
if secs >= 30:
    minute += 1
print approxclock.approx_time(hour, minute)

#eof
