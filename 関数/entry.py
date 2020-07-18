def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ',dessert)

menu('beef','ice', 'beer')

# どの値をどの引数に入れるか明示するには以下のようにする
menu(entree='beef', dessert='ice', drink='beer')
