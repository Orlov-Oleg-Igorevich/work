import pprint


def make_book(way):
    with open(way, "r", encoding = "utf-8") as f:
        cook_book = {}
        text = f.read()
        recipes = text.split("\n\n")
        for recipe in recipes:
            recipe = recipe.split("\n")
            cook_book[recipe[0]] = []
            for ig in range(2, len(recipe)):
                ig = [i.strip() for i in recipe[ig].split("|")]
                cook_book[recipe[0]].append({'ingredient_name': ig[0], 'quantity': ig[1], 'measure': ig[2]})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    a = {}
    for dish in dishes:
        for ig in cook_book[dish]:
            volume = int(ig['quantity'])*person_count
            if ig['ingredient_name'] in a.keys():
                a[ig['ingredient_name']] = {'quantity': a[ig['ingredient_name']]['quantity'] + volume, 'measure':  ig['measure']}
            else:
                a[ig['ingredient_name']] = {'quantity':  volume, 'measure':  ig['measure']}
    return a


def main(list = ['Запеченный картофель', 'Омлет'], n = 2, way = "recipes.txt"):
    book = make_book(way)
    pprint.pprint(get_shop_list_by_dishes(list, n, book))

    
main()
        

























