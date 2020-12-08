
from tube import tube

class Solver():
    """ 
    Solving with backtracking.
    """

    def __init__(self, Filled_tubes, Empty_tubes = [[0],[0]]):          # list, list
        self.Tubes = list()
        self.moves = list()
        self.last_move = []
        self.result = list()

        for i in Filled_tubes:
            self.Tubes.append(tube(i))

        for j in Empty_tubes:
            self.Tubes.append(tube(j))


    def is_allowed(self, a,b):
        if self.last_move == [b,a]:             # check reverse move 1->2  2->1
            return False
        elif self.Tubes[a].is_single_color():
            if self.Tubes[b].top() == 0:
                return False
            else: return True
        elif self.Tubes[b].is_single_color():
            if self.Tubes[a].top() == 0:
                return False
            else: return True
        else: return True
        


    def solve(self):
        if self.is_solved():
            return True
        else:
            current_matches = self.matches()
            # safe point to restart from
            save = self.Tubes, self.moves

            for i in current_matches:               # choose move
                if self.is_allowed(*i):            
                    self.moves.append(i)             # append to solution list      
                    self.pour(*i)                    # making move i
                    self.last_move = i               # save move
                    solved = self.solve()            # recursing for next move j
                    if solved == "Done":
                        return "Done"
                    elif solved == True:                
                        self.result = save
                        return "Done"
                    else:                           # no matches found after move i
                        self.Tubes, self.moves = save           # rewind to safepoint
                        continue                    # next move i+1                        # next move i+1
                else:
                    continue
            else:
                return False                        # when no further matching possible

    def matches(self):
        stat_ls = list()
        match_list = list()

        for i in enumerate(self.Tubes):
            # list( tube no , color no , space) (0,2,False)
            stat_ls.append([i[0], *i[1].status()])

        for i in stat_ls:
            for j in stat_ls:
                a, b = i[0], j[0]
                # diff tube and same color not 0 and space in j
                if a != b and i[1] == j[1] != 0 and j[2]:
                    # list of list [( tube no -> tube no ] [(0->5)]
                    match_list.append([a,b])
                elif j[1] == 0 and i[1] != 0 and j[2]:                             # only j 0
                    match_list.append([a,b])
        del stat_ls
        return match_list

    def pour(self, from_a, to_b):
        self.Tubes[to_b].addTop(self.Tubes[from_a].popTop())

    def is_solved(self):
        for i in self.Tubes:
            if i.is_done():
                continue
            else:
                return False
        else:
            return True

    def show_result(self):
        if self.result == []:
            return
        for t in self.result[0]:
            print(t.tubeList)
        print(self.result[1])




if __name__ == "__main__":
    sol = Solver([[3,1,2,1],[2,2,1,3],[3,1,2,3]])
    sol.solve()
    sol.show_result()



