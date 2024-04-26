class Birds():
    def __init__(self, wingspan, name, species):
        self.wingspan=wingspan
        self.name=name
        self.species=species

    def fly(self):
        return f"{self.name} can fly"


Jeff = Birds(50, 'Jeffrey', 'Eagle')

print(Jeff.name)
print(Jeff.fly)
