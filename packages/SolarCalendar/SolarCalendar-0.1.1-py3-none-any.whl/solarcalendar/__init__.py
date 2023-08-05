"""SolarCalendar printing functions

these calendars have Saturday as the first day of the week, and
Friday as the last (the Iranian convention). Use setfirstweekday() to
set the first day of the week (0=Saturday, 6=Friday)."""
import locale as _locale
import sys
from itertools import repeat

import jdatetime

__all__ = ["IllegalMonthError", "IllegalWeekdayError", "setfirstweekday",
           "firstweekday", "isleap", "leapdays", "weekday", "monthrange",
           "monthcalendar", "prmonth", "month", "prcal", "calendar", "timegm",
           "month_name", "month_abbr", "day_name", "day_abbr",
           "SolarCalendar", "TextSolarCalendar",
           "HTMLSolarCalendar", "LocaleTextSolarCalendar",
           "LocaleHTMLSolarCalendar", "weekheader", ]

# Exception raised for bad input (with string parameter for details)
error = ValueError


# Exceptions raised for bad input


class IllegalMonthError(ValueError):
    def __init__(self, month):
        self.month = month

    def __str__(self):
        return "bad month number {}; must be 1-12".format(self.month)


class IllegalWeekdayError(ValueError):
    def __init__(self, weekday):
        self.weekday = weekday

    def __str__(self):
        return "bad weekday number {}; must be 0 (Saturday) to 6 (Friday)".format(
            self.weekday
        )


# Constants for months referenced later
Farvardin = 1
ESFAND = 12

# Number of days per month (except for Esfand in leap years)
mdays = [0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]


class _localized_month:
    _months = [jdatetime.date(1360, i + 1, 1).strftime for i in range(12)]
    _months.insert(0, lambda x: "")

    def __init__(self, format):
        self.format = format

    def __getitem__(self, i):
        funcs = self._months[i]
        if isinstance(i, slice):
            return [f(self.format) for f in funcs]
        else:
            return funcs(self.format)

    def __len__(self):
        return 13


class _localized_day:
    # 1 Farvardin, 1360, was a Saturday.
    _days = [jdatetime.date(1360, 1, i + 1).strftime for i in range(7)]

    def __init__(self, format):
        self.format = format

    def __getitem__(self, i):
        funcs = self._days[i]
        if isinstance(i, slice):
            return [f(self.format) for f in funcs]
        else:
            return funcs(self.format)

    def __len__(self):
        return 7


# Full and abbreviated names of weekdays
day_name = _localized_day("%A")
day_abbr = _localized_day("%a")

# Full and abbreviated names of months (1-based arrays!!!)
month_name = _localized_month("%B")
month_abbr = _localized_month("%b")

# Constants for weekdays
(SATURDAY, SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY) = range(7)


def isleap(year):
    """Return True for leap years, False for non-leap years."""
    remaining = year % 33
    leap_year_remaining = [1, 5, 9, 13, 17, 26, 30]
    if remaining in leap_year_remaining:
        return True
    elif 1244 < year < 1343:
        if remaining == 21:
            return True
    else:
        if remaining == 22:
            return True

    return False


def leapdays(year1, year2):
    """Return number of leap years in range [y1, y2)."""
    assert year1 <= year2
    return sum(map(lambda y: 1 if isleap(y) else 0, range(year1, year2)))


def weekday(year, month, day):
    """Return weekday (0-6 ~ Sat-Fri) for year, month (1-12), day (1-31)."""
    assert jdatetime.MINYEAR <= year <= jdatetime.MAXYEAR
    return jdatetime.date(year, month, day).weekday()


def _monthlen(year, month):
    return mdays[month] + (month == ESFAND and isleap(year))


def monthrange(year, month):
    """Return weekday (0-6 ~ Sat-Fri) and number of days (29-31) for
    year, month."""
    if not 1 <= month <= 12:
        raise IllegalMonthError(month)
    day1 = weekday(year, month, 1)
    ndays = _monthlen(year, month)
    return day1, ndays


def _prevmonth(year, month):
    if month == 1:
        return year - 1, 12
    else:
        return year, month - 1


def _nextmonth(year, month):
    if month == 12:
        return year + 1, 1
    else:
        return year, month + 1


class SolarCalendar(object):
    """
    Base calendar class. This class doesn't do any formatting. It simply
    provides data to subclasses.
    """

    def __init__(self, firstweekday=0):
        self.firstweekday = firstweekday  # 0 = Saturday, 6 = Friday

    def getfirstweekday(self):
        return self._firstweekday % 7

    def setfirstweekday(self, firstweekday):
        self._firstweekday = firstweekday

    firstweekday = property(getfirstweekday, setfirstweekday)

    def iterweekdays(self):
        """
        Return an iterator for one week of weekday numbers starting with the
        configured first one.
        """
        for i in range(self.firstweekday, self.firstweekday + 7):
            yield i % 7

    def itermonthdates(self, year, month):
        """
        Return an iterator for one month. The iterator will yield jdatetime.date
        values and will always iterate through complete weeks, so it will yield
        dates outside the specified month.
        """
        for y, m, d in self.itermonthdays3(year, month):
            yield jdatetime.date(y, m, d)

    def itermonthdays(self, year, month):
        """
        Like itermonthdates(), but will yield day numbers. For days outside
        the specified month the day number is 0.
        """
        day1, ndays = monthrange(year, month)
        days_before = (day1 - self.firstweekday) % 7
        yield from repeat(0, days_before)
        yield from range(1, ndays + 1)
        days_after = (self.firstweekday - day1 - ndays) % 7
        yield from repeat(0, days_after)

    def itermonthdays2(self, year, month):
        """
        Like itermonthdates(), but will yield (day number, weekday number)
        tuples. For days outside the specified month the day number is 0.
        """
        for i, d in enumerate(self.itermonthdays(year, month),
                              self.firstweekday):
            yield d, i % 7

    def itermonthdays3(self, year, month):
        """
        Like itermonthdates(), but will yield (year, month, day) tuples.  Can be
        used for dates outside of jdatetime.date range.
        """
        day1, ndays = monthrange(year, month)
        days_before = (day1 - self.firstweekday) % 7
        days_after = (self.firstweekday - day1 - ndays) % 7
        y, m = _prevmonth(year, month)
        end = _monthlen(y, m) + 1
        for d in range(end - days_before, end):
            yield y, m, d
        for d in range(1, ndays + 1):
            yield year, month, d
        y, m = _nextmonth(year, month)
        for d in range(1, days_after + 1):
            yield y, m, d

    def itermonthdays4(self, year, month):
        """
        Like itermonthdates(), but will yield (year, month, day, day_of_week) tuples.
        Can be used for dates outside of jdatetime.date range.
        """
        for i, (y, m, d) in enumerate(self.itermonthdays3(year, month)):
            yield y, m, d, (self.firstweekday + i) % 7

    def monthdatescalendar(self, year, month):
        """
        Return a matrix (list of lists) representing a month's calendar.
        Each row represents a week; week entries are jdatetime.date values.
        """
        dates = list(self.itermonthdates(year, month))
        return [dates[i: i + 7] for i in range(0, len(dates), 7)]

    def monthdays2calendar(self, year, month):
        """
        Return a matrix representing a month's calendar.
        Each row represents a week; week entries are
        (day number, weekday number) tuples. Day numbers outside this month
        are zero.
        """
        days = list(self.itermonthdays2(year, month))
        return [days[i: i + 7] for i in range(0, len(days), 7)]

    def monthdayscalendar(self, year, month):
        """
        Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
        """
        days = list(self.itermonthdays(year, month))
        return [days[i: i + 7] for i in range(0, len(days), 7)]

    def yeardatescalendar(self, year, width=3):
        """
        Return the data for the specified year ready for formatting. The return
        value is a list of month rows. Each month row contains up to width months.
        Each month contains between 4 and 6 weeks and each week contains 1-7
        days. Days are jdatetime.date objects.
        """
        months = [
            self.monthdatescalendar(year, i) for i in
            range(Farvardin, Farvardin + 12)
        ]
        return [months[i: i + width] for i in range(0, len(months), width)]

    def yeardays2calendar(self, year, width=3):
        """
        Return the data for the specified year ready for formatting (similar to
        yeardatescalendar()). Entries in the week lists are
        (day number, weekday number) tuples. Day numbers outside this month are
        zero.
        """
        months = [
            self.monthdays2calendar(year, i) for i in
            range(Farvardin, Farvardin + 12)
        ]
        return [months[i: i + width] for i in range(0, len(months), width)]

    def yeardayscalendar(self, year, width=3):
        """
        Return the data for the specified year ready for formatting (similar to
        yeardatescalendar()). Entries in the week lists are day numbers.
        Day numbers outside this month are zero.
        """
        months = [self.monthdayscalendar(year, i)
                  for i in range(Farvardin, Farvardin + 12)]
        return [months[i: i + width] for i in range(0, len(months), width)]


class TextSolarCalendar(SolarCalendar):
    """
    Subclass of Calendar that outputs a calendar as a simple plain text
    similar to the UNIX program cal.
    """

    def prweek(self, theweek, width):
        """
        Print a single week (no newline).
        """
        print(self.formatweek(theweek, width), end="")

    def formatday(self, day, weekday, width):
        """
        Returns a formatted day.
        """
        s = "" if day == 0 else "%2i" % day  # right-align single-digit days
        return s.center(width)

    def formatweek(self, theweek, width):
        """
        Returns a single week in a string (no newline).
        """
        return " ".join(self.formatday(d, wd, width) for (d, wd) in theweek)

    def formatweekday(self, day, width):
        """
        Returns a formatted week day name.
        """
        names = day_name if width >= 9 else day_abbr
        return names[day][:width].center(width)

    def formatweekheader(self, width):
        """
        Return a header for a week.
        """
        return " ".join(
            self.formatweekday(i, width) for i in self.iterweekdays())

    def formatmonthname(self, theyear, themonth, width, withyear=True):
        """
        Return a formatted month name.
        """
        s = month_name[themonth]
        if withyear:
            s = "%s %r" % (s, theyear)
        return s.center(width)

    def prmonth(self, theyear, themonth, w=0, l=0):
        """
        Print a month's calendar.
        """
        print(self.formatmonth(theyear, themonth, w, l), end="")

    def formatmonth(self, theyear, themonth, w=0, l=0):
        """
        Return a month's calendar string (multi-line).
        """
        w = max(2, w)
        l = max(1, l)
        s = self.formatmonthname(theyear, themonth, 7 * (w + 1) - 1)
        s = s.rstrip()
        s += "\n" * l
        s += self.formatweekheader(w).rstrip()
        s += "\n" * l
        for week in self.monthdays2calendar(theyear, themonth):
            s += self.formatweek(week, w).rstrip()
            s += "\n" * l
        return s

    def formatyear(self, theyear, w=2, l=1, c=6, m=3):
        """
        Returns a year's calendar as a multi-line string.
        """
        w = max(2, w)
        l = max(1, l)
        c = max(2, c)
        colwidth = (w + 1) * 7 - 1
        v = []
        a = v.append
        a(repr(theyear).center(colwidth * m + c * (m - 1)).rstrip())
        a("\n" * l)
        header = self.formatweekheader(w)
        for (i, row) in enumerate(self.yeardays2calendar(theyear, m)):
            # months in this row
            months = range(m * i + 1, min(m * (i + 1) + 1, 13))
            a("\n" * l)
            names = (self.formatmonthname(theyear, k, colwidth, False)
                     for k in months)
            a(formatstring(names, colwidth, c).rstrip())
            a("\n" * l)
            headers = (header for k in months)
            a(formatstring(headers, colwidth, c).rstrip())
            a("\n" * l)
            # max number of weeks for this row
            height = max(len(cal) for cal in row)
            for j in range(height):
                weeks = []
                for cal in row:
                    if j >= len(cal):
                        weeks.append("")
                    else:
                        weeks.append(self.formatweek(cal[j], w))
                a(formatstring(weeks, colwidth, c).rstrip())
                a("\n" * l)
        return "".join(v)

    def pryear(self, theyear, w=0, l=0, c=6, m=3):
        """Print a year's calendar."""
        print(self.formatyear(theyear, w, l, c, m), end="")


class HTMLSolarCalendar(SolarCalendar):
    """
    This calendar returns complete HTML pages.
    """

    # CSS classes for the day <td>s
    cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    # CSS classes for the day <th>s
    cssclasses_weekday_head = cssclasses

    # CSS class for the days before and after current month
    cssclass_noday = "noday"

    # CSS class for the month's head
    cssclass_month_head = "month"

    # CSS class for the month
    cssclass_month = "month"

    # CSS class for the year's table head
    cssclass_year_head = "year"

    # CSS class for the whole year table
    cssclass_year = "year"

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = "".join(self.formatday(d, wd) for (d, wd) in theweek)
        return "<tr>%s</tr>" % s

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (
            self.cssclasses_weekday_head[day],
            day_abbr[day],
        )

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = "".join(self.formatweekday(i) for i in self.iterweekdays())
        return "<tr>%s</tr>" % s

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = "%s %s" % (month_name[themonth], theyear)
        else:
            s = "%s" % month_name[themonth]
        return '<tr><th colspan="7" class="%s">%s</th></tr>' % (
            self.cssclass_month_head,
            s,
        )

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a(
            '<table border="0" cellpadding="0" cellspacing="0" class="%s">'
            % (self.cssclass_month)
        )
        a("\n")
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a("\n")
        a(self.formatweekheader())
        a("\n")
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a("\n")
        a("</table>")
        a("\n")
        return "".join(v)

    def formatyear(self, theyear, width=3):
        """
        Return a formatted year as a table of tables.
        """
        v = []
        a = v.append
        width = max(width, 1)
        a(
            '<table border="0" cellpadding="0" cellspacing="0" class="%s">'
            % self.cssclass_year
        )
        a("\n")
        a(
            '<tr><th colspan="%d" class="%s">%s</th></tr>'
            % (width, self.cssclass_year_head, theyear)
        )
        for i in range(Farvardin, Farvardin + 12, width):
            # months in this row
            months = range(i, min(i + width, 13))
            a("<tr>")
            for m in months:
                a("<td>")
                a(self.formatmonth(theyear, m, withyear=False))
                a("</td>")
            a("</tr>")
        a("</table>")
        return "".join(v)

    def formatyearpage(self, theyear, width=3, css="calendar.css",
                       encoding=None):
        """
        Return a formatted year as a complete HTML page.
        """
        if encoding is None:
            encoding = sys.getdefaultencoding()
        v = []
        a = v.append
        a('<!DOCTYPE html>\n' % encoding)
        a("<html>\n")
        a("<head>\n")
        a(
            '<meta http-equiv="Content-Type" content="text/html; charset=%s" />\n'
            % encoding
        )
        if css is not None:
            a('<link rel="stylesheet" type="text/css" href="%s" />\n' % css)
        a("<title>Solar  Calendar for %d</title>\n" % theyear)
        a("</head>\n")
        a("<body>\n")
        a(self.formatyear(theyear, width))
        a("</body>\n")
        a("</html>\n")
        return "".join(v).encode(encoding, "xmlcharrefreplace")


class different_locale:
    def __init__(self, locale):
        self.locale = locale

    def __enter__(self):
        self.oldlocale = _locale.getlocale(_locale.LC_TIME)
        _locale.setlocale(_locale.LC_TIME, self.locale)

    def __exit__(self, *args):
        _locale.setlocale(_locale.LC_TIME, self.oldlocale)


class LocaleTextSolarCalendar(TextSolarCalendar):
    """
    This class can be passed a locale name in the constructor and will return
    month and weekday names in the specified locale. If this locale includes
    an encoding all strings containing month and weekday names will be returned
    as unicode.
    """

    def __init__(self, firstweekday=0, locale=None):
        TextSolarCalendar.__init__(self, firstweekday)
        if locale is None:
            locale = _locale.getdefaultlocale()
        self.locale = locale

    def formatweekday(self, day, width):
        with different_locale(self.locale):
            if width >= 9:
                names = day_name
            else:
                names = day_abbr
            name = names[day]
            return name[:width].center(width)

    def formatmonthname(self, theyear, themonth, width, withyear=True):
        with different_locale(self.locale):
            s = month_name[themonth]
            if withyear:
                s = "%s %r" % (s, theyear)
            return s.center(width)


class LocaleHTMLSolarCalendar(HTMLSolarCalendar):
    """
    This class can be passed a locale name in the constructor and will return
    month and weekday names in the specified locale. If this locale includes
    an encoding all strings containing month and weekday names will be returned
    as unicode.
    """

    def __init__(self, firstweekday=0, locale=None):
        HTMLSolarCalendar.__init__(self, firstweekday)
        if locale is None:
            locale = _locale.getdefaultlocale()
        self.locale = locale

    def formatweekday(self, day):
        with different_locale(self.locale):
            s = day_abbr[day]
            return '<th class="%s">%s</th>' % (self.cssclasses[day], s)

    def formatmonthname(self, theyear, themonth, withyear=True):
        with different_locale(self.locale):
            s = month_name[themonth]
            if withyear:
                s = "%s %s" % (s, theyear)
            return '<tr><th colspan="7" class="month">%s</th></tr>' % s


# Support for old module level interface
c = TextSolarCalendar()

firstweekday = c.getfirstweekday


def setfirstweekday(firstweekday):
    if not SATURDAY <= firstweekday <= FRIDAY:
        raise IllegalWeekdayError(firstweekday)
    c.firstweekday = firstweekday


monthcalendar = c.monthdayscalendar
prweek = c.prweek
week = c.formatweek
weekheader = c.formatweekheader
prmonth = c.prmonth
month = c.formatmonth
calendar = c.formatyear
prcal = c.pryear

# Spacing of month columns for multi-column year calendar
_colwidth = 7 * 3 - 1  # Amount printed by prweek()
_spacing = 6  # Number of spaces between columns


def format(cols, colwidth=_colwidth, spacing=_spacing):
    """Prints multi-column formatting for year calendars"""
    print(formatstring(cols, colwidth, spacing))


def formatstring(cols, colwidth=_colwidth, spacing=_spacing):
    """Returns a string formatted from n strings, centered within n columns."""
    spacing *= " "
    return spacing.join(c.center(colwidth) for c in cols)


EPOCH = 1340
_EPOCH_ORD = jdatetime.date(EPOCH, 1, 1).toordinal()


def timegm(tuple):
    """Unrelated but handy function to calculate Unix timestamp from GMT."""
    year, month, day, hour, minute, second = tuple[:6]
    days = jdatetime.date(year, month, 1).toordinal() - _EPOCH_ORD + day - 1
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    seconds = minutes * 60 + second
    return seconds


def main(args):
    import argparse

    parser = argparse.ArgumentParser()
    textgroup = parser.add_argument_group("text only arguments")
    htmlgroup = parser.add_argument_group("html only arguments")
    textgroup.add_argument(
        "-w", "--width", type=int, default=2,
        help="width of date column (default 2)"
    )
    textgroup.add_argument(
        "-l",
        "--lines",
        type=int,
        default=1,
        help="number of lines for each week (default 1)",
    )
    textgroup.add_argument(
        "-s",
        "--spacing",
        type=int,
        default=6,
        help="spacing between months (default 6)",
    )
    textgroup.add_argument(
        "-m", "--months", type=int, default=3,
        help="months per row (default 3)"
    )
    htmlgroup.add_argument(
        "-c", "--css", default="calendar.css", help="CSS to use for page"
    )
    parser.add_argument(
        "-L",
        "--locale",
        default=None,
        help="locale to be used from month and weekday names",
    )
    parser.add_argument(
        "-e", "--encoding", default=None, help="encoding to use for output"
    )
    parser.add_argument(
        "-t",
        "--type",
        default="text",
        choices=("text", "html"),
        help="output type (text or html)",
    )
    parser.add_argument("year", nargs="?", type=int,
                        help="year number (1-9999)")
    parser.add_argument(
        "month", nargs="?", type=int, help="month number (1-12, text only)"
    )

    options = parser.parse_args(args[1:])

    if options.locale and not options.encoding:
        parser.error("if --locale is specified --encoding is required")
        sys.exit(1)

    locale = options.locale, options.encoding

    if options.type == "html":
        if options.locale:
            cal = LocaleHTMLSolarCalendar(locale=locale)
        else:
            cal = HTMLSolarCalendar()
        encoding = options.encoding
        if encoding is None:
            encoding = sys.getdefaultencoding()
        optdict = dict(encoding=encoding, css=options.css)
        write = sys.stdout.buffer.write
        if options.year is None:
            write(cal.formatyearpage(jdatetime.date.today().year, **optdict))
        elif options.month is None:
            write(cal.formatyearpage(options.year, **optdict))
        else:
            parser.error("incorrect number of arguments")
            sys.exit(1)
    else:
        if options.locale:
            cal = LocaleTextSolarCalendar(locale=locale)
        else:
            cal = TextSolarCalendar()
        optdict = dict(w=options.width, l=options.lines)
        if options.month is None:
            optdict["c"] = options.spacing
            optdict["m"] = options.months
        if options.year is None:
            result = cal.formatyear(jdatetime.date.today().year, **optdict)
        elif options.month is None:
            result = cal.formatyear(options.year, **optdict)
        else:
            result = cal.formatmonth(options.year, options.month, **optdict)
        write = sys.stdout.write
        if options.encoding:
            result = result.encode(options.encoding)
            write = sys.stdout.buffer.write
        write(result)


if __name__ == "__main__":
    main(sys.argv)
