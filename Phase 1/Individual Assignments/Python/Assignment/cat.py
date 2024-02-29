from series import get_val_from_series

class Cat:
    

    def __init__(self, name, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        self.name = name

    def update_x_y(self, x, y):
        self.x = x
        self.y = y

    def find_cat_x_y(self, name):
        self.x = get_val_from_series(int(input(f"\nPlease enter a for {name}: ")))
        self.y = get_val_from_series(int(input(f"\nPlease enter b for {name}: ")))
    
    def show_cat(self):
        print(f"\nPosition of {self.name} is {[self.x, self.y]}")

    def update_cat(self):

        if input(f"\nDo you want to update {self.name}'s position? [y/n]: ").upper() == "Y":
            self.x = get_val_from_series(int(input(f"\nPlease enter a for {self.name}: ")))
            self.y = get_val_from_series(int(input(f"\nPlease enter b for the {self.name}: ")))
            print(f"\n{self.name} has changed position to the point {[self.x, self.y]}")
        else:
            print(f"\n{self.name} is still at the point, {[self.x, self.y]}")
