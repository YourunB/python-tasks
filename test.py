from datetime import datetime

print(datetime.strptime("2023-31-12T23:59:59", "%Y-%d-%mT%H:%M:%S"))
print(datetime.now())
print(datetime.now().time())