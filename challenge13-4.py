class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self, name):
        self.name = name


r = Rider("John")
h = Horse("Sherry", r)
print(h.name + "'s rider is " + h.rider.name + ".")
