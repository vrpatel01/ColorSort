class tube():
    """
    color order bottom -> top
    0 - wildcard
    """

    def __init__(self,colors):
        self.tubeList = colors
        self.tube_done = False

    def fill_count(self):
        return len(self.tubeList)

    def color_count(self,color):
        return self.tubeList.count(color)

    def top(self):
        return self.tubeList[-1]

    def space(self):
        return True if (len(self.tubeList) < 4) else False

    def status(self):
        return self.top(), self.space()

    def popTop(self):
        if len(self.tubeList) > 1:
            return self.tubeList.pop()
        else:                                           # if last color in tubepipli
            r = self.tubeList.pop()
            self.tubeList.append(0)                     # 0 for wildcard
            return r

    def addTop(self, new):
        if new != 0:
            if self.top() == 0:
                self.tubeList.pop()
                self.tubeList.append(new)
            else:
                self.tubeList.append(new)
        else:
            return

    def is_single_color(self):
        return True if self.fill_count() == self.color_count(self.top()) else False

    def is_done(self):
        if self.tube_done:
            return self.tube_done
        else:
            self.tube_done = True if self.tubeList.count(
                self.top()) == 4 or self.color_count(0) == 1 else False
            return self.tube_done

