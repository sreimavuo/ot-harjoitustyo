class Bag:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.pockets = []

    def add_pocket(self, pocket):
        self.pockets.append(pocket)

    def list_pockets(self):
        return self.pockets

    def __str__(self):
        printout = f"{self.name}, {self.description}"
        for i in self.list_pockets():
            printout = printout + "\n  " + str(i)
        return printout
