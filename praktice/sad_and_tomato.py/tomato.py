class Tomato:
    stages = {0: 'nothing',
              1: 'flower',
              2: 'green_tomato',
              3: 'red_tomato'}
    
    def __init__(self, index):
        self._index = index
        self._stage = 0
    
    def mature(self):
        self._change_state()
    
    def is_ripe(self):
        return self._stage == 3
    
    def _change_state(self):
        if self._stage < 3:
            self._stage += 1
        self._print_state()
    
    def _print_state(self):
        print(f'Tomato {self._index} is  {Tomato.stages[self._stage]}')
