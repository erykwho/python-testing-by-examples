import datetime


class LastWeekdayInMonthPattern(object):
    def __init__(self, weekday):
        self.weekday = weekday

    def matches(self, date):
        next_week = date + datetime.timedelta(7)
        return self.weekday == date.weekday() and next_week.month != date.month
