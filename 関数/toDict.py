# **kwargs で辞書を受け取ることができる
def menu(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)