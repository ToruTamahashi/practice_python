import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # このクラスを継承したサブクラスは必ずdriveメソッドを実装しなければならない（してないとエラーになる）
    @abc.abstractmethod
    def drive(self):
        pass