# default引数は引数に何も値が渡されなかったときに代わりに入れる値を設定しておくこと
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ',dessert)

menu()
menu(entree='chicken')


# リストや辞書をデフォルト引数にするときはNoneで設定し関数内で初期化を行うこと
# 参照渡しなので前の値を引き継いでしまうから
def test_func(x, l=None):
 if l is None:
     l = []
 l.append(x)
 return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)

