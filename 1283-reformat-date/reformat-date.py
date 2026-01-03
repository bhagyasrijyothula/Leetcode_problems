from datetime import datetime
class Solution(object):
    def reformatDate(self, date):
        day,mnth,year=date.split()
        day=day[:-2]
        date_str = day + " " + mnth + " " + year
        date_obj = datetime.strptime(date_str, "%d %b %Y")
        return date_obj.strftime("%Y-%m-%d")
        