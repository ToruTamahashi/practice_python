"""
クラス同士の間は2行分空ける
関数同氏は間に1行分空ける
importとその後には2行分空ける
グローバル変数の後は2行分空ける

クラス名はキャメルケース
変数、関数名はスネークケース
グローバル変数は大文字＋スネークケース
"""
import pandas
import numpy


DEFAULT_NAME = 'TAKA'


class Person():
    """ testClass """

    def test_func(self):
        print('aaa')

    def test_func2(self):
        print('bbb')


class Car():
    pass