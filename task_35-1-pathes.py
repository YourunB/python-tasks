import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    start_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted_time = start_time + datetime.timedelta(days=days, seconds=seconds)
    return (shifted_time.day, shifted_time.second)

print(shift_time(days, seconds))
