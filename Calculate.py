class Calculator:

    def adder(self, x, y):
        result = int(x + y)
        return result

    def subtractor(self, x, y):
        result = int(x - y)
        return result

    def product(self, x, y):
        result = float(x * y)
        return result

    def divide(self, x, y):
        result = float(x / y)
        return result

    def modulus(self, x, y):
        result = x % y
        return result


def main():
    get = Calculator()
    ch = None
    while True:

        ch = int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Remainder\n9.Exit\nEnter Choice: "))
        if ch == 9:
            break

        if 0 < ch < 6:
            print("Enter 2 numbers:")
            x = int(input("1st value: "))
            y = int(input("2nd value: "))

            if ch == 1:
                result = get.adder(x, y)

            elif ch == 2:
                result = get.subtractor(x, y)

            elif ch == 3:
                result = get.product(x, y)

            elif ch == 4:
                result = get.divide(x, y)

            else:
                result = get.modulus(x, y)

            print(f"Result is : {result}")

        else:
            print("Wrong Choice!")

    print("Thank You!!!")


if __name__ == "__main__":
    main()
