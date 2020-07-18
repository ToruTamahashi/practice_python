def say_someting():
    print('hi')

say_someting()

# 関数も型のひとつ
#print(type(say_someting))

# なので関数を変数に格納することも可能
f = say_someting

f()
