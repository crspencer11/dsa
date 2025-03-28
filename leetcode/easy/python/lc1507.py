class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        date_parts = date.split(" ")
        day = date_parts[0][:-2]
        if len(day) == 1:
            day = "0" + day
        month = month_map[date_parts[1]]
        year = date_parts[2]
        return f"{year}-{month}-{day}"

