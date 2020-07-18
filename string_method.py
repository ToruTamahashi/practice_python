s = 'My name is Mike. Hi Mike'

# 先頭の文字列が指定の文字かどうか
is_start = s.startswith(('My'))
print(is_start)

# 指定の文字列のインデックスを検索
print(s.find('Mike'))

# 後ろからインデックスを検索
print(s.rfind('Mike'))

# 変数中に指定の文字が何個あるか
print(s.count('Mike'))

# 先頭を大文字にして残りを小文字にする
print(s.capitalize())

# 各文字の先頭を大文字にする
print(s.title())

# 全てを大文字にする
print(s.upper())

# 文字を入れ替え
print(s.replace('Mike','Nancy'))