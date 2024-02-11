from cat import Cat
from mouse import Mouse
from distance import find_cat_mouse_distance
from series import get_val_from_series
from util import printLine

def get_cats():
    catNames = ["CatA", "CatB", "CatC"]

    cats = []

    for cat in catNames:
        x = get_val_from_series(int(input(f"\nPlease enter a for {cat}: ")))
        y = get_val_from_series(int(input(f"\nPlease enter b for {cat}: ")))

        cats.append(Cat(cat, x, y))

    printLine()

    for cat in cats:
        cat.show_cat()


    return cats

def update_cats(cats):
    for cat in cats:
        cat.update_cat()

    return cats


if __name__ == "__main__":
    
    cats = get_cats()

    printLine()

    mouse = Mouse()

    printLine()

    if input("\nDo you want to change any cat or mouse's position? [y/n]: ").lower() == 'y':

        cats = update_cats(cats)
        mouse.update_mouse_position()

    printLine()
    
    min_dist = find_cat_mouse_distance(cats, mouse)

    print(f'\nWinner: {min_dist}\n\n')
