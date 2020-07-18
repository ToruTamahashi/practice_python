import string
# テキストのテンプレを作って任意の位置に値を表示したい
# 挿入される位置に$変数を記述
# メール送信のテンプレに使える
s = """\

Hi $name.

$contents

Have a good day
"""

# テンプレートの読み込み
t = string.Templete(s)
contents = t.substitute(name='Mike', contents='How are you')
print(contents)