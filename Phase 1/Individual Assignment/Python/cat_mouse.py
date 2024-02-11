from series import get_val_from_series


def get_cats():

    cats = ["CatA", "CatB", "CatC"]

    cat_pos = {}
    
    for cat in cats:
        x = get_val_from_series(int(input(f"\nPlease enter a for {cat}: ")))
        y = get_val_from_series(int(input(f"\nPlease enter b for {cat}: ")))

        cat_pos[cat] = [x, y]

    return cat_pos


def get_mouse():

    mouse = [0, 0]
    if input("\nDo you want to manually create mouse's position? [y/n]: ").upper() == "Y":
        x = get_val_from_series(int(input(f"\nPlease enter a for the mouse: ")))
        y = get_val_from_series(int(input(f"\nPlease enter b for the mouse: ")))
        print(f"\nThe mouse is at the point, {[x, y]}")

    else:
        print(f"\nThe mouse is at the origin, {mouse}")

    return mouse


if __name__ == "__main__":
    print(get_cats())
    print(get_mouse())