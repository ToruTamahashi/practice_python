"""
 コメント中にpython consoleを記述することでテストが可能
 >> > [操作]
 [期待する戻り値]
 ↑の形式で記述
"""
class Cal(object):
    def add_num_and_double(self, x, y):
        """Add and double
        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        5
        """
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()