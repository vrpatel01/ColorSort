from Liquid_sort_solver import Solver
from copy import deepcopy

class player(Solver):
    def __init__(self,game,moves_to_do = []):
        self.game = deepcopy(game)
        super().__init__(deepcopy(game))
        self.m_list = moves_to_do
        self.play()

    def play(self,moves_to_do = None):
        if moves_to_do == None:
            moves_to_do = self.m_list
        for move in moves_to_do:
            self.pour(*move)
        else:
            self.staus()

    def staus(self):
        print("\nGame : ",self.game)
        print("Is solved : ",self.is_solved())

if __name__ == "__main__":
    filled =  []  #list of filled tubes 
    move = []     #moves to do
    p = player(filled,move)




