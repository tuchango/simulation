import random

from entities.herbivore import Herbivore
from entities.creature import Creature
from simulation_map import SimulationMap
from ulils import sign
from actions import find_nearest_entity


class Predator(Creature):
    color = "red"
    visibility_dist = 15

    def do_move(self,
                current_coord: tuple[int, int],
                cells: SimulationMap):
        target_coord = find_nearest_entity(Herbivore, self.visibility_dist, current_coord, cells)
        if target_coord:
            move_to_coord = (current_coord[0] + sign(target_coord[0] - current_coord[0]),
                             current_coord[1] + sign(target_coord[1] - current_coord[1]))
        else:
            move_to_coord = (current_coord[0] + random.randint(-1, 1),
                             current_coord[1] + random.randint(-1, 1))
        cells.move_entity(current_coord, move_to_coord)
