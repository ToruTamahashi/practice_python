import os

# それがファイルなのかチェック
print(os.path.isfile('text.txt'))
# それがディレクトリなのかチェック
print(os.path.isdir('design'))

# ファイル名を変更
#os.rename('text.txt', 'renamed.txt')

# シンボリックリンク作成（ショートカット作成）
# なのでsymlink.txtが変更されるとrenamed.txtの内容も変わる
# 管理者権限じゃないとエラーはく
#os.symlink('renamed.txt', 'symlink.txt')

# 新規フォルダ作成
os.mkdir('test_dir')

# フォルダ削除
# os.rmdir('test_dir')