import random


class Dice:

    def roll():
        dice2 = random.randint(1, 6)
        dice1 = random.randint(1, 6)
        print(f"{dice1}, {dice2}")

    print("Rolling...")


def main():
    Dice.roll()


if __name__ == "__main__":
    main()
