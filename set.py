# 集合型
# 集合型は重複する値が消されて保存される
a = {1,1,2,3,4,4,5,6}
print(a)

x = {1,2,3}
y = {2,4,6}
# 差集合
print(x - y)

# キャップ
print(x & y)

# カップ
print(x | y)

s = {1,2,3,4,5}
# データ追加
s.add(6)
print(s)

# データ削除
s.remove(6)
print(s)