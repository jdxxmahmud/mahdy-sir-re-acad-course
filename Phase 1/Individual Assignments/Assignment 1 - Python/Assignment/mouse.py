from series import get_val_from_series

class Mouse:

    x = 0
    y = 0

    def __init__(self) -> None:
        self.get_mouse_position()

    def get_mouse_position(self):
    
        mouse = [0, 0]
        if input("\nDo you want to manually create mouse's position? [y/n]: ").upper() == "Y":
            self.x = get_val_from_series(int(input(f"\nPlease enter a for the mouse: ")))
            self.y = get_val_from_series(int(input(f"\nPlease enter b for the mouse: ")))
            print(f"\nThe mouse is at the point, {[self.x, self.y]}")
        else:
            print(f"\nThe mouse is at the origin, {[self.x, self.y]}")

    def update_mouse_position(self):

        if input("\nDo you want to update mouse's position? [y/n]: ").upper() == "Y":
            self.x = get_val_from_series(int(input(f"\nPlease enter a for the mouse: ")))
            self.y = get_val_from_series(int(input(f"\nPlease enter b for the mouse: ")))
            print(f"\nThe mouse is changed position to the point {[self.x, self.y]}")
        else:
            print(f"\nThe mouse is still at the point, {[self.x, self.y]}")

        

