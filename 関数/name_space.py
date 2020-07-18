# グローバルに関数内からアクセスしたいとき

animal = 'cat'

def f():
    # 手前にglobalをつける
    global animal
    animal = 'dog'

f()
print(animal)