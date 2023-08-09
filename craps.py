import random


def roll_dice():
    return random.randint(1, 6)


def main():
    while True:
        input("Press Enter to roll the dice...")

        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2

        print(f"Roll 1: {dice1}, Roll 2: {dice2}, Total: {total}")

        if total in [7, 11]:
            print("Congratulations! You win!")
            break
        elif total in [2, 3, 12]:
            print("Casino wins! Better luck next time.")
            break
        else:
            goal = total
            print(f"Goal is now set to {goal}. Roll again to win, or roll a 7 to lose.")
            while True:
                input("Press Enter to roll the dice...")
                dice1 = roll_dice()
                dice2 = roll_dice()
                total = dice1 + dice2
                print(f"Roll 1: {dice1}, Roll 2: {dice2}, Total: {total}")

                if total == goal:
                    print("Congratulations! You win!")
                    return
                elif total == 7:
                    print("Sorry, you rolled a 7 before reaching the goal. Casino wins.")
                    return


if __name__ == "__main__":
    main()

