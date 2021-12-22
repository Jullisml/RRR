class SpecialHashMap:
    iloc = list()

    # ploc = Ploc()

    def __init__(self):
        self.map = dict()

    def __setitem__(self, key, value):
        self.map[key] = value
        self.toSortedSet()

    def toSortedSet(self):
        # из отсортированного списка ключей добавляем в список iloc значения по этим ключам, из чего получается
        # список значений (где номер ключа - индекс)
        self.iloc = list()
        for i in sorted(self.map.keys()):
            self.iloc.append(self.map[i])
