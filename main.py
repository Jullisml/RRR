from SpecialHashMap import SpecialHashMap


map = SpecialHashMap()

map["value1"] = 1
map["value2"] = 2
map["value3"] = 3
map["1"] = 10
map["2"] = 20
map["3"] = 30
map["1, 5"] = 100
map["5, 5"] = 200
map["10, 5"] = 300

print(map.iloc[0])
print(map.iloc[1])
print(map.iloc[2])
print(map.iloc[3])