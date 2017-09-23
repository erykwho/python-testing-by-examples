class CompositePattern(object):
    def __init__(self):
        self.patterns = list()

    def add(self, pattern):
        self.patterns.append(pattern)

    def matches(self, date):
        for pattern in self.patterns:
            if not pattern.matches(date):
                return False
        return True
