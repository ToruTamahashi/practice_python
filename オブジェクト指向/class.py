# クラスを定義するときはクラス引数にobjectを記述することが推奨される
# (後で使うから)


class Person(object):
    def say_something(self):
        print('hello')

person = Person()
person.say_something()