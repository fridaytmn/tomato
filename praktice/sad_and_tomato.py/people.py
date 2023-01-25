from bush import Bush
from tomato import Tomato

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        
    def work(self):
        print('Gardener is working..')
        self._plant.grow_all()
        print('Gardener finished')
        
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early!')
        