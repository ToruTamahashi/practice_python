with open('text.txt', 'r') as f:
    # test.txtのなかで今何文字目を見ているかを表示
    print(f.tell())
    # 現在の位置の文字を読み込んで次の位置に移動
    print(f.read(1))
    # 5文字目に移動
    f.seek(5)
    print(f.read(1))
    # 戻ることもできる
    f.seek(1)
    print(f.read(1))
    f.seek(10)
    print(f.read(1))