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
        """ SUB - Issue Number #2 """
        total = self._number1 - self._number2
        return f"{self._number1} - {self._number2} = {total}"

    def mul(self):
        """ MULT - Issue Number #3 """
        total = self._number1 * self._number2
        return f"{self._number1} x {self._number2} = {total}"

    def div(self):
        """ DIV - Issue Number #4 """
        try:
            total = self._number1 / self._number2
            return f"{self._number1} / {self._number2} = {total}"
        except ZeroDivisionError:
            return "No numbers or division by zero."
