
# '"をただの文字列として認識させたいときは手前にバックスラッシュ
print("say \"I don\'t know\"")

# とちゅうで改行させたい
print('Hi \nHow are you?')

# 改行を認識させないときは先頭にr(raw)
print(r'C:\name\name')

# 複数行の文章をまとめて書く
print("""\
line1
line2
line3\
""")

print('Hi' * 3)


word = 'python'
# 先頭を表示
print(word[0])
# 尾を表示
print(word[-1])

#スライス
print(word[0:2])

#文字を書き換え
word = 'j'+word[1:]
print(word)