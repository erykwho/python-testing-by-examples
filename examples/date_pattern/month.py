class MonthPattern(object):
    def __init__(self, month):
        self.month = month

    def matches(self, date):
        return self.month == date.month


