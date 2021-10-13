"""
Calculator: addition, subtraction, multiplication and division.
"""

from basic_calcs import calc, extras


def main():
    """ Start the calculation """
    while True:
        try:
            extras.clear()
            print("=" * 20)
            option = int(input("""Choose the option:
            1 - Sum
            2 - Sub
            3 - Mul
            4 - Div
            5 - Exit
            Your choice:"""))
            print("=" * 20)
            if option in [1, 2, 3, 4]:
                num1 = extras.readfloat("First Number: ")
                num2 = extras.readfloat("Second Number: ")
                start_calc = calc.Calc(num1, num2)
                if option == 1:
                    print(start_calc.sum())
                    input()
                elif option == 2:
                    print(start_calc.sub())
                    input()
                elif option == 3:
                    print(start_calc.mul())
                    input()
                elif option == 4:
                    print(start_calc.div())
                    input()
            elif option == 5:
                break
            else:
                print("Wrong Option ...")
                input()
        except ValueError:
            print("Type a number from 1 to 5 ...")
            input()
        except KeyboardInterrupt:
            print("Calculator Stopped")
            input()
            break


if __name__ == "__main__":
    main()
