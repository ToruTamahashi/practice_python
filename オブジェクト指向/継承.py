class Car(object):
    #pass
    def run(self):
        print('run')

class ToyotaCar(Car):
    # passは何もしないことを表す
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print('###########')
toyota_car = ToyotaCar()
toyota_car.run()
print('##############')
tesla_car = TeslaCar()
tesla_car.auto_run()
tesla_car.run()