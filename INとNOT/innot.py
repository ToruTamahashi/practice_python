y = [1,2,3]
x = 1

# xの値がyに含まれていればtrue
if x in y:
    print('in')

# 100がyに含まれていなければtrue
if 100 not in y:
    print('not in')


a = 1
b = 2
# 数値を比較するときにnotは推奨されない（!=）があるから
if not a == b:
    print('Not equal')

is_ok = True
#if is_ok != True:
# bool型の判定を否定したい場合にnotを用いることが多い
if not is_ok:
    print('hello')


# 変数の中身が空かどうか判定する方法
str1 = ''
str2 = 'adfad'
str3 = []
"""
 分岐条件の部分でbool以外の変数を入れた場合
 中身が入っていればTrue
 何もなければFalseが帰る
 この性質を利用することでlen(str1)で配列長を求めなくても判定が可能になる
"""
if str2:
    print('あるよ')
else:
    print('ないよ')
