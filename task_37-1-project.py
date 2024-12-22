import datetime
from collections import Counter
from typing import List

def most_common_months(dates: List[str], n) -> List[int]:
    months = [datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").month for date in dates]
    month_counter = Counter(months)
    most_common = month_counter.most_common(n)
    return [month for month, count in most_common]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
