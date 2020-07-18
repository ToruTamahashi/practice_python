with open('text.txt', 'r') as f:
    # まとめと読み込んで表示
    # print(f.read())
    # 一行ずつ読み込んで表示
    """
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break
    """
    # 指定文字ごとに変数に保存して表示（1文字の奴は後ろに改行が入っている）
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break