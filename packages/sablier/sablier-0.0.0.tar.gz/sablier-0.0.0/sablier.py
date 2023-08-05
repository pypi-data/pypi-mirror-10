"""
Python API to play with date, time and timezones

Say we want to find out what time it is in Sydney when it is 10 amd in Japan on
the 20th of May 2015:

    >>> from sablier import In
    >>> In('Japan').On(2015, 5, 20).At(11).time_in('Sydney')
    datetime.time(12, 0)

Or better based on an epoch timestamp, in Singapore, at 11:30, what is the
date time in Paris:

    >>> from sablier import Epoch
    >>> Epoch(1432083030).In('Singapore').At(11, 30).datetime_in('Paris')
    datetime.datetime(2015, 5, 20, 5, 30, tzinfo=<DstTzInfo 'Europe/Paris' CEST+2:00:00 DST>)
"""

import datetime

import pytz


class Sablier(object):
    """Date, time and timezone for the rest of us."""

    def __init__(self, date=None, time=datetime.time(0), timezone='UTC'):
        self.date = date
        self.time = time
        self.timezone = pytz.timezone(disambiguate(timezone))

    def On(self, date_or_year, month=None, day=None):
        """Chainable date setter"""
        if isinstance(date_or_year, datetime.date):
            self.date = date_or_year
        else:
            if month is None:
                raise TypeError('month required (pos 2)')
            if day is None:
                raise TypeError('day required (pos 3)')
            self.date = datetime.date(date_or_year, month, day)
        return self

    def At(self, time_or_hour, minute=0, second=0):
        """Chainable time setter"""
        if isinstance(time_or_hour, datetime.time):
            self.time = time_or_hour
        else:
            self.time = datetime.time(time_or_hour, minute, second)
        return self

    def In(self, timezone):
        """Change timezone and return a new Sablier instance"""
        dt = self.datetime_in(timezone)
        return Sablier(dt.date(), dt.time(), timezone)

    @property
    def datetime(self):
        """Localized datetime"""
        try:
            year, month, day = self.date.year, self.date.month, self.date.day
        except AttributeError:
            raise InvalidDate()
        try:
            hour, minute, second = self.time.hour, self.time.minute, self.time.second
        except AttributeError:
            raise InvalidTime()
        return self.timezone.localize(datetime.datetime(year, month, day,
                                                        hour, minute, second))

    def datetime_in(self, timezone):
        """Change timezone and return datetime.datetime"""
        timezone = disambiguate(timezone)
        return self.datetime.astimezone(pytz.timezone(timezone))

    def date_in(self, timezone):
        """Change timezone and return datetime.date"""
        return self.datetime_in(timezone).date()

    def time_in(self, timezone):
        """Change timezone and return datetime.time"""
        return self.datetime_in(timezone).time()

    def __repr__(self):
        return "Sablier(%r, %r, '%s')" % (self.date, self.time, self.timezone.zone)

def disambiguate(timezone):
    """Disambiguates timezone string, raise AmbiguousTimezone"""
    if timezone not in pytz.all_timezones:
        candidates = [candidate for candidate in pytz.all_timezones if timezone in candidate]
    else:
        candidates = [timezone]
    if len(candidates) > 1:
        raise AmbiguousTimezone('%s: use one of %s' % (timezone, candidates))
    return candidates[0]

def On(*args):
    """Date constructor"""
    if not isinstance(args[0], datetime.date):
        date = datetime.date(*args)
    else:
        date = args[0]
    return Sablier(date)

def At(*args):
    """Time constructor"""
    if not isinstance(args[0], datetime.time):
        time = datetime.time(*args)
    else:
        time = args[0]
    return Sablier(time=time)

def In(timezone):
    """Timezone constructor"""
    return Sablier(timezone=timezone)

def Epoch(timestamp):
    """Epoch timestamp constructor"""
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    return Sablier(date=dt.date(), time=dt.time(), timezone='UTC')

class SablierError(Exception):
    """Generic sablier exception"""
    pass

class AmbiguousTimezone(SablierError):
    """Raised when can't disambiguate and timezone string"""
    pass

class InvalidDate(SablierError):
    """Raised when date is not or improperly set"""
    pass

class InvalidTime(SablierError):
    """Raised when time is not or improperly set"""
    pass
