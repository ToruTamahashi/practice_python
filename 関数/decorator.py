# デコレーター；ある関数を実行する前に別の関数を実行したいときに使う

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    # 関数オブジェクトを返す
    return wrapper

"""
add_numが呼び出されたとき、代わりに@の先の関数を呼び出す
その際引数としてadd_num関数オブジェクトを引数funcとして渡され
add_numが受け取った引数10,20は内部関数wrapperに渡される

関数の実行の前後に特定の処理を付け加えたい場合に使う
"""
@print_info
def add_num(a,b):
    return a+b

r = add_num(10,20)
print(r)