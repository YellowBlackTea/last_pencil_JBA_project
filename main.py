import random


def main():
    print("How many pencils would you like to use:")
    pen = input()

    while not (pen.isdigit()):
        print("The number of pencils should be numeric")
        pen = input()
        if pen == '0':
            print("The number of pencils should be positive")
            pen = input()
        if pen < '0':
            print("The number of pencils should be numeric")
            pen = input()

    while pen == '0':
        print("The number of pencils should be positive")
        pen = input()
        if pen < '0':
            print("The number of pencils should be numeric")
            pen = input()
        if not (pen.isdigit()):
            print("The number of pencils should be numeric")
            pen = input()
    while pen < '0':
        print("The number of pencils should be numeric")
        pen = input()
        if pen == '0':
            print("The number of pencils should be positive")
            pen = input()
        if not (pen.isdigit()):
            print("The number of pencils should be numeric")
            pen = input()

    print("Who will be the first (John, Jack):")
    name = input()

    while name not in "Jack" and name not in "John":
        print("Choose between 'John' and 'Jack'")
        name = input()

    pen_int = int(pen)

    while pen_int > 0:
        print(pen_int * "|")
        print(name + "'s turn:")

        if name == "John":
            name = "Jack"
            bot = 1
        else:
            name = "John"
            bot = 0

        if bot == 0:
            if pen_int == 1:
                remove = "1"
                print(1)
            elif pen_int % 4 == 0:
                remove = "3"
                print(3)
            elif pen_int % 4 == 3:
                remove = "2"
                print(2)
            elif pen_int % 4 == 2:
                remove = "1"
                print(1)
            else:
                random.seed()
                supp = random.randint(1, 3)
                print(supp)
                remove = str(supp)

        else:
            remove = input()

        while remove not in "1" and remove not in "2" and remove not in "3":
            print("Possible values: '1', '2' or '3'")
            remove = input()

        while int(remove) > pen_int:
            print("Too many pencils were taken")
            remove = input()

        remove_int = int(remove)
        pen_int -= remove_int

    print(name + " won!")


if __name__ == '__main__':
    main()

