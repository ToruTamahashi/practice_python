class Car(object):
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    # 継承したメソッドを再定義（上書き）（override）
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model_S', enable_auto_run = False):
        # 上書きでなく、機能の追加をしたい場合はsuperメソッドで親メソッドを呼び出す
        super.__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        super()
        print('super fast')
    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print('###########')
toyota_car = ToyotaCar('Lexus')
toyota_car.run()
print('##############')
tesla_car = TeslaCar()
tesla_car.auto_run()
tesla_car.run()