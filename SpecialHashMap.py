class SpecialHashMap:
    iloc = list()


    def __init__(self):
        self.map = dict()

    def __setitem__(self, key, value):
        self.map[key] = value
        self.toSortedSet()

    def toSortedSet(self):
        self.iloc = list()
        for i in sorted(self.map.keys()):
            self.iloc.append(self.map[i])
