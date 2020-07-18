# クラス内で定義された変数を外部から変更することを禁止したい(privateにする)
"""
 privateにしたい変数名の先頭に「　__　」を追加する(クラス内からはアクセスできる)
 ゲッターの追加-> ゲッターメソッドの上に@propertyを付与する
 (任意で)セッター -> @[ゲッターメソッド名].setter

 ゲッターとセッターのメソッド名は元の変数から__をとった名前にすること
"""
class Car(object):
    def __init__(self, model = None):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def run(self):
        print('run')


car = Car('test')
#car.model = 'aaa'
#print(car.model)
print(car.model)
car.model='123'
print(car.model)