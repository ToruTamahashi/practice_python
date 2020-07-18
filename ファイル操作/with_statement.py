s = """\
AAA
BBB
CCC
DDD
"""

# withステートメントで記述するとf.closeなしに記述できる
# あとファイル操作をしている範囲が見やすくなる
with open('text.txt','w') as f:
    f.write(s)