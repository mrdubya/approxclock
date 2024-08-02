# Copyright (c) 2008-2024 Mike Williams <mrmrdubya@gmail.com>
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
# o Split hour and min calculations from string generation
# o noon or midday
# o words or numbers - five past four, 4.05
# o morning/afternoon, am/pm, or not
#

import datetime
import getopt
import re
import sys


class ApproxClock(object):

    def __init__(self, fast=0, resolution=5, words=True, ampm=False, noon=True):
        self.__fast = fast
        self.__resolution = resolution
        self.__words = words
        self.__ampm = ampm
        self.__noon = noon

    def __hour(self, hour, minutes):
        """Return hour as colloquial string."""
        hours = [
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
        ]
        h = hour % 12
        if h == 0:
            if hour == 12:
                return "Midday"
            return "Midnight"
        if minutes == 0:
            return "%s o'clock" % (h)
        return "%s" % (hours[h - 1])

    def __minutes(self, minutes):
        # Map minutes to nearest resolution for the clock, all of which have 5
        # as a common factor
        return (
            (minutes + self.__resolution // 2) // self.__resolution * self.__resolution
        ) // 5

    def __str(self, hour, minutes):
        per_5_mins = ["Five", "Ten", "Quarter", "Twenty", "Twenty-five", "Half"]
        mins = self.__minutes(minutes)
        if mins == 0 or mins == 12:
            return "%s." % self.__hour(hour, mins)
        elif mins < 7:
            return "%s past %s." % (per_5_mins[mins - 1], self.__hour(hour, mins))
        else:
            return "%s to %s." % (
                per_5_mins[11 - mins],
                self.__hour((hour + 1) % 24, mins),
            )

    def time(self, hour, minutes):
        return self.__str(hour, minutes)

    def __str__(self):
        # Current time plus fast clock offset to the nearest minute
        time = datetime.datetime.now() + datetime.timedelta(
            seconds=(self.__fast * 60 + 30)
        )
        return self.__str(time.hour, time.minute)

    def __repr__(self):
        return "%s.%s(%s, %s, %s, %s, %s)" % (
            self.__class__.__module__,
            self.__class__.__name__,
            self.__fast,
            self.__resolution,
            self.__words,
            self.__ampm,
            self.__noon,
        )


_description = """Display the approximate time.

usage: atime [-h] [-f mins] [-r mins]

-h display this help
-f how many minutes fast the clock is.  Default is 0.
-r clock resolution - 5, 10, 15, or 20 minutes. Default is 5.
"""


def _usage(message):
    usage = re.search("^usage:.*", _description, re.MULTILINE).group()
    return f"{message}\n{usage}"


def main(argv=None):
    try:
        opts, pargs = getopt.getopt(argv, "f:hr:")
    except getopt.GetoptError as e:
        return _usage(e)

    # Process options
    resolution = 5
    fast = 0
    for option, value in opts:
        if option == "-h":
            print(f"{_description}")
            return 0

        elif option == "-f":  # Minutes fast
            fast = int(value)

        elif option == "-r":  # Clock resolution
            resolution = int(value)
            if resolution % 5 != 0 or resolution > 20:
                return _usage(f"Invalid clock resolution {resolution}.")

    print(ApproxClock(fast=fast, resolution=resolution))
    return 0


def atime():
    sys.exit(main(sys.argv[1:]))


# eof
