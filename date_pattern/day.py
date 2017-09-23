class DayPattern(object):
    def __init__(self, day):
        self.day = day

    def matches(self, date):
        return self.day == date.day


