# インスタンス間で変数を共有する
class Person(object):
    # このように記述すると変数kindはすべてのインスタンス間で共有される
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()