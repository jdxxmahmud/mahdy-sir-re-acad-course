from cat_mouse import *
from distance import Distance


if __name__ == "__main__":
    cats = get_cats()
    mouse = get_mouse()

    dist = Distance()
    min_dist = dist.find_cat_mouse_distance(cats, mouse)