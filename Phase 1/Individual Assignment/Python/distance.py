from time import sleep

class Distance:
    def manhattan_distance(self, point1, point2):
        return round(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]), 2)
    
    def pythagorean_distance(self, point1, point2):
        return round(pow(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2), .5), 2)
    
    def find_cat_mouse_distance(self, cats, mouse):
        sleep(2)
        x =  input("\nAvailable distance finding methods\n\t[1] Manhattan Distance.\n\t[2] Pythagorean Distance\n\tChoose your option: ")

        
        while x != '1' and x != '2':
            x = input("\nInvalid Input! Enter [q] to quit or enter valid input: ").lower()
            if x == "q":
                print("\nQuitting the program\n\n")
                return -1
        
        distances = {}
        dist_methods = ["manhattan_distance", "pythagorean_distance"]


        for name, pos in cats.items():
            distances[name] = eval(f'self.{dist_methods[int(x)]}({pos}, {mouse})')

        print(f'Distance of the cats with the mouse are: {distances}')

        min_dist_cats = self.find_cat_min_distance_with_mouse(distances)

        print(f"\nThe cat(s) closest to the mouse: {min_dist_cats}")

        res = {cat: distances[cat] for cat in min_dist_cats}
        print(f'\nResult: {res}')

        return res
    
    def find_cat_min_distance_with_mouse(self, distances):
        temp = min(distances.values())
        res = [key for key in distances if distances[key] == temp]

        return res


            
    

if __name__ == "__main__":
    dist = Distance()

    man = dist.manhattan_distance([1, 2], [3, 4])
    pyth = dist.pythagorean_distance([1, 2], [3, 4])

    print(f"Manhattan Distance: {man}")
    print(f"Pythagorean Distance: {pyth}")


    cats = {'CatA': (11.0, 11.0), 'CatB': (5.0, 3.0), 'CatC': (11.0, 11.0)}
    mouse = [0, 0]
    dist.find_cat_mouse_distance(cats, mouse)