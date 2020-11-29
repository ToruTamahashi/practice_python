import datetime

t = datetime.time(12, 15, 0, 0)
print(t)
print(t.hour)

# 12時15分の一分後
dt1 = datetime.datetime.combine(datetime.date.today(), t) + datetime.timedelta(minutes=1)
t = datetime.time(dt1.hour, dt1.minute, 0, 0)
print(t)