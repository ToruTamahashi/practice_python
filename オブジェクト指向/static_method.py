class Person(object):
    # このように記述すると変数kindはすべてのインスタンス間で共有される
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

# aboutメソッドはとくにPersonクラスないの変数と直接関係がないのでインスタンスを作らずに直接呼び出せる
Person.about(1999)
