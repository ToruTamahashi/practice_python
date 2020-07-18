d = {'x':10,'y':20}
d['z'] = 100

print(d)

print(d.pop('x'))


# 指定のキーがあるか検索
print('y' in d)

# 辞書型にも値渡しと参照渡しがある
x = {'a':1}
y = x.copy()
#空にする
d.clear()
print(d)