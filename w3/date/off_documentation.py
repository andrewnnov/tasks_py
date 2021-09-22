import datetime
from datetime import date

now = date.today()
print(now.strftime("%m.%d.%y"))

print(datetime.date(2013, 12, 2))
print(now.strftime("%m.%d.%y"))