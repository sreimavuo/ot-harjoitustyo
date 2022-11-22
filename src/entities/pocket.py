class Pocket:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items

    def __str__(self):
        printout = f"{self.name}"
        for i in self.list_items():
            printout = printout + "\n  " + str(i)
        return printout
