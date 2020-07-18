# w オプションで記述したファイル名でファイルを作成する
f = open('text.txt','w')
# f.writeもしくは、printのfile=fで文字を記述する
f.write('Test\n')
print('My','name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()
