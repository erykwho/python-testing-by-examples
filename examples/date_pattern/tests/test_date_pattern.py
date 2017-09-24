# failUnless = assertTrue
# failIf = assertFalse

import datetime
import unittest

from date_pattern.composite import CompositePattern
from date_pattern.day import DayPattern
from date_pattern.last_day_in_month import LastDayInMonthPattern
from date_pattern.last_weekday_in_month import LastWeekdayInMonthPattern
from date_pattern.month import MonthPattern
from date_pattern.nth_weekday_in_month import NthWeekdayInMonthPattern
from date_pattern.weekday import WeekdayPattern
from date_pattern.year import YearPattern

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(0, 7)


class YearPatternTests(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2004, 9, 29)

    def test_year_pattern_matches(self):
        year_pattern = YearPattern(2004)
        self.assertTrue(year_pattern.matches(self.date))

    def test_year_pattern_does_not_match(self):
        year_pattern = YearPattern(2005)
        self.assertFalse(year_pattern.matches(self.date))


class MonthPatternTests(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2004, 9, 29)

    def test_month_pattern_matches(self):
        month_pattern = MonthPattern(9)
        self.assertTrue(month_pattern.matches(self.date))

    def test_month_pattern_does_not_match(self):
        month_pattern = MonthPattern(11)
        self.assertFalse(month_pattern.matches(self.date))


class DayPatternTests(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2004, 9, 29)

    def test_day_pattern_matches(self):
        day_pattern = DayPattern(29)
        self.assertTrue(day_pattern.matches(self.date))

    def test_day_pattern_does_not_match(self):
        day_pattern = DayPattern(21)
        self.assertFalse(day_pattern.matches(self.date))


class WeekdayPatternTests(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2004, 9, 29)

    def test_weekday_pattern_matches(self):
        weekday_pattern = WeekdayPattern(2)  # Wednesday
        self.assertTrue(weekday_pattern.matches(self.date))

    def test_weekday_pattern_does_not_match(self):
        weekday_pattern = WeekdayPattern(1)  # Tuesday
        self.assertFalse(weekday_pattern.matches(self.date))


class CompositePatternTests(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2004, 9, 29)

    def test_composite_matches(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        self.assertTrue(cp.matches(self.date))

    def test_composite_does_not_match(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(30))
        self.assertFalse(cp.matches(self.date))

    def test_composite_without_year_matches(self):
        cp = CompositePattern()
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        self.assertTrue(cp.matches(self.date))


class LastWeekdayPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = LastWeekdayInMonthPattern(WEDNESDAY)

    def test_last_wednesday_matches(self):
        last_wed_of_sept_2004 = datetime.date(2004, 9, 29)
        self.assertTrue(self.pattern.matches(last_wed_of_sept_2004))

    def test_last_wednesday_does_not_match(self):
        first_wed_of_sept_2004 = datetime.date(2004, 9, 1)
        self.assertFalse(self.pattern.matches(first_wed_of_sept_2004))


class NthWeekdayPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = NthWeekdayInMonthPattern(1, WEDNESDAY)

    def test_matches(self):
        first_wed_of_sept_2004 = datetime.date(2004, 9, 1)
        self.assertTrue(self.pattern.matches(first_wed_of_sept_2004))

    def test_does_not_matches(self):
        second_wed_of_sept_2004 = datetime.date(2004, 9, 8)
        self.assertFalse(self.pattern.matches(second_wed_of_sept_2004))


class LastDayInMonthPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = LastDayInMonthPattern()

    def test_matches(self):
        last_day_in_sept_2004 = datetime.date(2004, 9, 30)
        self.assertTrue(self.pattern.matches(last_day_in_sept_2004))

    def test_does_not_match(self):
        second_to_day_in_sept_2004 = datetime.date(2004, 9, 23)
        self.assertFalse(self.pattern.matches(second_to_day_in_sept_2004))


if __name__ == '__main__':   unittest.main()
