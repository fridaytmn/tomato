from tomato import Tomato

class Bush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]
        
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.mature()
            
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    
    def give_away_all(self):
        self.tomatoes = []
    