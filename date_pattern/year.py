class YearPattern(object):
    def __init__(self, year):
        self.year = year

    def matches(self, date):
        return self.year == date.year


