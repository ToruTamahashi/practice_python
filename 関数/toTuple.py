# 引数をタプルにまとめて渡す
# 渡される引数の数が不定の時に有効
# 引数の変数の前に＊をつけると渡された引数がタプルにまとめられる
def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi','Mike','Nance')


# 一つ目は普通に渡して残りをタプルにする
def say_something2(word,*args):
    print('word= ',word)
    for arg in args:
        print(arg)

say_something2('Hi','Mike','Nance')