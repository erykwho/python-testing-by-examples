import datetime


class NthWeekdayInMonthPattern(object):
    def __init__(self, n, weekday):
        self.n = n
        self.weekday = weekday

    def matches(self, date):
        if self.weekday != date.weekday():
            return False

        return self.n == self._get_weekday_number(date)

    @staticmethod
    def _get_weekday_number(date):
        n = 1
        while True:
            previous_date = date - datetime.timedelta(7 * n)
            if previous_date.month == date.month:
                n += 1
            else:
                break
        return n