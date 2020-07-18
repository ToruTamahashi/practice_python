n = [1,4,5,6,7,9]
# 末尾に追加
n.append(100)
print(n)

# 任意の位置の挿入
n.insert(2,20)
print(n)


# 先頭を取り出す
print(n.pop(0))
# 末尾取り出す
print(n.pop())

# インデックス削除
del n[0]
print(n)


# リスト同士を結合
x = [1,2,3,4,5]
y = [6,7,8,9,10]
print(x+y)
x.extend(y)
print(x)