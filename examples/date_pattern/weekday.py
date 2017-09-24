class WeekdayPattern(object):
    def __init__(self, weekday):
        self.weekday = weekday

    def matches(self, date):
        return self.weekday == date.weekday()


