import datetime

string_datetime = input()

def parse_time(s):
    dt = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    dt += datetime.timedelta(days=1)
    return dt.day

print(parse_time(string_datetime))
