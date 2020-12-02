# リストの中身をそれぞれ2倍する
def double(x):
    return x * 2
scores = [1, 2, 3]
# 第一引数に変換操作のための関数(double)
# 第二引数に変換対象(scores)
scores_double = map(double, scores)
for s in scores_double:
    print(s)