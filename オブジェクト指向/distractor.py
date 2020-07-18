# クラスの初期化
class Person(object):
    def __init__(self, name):
        self.name = name
        print('First',self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))

    # delメソッドでインスタンスが削除されたとき、プログラム終了時に呼ばれる
    def __del__(self):
        print('goodbye')
person = Person('Mike')

# del person
print('############333')
