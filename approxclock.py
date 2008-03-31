#
# Copyright (c) 2008 Mike Williams <mrw@eandem.co.uk>
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
# o Short a long versions (e.g. whether to include 'minutes' as in x minutes past/to y
# o Run fast slow but x mins
# o Split hour and min calculations from string generation
# o Resolutions - hour, half hour, quarter hour, 5 mins
# o noon or midday
#

def hour_str(hour, minutes):
    """Return hour as colloquial string."""
    h = hour%12
    if h == 0:
        if hour == 12:
            return 'Midday'
        if hour == 0:
            return 'Midnight'
    if minutes == 0:
        return '%s o\'clock' % (h)
    else:
        return '%s' % (h)

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
        return '%s.' % hour_str(hour, mins)
    elif mins < 7:
        return '%s past %s.' % (per_5_mins[mins], hour_str(hour, mins))
    else:
        return '%s to %s.' % (per_5_mins[12 - mins], hour_str((hour + 1)%24, mins))

if __name__ == '__main__':
    for hour in [0, 3, 8, 11, 15, 23]:
        for minute in [0, 5, 13, 18, 29, 36, 47, 54]:
            print approx_time(hour, minute)

#eof
