# range関数
# iを0から10-1までイテレーションする(10回ループ)
for i in range(10):
    print(i)

# スタートの値を指定できる
for i in range(2,10):
    print(i)

# イテレーションの値も指定できる（何個飛ばしにするか)
for i in range(2,10,3):
    print(i)

# ループする際にiを使わない（定義したくない）場合_(アンダースコア)を入れる
for _ in range(10):
    print('hello')