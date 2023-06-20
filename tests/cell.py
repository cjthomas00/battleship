import ipdb

class Cell:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.fired_upon = False

    def empty(self):
        return self.ship is None
    
    def place_ship(self, ship):
        self.ship = ship
    
    def fire_upon(self):
        if self.ship is not None:
            self.ship.hit()
        self.fired_upon = True
    
    def render(self, user_ships = False):
        if self.fired_upon:
            if self.ship is None:
              return "M"
            elif self.ship.sunk():
                return "X"
            else:
                return "H"
        elif user_ships and self.ship is not None:
            return "S"
        else:
            return "."