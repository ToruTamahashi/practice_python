is_empty = None

# Noneを判定する
if is_empty == None:
    print('None!!')

if is_empty is None:
    print('NoneNone')

if is_empty is not None:
    print('NoneNone')

# == は1という値がTrueかどうか判定するのでTrue
print(1 == True)
# is は左右のオブジェクトが同じものであるかを判定するのでFalse
print(1 is True)


# とにかくNoneを判定するときはisを使おう！