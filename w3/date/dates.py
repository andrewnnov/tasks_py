import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2021, 9, 21)
print(y)

print(y.strftime("%B"))

print(y.strftime("%x"))