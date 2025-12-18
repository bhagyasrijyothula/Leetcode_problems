class Solution(object):
    def dayOfYear(self, date):
        year, mon, day = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            if mon > 2:
                day += 1
        day += sum(days[:mon - 1])
        return day
