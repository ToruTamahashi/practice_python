# クラスの初期化
class Person(object):
    def __init__(self, name):
        self.name = name
        print('First',self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))

# インスタンスを生成するとinitメソッド(コンストラクタ)が自動的に呼ばれる
person = Person('Mike')