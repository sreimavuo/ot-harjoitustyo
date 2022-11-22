from entities.item import Item
from entities.pocket import Pocket
from entities.bag import Bag


def main():
    item1 = Item("Kompassi", "Suunto M3")
    item2 = Item("Virtapankki", "Anker PowerCore III 10K")

    pocket1 = Pocket("Vasen Sivutasku")
    pocket1.add_item(item1)
    pocket1.add_item(item2)

    bag1 = Bag("Reppu", "Eberlestock Switchblade")
    bag1.add_pocket(pocket1)

    print("Items:")
    print(item1)
    print(item2)
    print("Pockets with items:")
    print(pocket1)
    print("Bags with pockets with items:")
    print(bag1)


if __name__ == "__main__":
    main()
