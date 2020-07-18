import datetime

# 現在時刻の取得
now = datetime.datetime.now()
print(now)

# 国際標準形式で表示
print(now.isoformat())

# 表示形式を指定
print(now.strftime('%d/%m/%y-%H%M%S%f'))

# 今日の日付だけ取得
today = datetime.date.today()
print(today)
print(today.strftime('%d/%m/%y'))


# 日付格納
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.strftime('%H_%M_%S_%f'))


# 日付演算
print(now)
# timedeltaで一週間分の期間を取得
d = datetime.timedelta(weeks=1)
# d = datetime.timedelta(days=1)
# d = datetime.timedelta(hours=1)
# 一週間前の日付を表示
print(now - d)