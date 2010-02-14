#! /usr/local/bin/python
#
# Copyright (c) 2008-2010 Mike Williams <mrw@eandem.co.uk>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

# Ideas:
# o Run fast or slow by x mins
# o Split hour and min calculations from string generation
# o Resolutions - hour, half hour, quarter hour, 5 mins
# o noon or midday
# o words or numbers - five past four, 4.05
# o morning/afternoon, am/pm, or not
#

import datetime

class ApproxClock(object):

    def __init__(self, fast=0, words=True, ampm=False, noon=True):
        self.__fast = fast
        self.__words = words
        self.__ampm = ampm
        self.__noon = noon

    def __hour(self, hour, minutes):
        """Return hour as colloquial string."""
        hours = [ 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                'Eight', 'Nine', 'Ten', 'Eleven' ]
        h = hour%12
        if h == 0:
            if hour == 12:
                return 'Midday'
            if hour == 0:
                return 'Midnight'
        if minutes == 0:
            return '%s o\'clock' % (h)
        else:
            return '%s' % (hours[h - 1])

    def __str(self, hour, minutes):
        per_5_mins = [ 'Five', 'Ten', 'Quarter', 'Twenty', 'Twenty-five', 'Half' ]
        mins = (minutes + 2)/5
        if mins == 0 or mins == 12:
            return '%s.' % self.__hour(hour, mins)
        elif mins < 7:
            return '%s past %s.' % (per_5_mins[mins - 1], self.__hour(hour, mins))
        else:
            return '%s to %s.' % (per_5_mins[11 - mins], self.__hour((hour + 1)%24, mins))

    def time(self, hour, minutes):
        return self.__str(hour, minutes)

    def __str__(self):
        # Current time plus fast clock offset to the nearest minute
        time = datetime.datetime.now() + \
                datetime.timedelta(seconds=(self.__fast*60 + 30))
        return self.__str(time.hour, time.minute)

    def __repr__(self):
        return '%s.%s(%s, %s, %s, %s)' % (self.__class__.__module__,
                self.__class__.__name__, self.__fast, self.__words,
                self.__ampm, self.__noon)

if __name__ == '__main__':
    a = ApproxClock()
    print repr(a)
    for hour in [0, 3, 8, 11, 15, 23]:
        for minute in [0, 5, 13, 18, 29, 36, 47, 54]:
            print a.time(hour, minute)

#eof
