from time import sleep
from util import printLine


def manhattan_distance(point1, point2):
    return round(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]), 2)


def pythagorean_distance(point1, point2):
    return round(pow(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2), .5), 2)


def find_cat_mouse_distance(cats, mouse):

    x =  input("\nAvailable distance finding methods\n\t[1] Manhattan Distance.\n\t[2] Pythagorean Distance\n\tChoose your option: ")
    
    while x != '1' and x != '2':
        x = input("\nInvalid Input! Enter [q] to quit or enter valid input: ").lower()
        if x == "q":
            print("\nQuitting the program\n\n")
            return -1
    

    distances = {}
    dist_methods = ["manhattan_distance", "pythagorean_distance"]


    print(f"\n\nDistance method chosen {dist_methods[int(x) - 1]}")

    printLine()
    print("\n\nCalculating...\n\n")
    sleep(1.5)


    for cat in cats:
        distances[cat.name] = eval(f'{dist_methods[int(x) - 1]}({[cat.x, cat.y]}, {[mouse.x, mouse.y]})')


    sleep(.9)
    print(f'Distance of the cats with the mouse are: {distances}')


    min_dist_cats = find_cat_min_distance_with_mouse(distances)


    sleep(.9)
    print(f"\nThe cat(s) closest to the mouse: {min_dist_cats}")
    sleep(.9)

    res = {cat: distances[cat] for cat in min_dist_cats}

    return res


def find_cat_min_distance_with_mouse(distances):

    min_dist = min(distances.values())
    res = [key for key in distances if distances[key] == min_dist]

    return res
            

if __name__ == "__main__":


    man = manhattan_distance([1, 2], [3, 4])
    pyth = pythagorean_distance([1, 2], [3, 4])

    print(f"Manhattan Distance: {man}")
    print(f"Pythagorean Distance: {pyth}")


    cats = {'CatA': (11.0, 11.0), 'CatB': (5.0, 3.0), 'CatC': (11.0, 11.0)}
    mouse = [0, 0]
    find_cat_mouse_distance(cats, mouse)