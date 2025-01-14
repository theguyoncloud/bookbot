def sort_on(d):
    return d["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]

vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
