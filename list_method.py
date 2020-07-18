r = [1,2,3,7,6,5,4,8,9]

# 昇順ソート
r.sort()
print(r)

# 降順ソート
r.sort(reverse=True)
print(r)


s = 'My name is Mike'
# スプリット(スペースでスプリット)
to_sprit = s.split(' ')
print(to_sprit)

# 逆にスペースで結合
x = ' '.join(to_sprit)
print(x)


# 値渡しと参照渡し
i = [1,2,3,4,5]
j = i
j[0] = 100
print('i=',i)
print('j=',j)

x = [1,2,3,4,5]
y = x.copy()
y[0] = 100
print('x=',x)
print('y=',y)