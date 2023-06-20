from ship import Ship
from cell import Cell

# Ship Tests
def test_ship_properties():
    cruiser = Ship("Cruiser", 3)
    assert cruiser.name == "Cruiser"
    assert cruiser.length == 3  
    assert cruiser.health == 3 
    assert not cruiser.sunk() 

def test_ship_hit_and_sunk():
    cruiser = Ship("Cruiser", 3)
    cruiser.hit()
    assert cruiser.health == 2
    cruiser.hit()
    assert cruiser.health == 1
    assert not cruiser.sunk()
    cruiser.hit()
    assert cruiser.sunk()

# Cell Tests

def test_cell_properties():
    cell = Cell("B4")
    assert cell.coordinate == "B4"
    assert cell.ship is None
    assert cell.empty()

def test_cell_place_ship():
    cell = Cell("B4")
    cruiser = Ship("Cruiser", 3)
    cell.place_ship(cruiser)
    assert cell.ship == cruiser
    assert not cell.empty()

def test_cell_fired_upon():
    cell = Cell("B4")
    cruiser = Ship("Cruiser", 3)
    cell.place_ship(cruiser)
    assert not cell.fired_upon
    cell.fire_upon()
    assert cell.ship.health == 2
    assert cell.fired_upon

def test_cell_render():
    cell_1 = Cell("B4")
    assert cell_1.render() == "."
    cell_1.fire_upon()  # Corrected method name
    assert cell_1.render() == "M"

    cell_2 = Cell("C3")
    cruiser = Ship("Cruiser", 3)
    cell_2.place_ship(cruiser)
    assert cell_2.render() == "."
    assert cell_2.render(True) == "S"
    cell_2.fire_upon()
    assert cell_2.render() == "H"
    assert not cruiser.sunk()
    cruiser.hit()
    cruiser.hit()
    assert cruiser.sunk()
    assert cell_2.render() == "X"
