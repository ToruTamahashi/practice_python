# 間スペース
print("abc","def")

# 間指定
print("abc","def",sep=',')

# 最後指定
print('abc','def',end='/')


lines = "World"
# リスト文字列を文字列に変換
t = "".join(map(str, lines))
s = 'Hello' + ' ' + t + '!'
print (s)