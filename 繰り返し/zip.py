# 同じサイズの複数の変数を並列で表示したいとき
days = ['Mon','Tue','Wed']
fruits = ['apple','banana','orange']
drinks = ['coffee','tea','beer']
# 面倒な例
for i in range(len(days)):
    print(days[i],fruits[i],drinks[i])

# zip関数を使った例
# 対応する変数にループごとに配列の要素を格納する
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
