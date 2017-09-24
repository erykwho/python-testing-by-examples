import datetime


class LastDayInMonthPattern(object):
    def matches(self, date):
        tomorrow = date + datetime.timedelta(1)
        return date.month != tomorrow.month