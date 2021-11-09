"""
Misc Functions

Miscellaneous useful functions

Author: Alex Lim
Date of Initial Creation: October 21, 2021

"""

import numpy as np
from random import randint
from warnings import catch_warnings, simplefilter

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"


class MiscFunctions:
    """Miscellaneous useful functions"""
    @staticmethod
    def print_qubits(*argv: np.ndarray):
        """
        Prints the dimensions and matrices of qubits

        :param argv: The qubits to print in order (starting at 0)
        :type argv: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for args in argv:
            print("qubit " + str(i) + " dimensions: " + str(args.shape))
            print("qubit " + str(i) + ":")
            print(args)
            print()
            i += 1

    @staticmethod
    def print_truncated_qubits(numDecimals: int, *argv: np.ndarray):
        """
        Prints the dimensions and truncated matrices of qubits

        :param numDecimals: The number of decimals to truncate to
        :param argv: The qubits to print in order (starting at 0)
        :type argv: np.ndarray
        """
        np.set_printoptions(linewidth=np.inf)
        i = 0
        for args in argv:
            print("qubit " + str(i) + " dimensions: " + str(args.shape))
            print("qubit " + str(i) + ":")
            print(np.round(args, numDecimals))
            print()
            i += 1

    @staticmethod
    def varName(variable):
        """
        Gets the name of the variable

        :param variable: Any variable
        :return: The name of the variable
        :rtype: str
        """
        for variableName, variableContents in globals().items():
            if id(variable) == id(variableContents):
                return variableName

    @staticmethod
    def real_to_complex_matrix(real_matrix: np.ndarray):
        """
        Converts a real number matrix to a complex number matrix

        :param real_matrix: A real number matrix
        :type real_matrix: np.ndarray
        :return: A complex number matrix
        :rtype: np.ndarray
        """
        if real_matrix.dtype == np.complex_:
            return real_matrix
        else:
            return np.array(real_matrix, dtype=np.complex_)

    @staticmethod
    def complex_to_real_matrix(complex_matrix: np.ndarray,
                               show_warnings: bool=False):
        """
        Converts a complex number matrix to a real number matrix.\n
        * Note: The ComplexWarning is filtered and will not show up by default.

        :param complex_matrix: A complex number matrix
        :type complex_matrix: np.ndarray
        :param show_warnings: Whether to show or ignore warnings,
            defaults to false
        :type show_warnings: bool
        :raises ComplexWarning: Casting complex values to real discards the
            imaginary part
        :return: A real number matrix
        :rtype: np.ndarray
        """
        if complex_matrix.dtype != np.complex_:
            return complex_matrix
        else:
            if show_warnings:
                return np.array(complex_matrix, dtype=np.float_)
            with catch_warnings():
                simplefilter("ignore")
                return np.array(complex_matrix, dtype=np.float_)

    @staticmethod
    def random_ndarray(*args: np.ndarray):
        return args[randint(0, len(args)-1)]


class FactoringFunctions:
    """Useful factoring functions"""
    @staticmethod
    def gcd(x: int, y: int):
        """
        Euclid's algorithm for computing the greatest common divisor

        :param x: A number with that has at least 1 factor in common with y
        :type x: int
        :param y: A number with that has at least 1 factor in common with x
        :type y: int
        :return: The greatest common divisor of x and y
        :rtype: int
        """
        # if y == x:
        #     return x
        # if y > x:
        #     return FactoringFunctions.gcd(y, x)
        # if x % y == 0:
        #     return y
        # return FactoringFunctions.gcd(y, x % y)
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x

    @staticmethod
    def period(num: int, a: int, maxAllowedPeriod: int=2**8):
        """
        Calculates the period of (a**x) % num

        :param num: A number to be used in (a**x) % num
        :type num: int
        :param a: A number to be used in (a**x) % num
        :param maxAllowedPeriod: The maximum allowed period before assuming
        the period to be None, defaults to 2**8=256
        :return: The period of (a**x) % num, or 0 if period > maxAllowedPeriod
        :rtype: int
        """
        period_list = list()
        x = 1
        while x <= maxAllowedPeriod:
            if (a**x) % num in period_list:
                return len(period_list)
            period_list.append((a**x) % num)
            x += 1
        return 0

    @staticmethod
    def isPrime(num: int):
        """
        Uses trial division to check if num is prime

        :param num: A natural number
        :type num: int
        :return: If num is prime
        :rtype: bool
        """
        i = 2
        while i < np.sqrt(num):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def isPrimeQuick(num: int):
        """
        Uses trial division to check if num is prime

        :param num: A natural number
        :type num: int
        :return: If num is prime
        :rtype: bool
        """
        if num & 1 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i = i + 2
        return True

    @staticmethod
    def most_common_element(List: list):
        """
        Finds the most common element in a list

        :param List: A list of elements
        :type List: list
        :return: The most common element
        """
        counter = 0
        num = List[0]
        for elements in List:
            freq = List.count(elements)
            if freq > counter:
                counter = freq
                num = elements
        return num
