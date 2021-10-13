"""
Calculator: addition, subtraction, multiplication and division.
"""


class Calc():
    """
    Class to perform calculations
    """

    def __init__(self, number1, number2):
        """
        Import the first and second number
        """
        self._number1 = number1
        self._number2 = number2

    def sum(self):
        """ SUM - Issue Number #1 """
        total = self._number1 + self._number2
        return f"{self._number1} + {self._number2} = {total}"

    def sub(self):
        """ SUB """
        total = self._number1 - self._number2
        return f"{self._number1} - {self._number2} = {total}"

    def mul(self):
        """ MULT """
        total = self._number1 * self._number2
        return f"{self._number1} x {self._number2} = {total}"

    def div(self):
        """ DIV """
        try:
            total = self._number1 / self._number2
            return f"{self._number1} / {self._number2} = {total}"
        except ZeroDivisionError:
            return "No numbers or division by zero."
