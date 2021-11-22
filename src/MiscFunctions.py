"""
Misc Functions

Miscellaneous useful functions

Author: Alex Lim

Date of Initial Creation: October 21, 2021

"""

from random import randint
from warnings import catch_warnings, simplefilter

import numpy as np

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
                               show_warnings: bool = False):
        """
        Converts a complex number matrix to a real number matrix.\n
        * Note: The ComplexWarning is filtered and will not show up by default.

        :param complex_matrix: A complex number matrix
        :type complex_matrix: np.ndarray
        :param show_warnings: Whether to show or ignore warnings,
            defaults to False
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
        """
        Randomly chooses a random ndarray from args

        :param args: The ndarrays to randomly choose from
        :type args: np.ndarray
        :return: A random ndarray from args
        :rtype: np.ndarray
        """
        return args[randint(0, len(args)-1)]


class FactoringFunctions:
    """Useful factoring functions"""
    @staticmethod
    def gcd(x: int, y: int):
        """
        Euclid's algorithm for computing the greatest common divisor\n
        Further reading about Euclid's algorithm:\n
        .. _Khan Academy: https://www.khanacademy.org/computing/
            computer-science/cryptography/modarithmetic/a/
            the-euclidean-algorithm
        .. _Wikipedia: https://en.wikipedia.org/wiki/Euclidean_algorithm
        .. _Wolfram MathWorld:
            https://mathworld.wolfram.com/EuclideanAlgorithm.html
        * `Khan Academy`_
        * `Wikipedia`_
        * `Wolfram MathWorld`_

        :param x: A number with that has at least 1 factor in common with y
        :type x: int
        :param y: A number with that has at least 1 factor in common with x
        :type y: int
        :return: The greatest common divisor of x and y
        :rtype: int
        """
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x

    @staticmethod
    def gcd_recursive(x: int, y: int):
        """
        Euclid's algorithm for computing the greatest common divisor\n
        Further reading about Euclid's algorithm:\n
        .. _Khan Academy: https://www.khanacademy.org/computing/
            computer-science/cryptography/modarithmetic/a/
            the-euclidean-algorithm
        .. _Wikipedia: https://en.wikipedia.org/wiki/Euclidean_algorithm
        .. _Wolfram MathWorld:
            https://mathworld.wolfram.com/EuclideanAlgorithm.html
        * `Khan Academy`_
        * `Wikipedia`_
        * `Wolfram MathWorld`_

        :param x: A number with that has at least 1 factor in common with y
        :type x: int
        :param y: A number with that has at least 1 factor in common with x
        :type y: int
        :return: The greatest common divisor of x and y
        :rtype: int
        """
        if y == x:
            return x
        if y > x:
            return FactoringFunctions.gcd_recursive(y, x)
        if x % y == 0:
            return y
        return FactoringFunctions.gcd_recursive(y, x % y)

    @staticmethod
    def isqrt(num):
        """
        Newton's method for finding the integer square root of a number\n
        Further reading about Newton's method:\n
        .. _Wolfram MathWorld: https://mathworld.wolfram.com/NewtonsMethod.html
        * `Wolfram MathWorld`_

        :param num: The number to take the square root of
        :type num: int
        :return: The integer approximation of the square root of num
        :rtype: int
        """
        num_upper_bound = num
        num_lower_bound = (num_upper_bound + 1) // 2
        while num_lower_bound < num_upper_bound:
            num_upper_bound = num_lower_bound
            num_lower_bound += num // num_upper_bound
            num_lower_bound //= 2
        return num_upper_bound

    @staticmethod
    def period(num: int, a: int, max_allowed_period: int = 2**8):
        """
        Calculates the period of (a**x) % num

        :param num: A natural number
        :type num: int
        :param a: A guess factor
        :type a: int
        :return: The period
        :rtype: int
        :param max_allowed_period: The maximum allowed period before assuming
        the period to be None, defaults to 2**8=256
        :return: The period of (a**x) % num, or 0 if period > maxAllowedPeriod
        :rtype: int
        """
        period_list = list()
        x = 1
        while x <= max_allowed_period:
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

    @staticmethod
    def slow_version_sieve_Chinese_remainder_theorem(
            remainders: list[int], moduli: list[int]):
        """
        Applies Chinese remainder theorem using a search by sieving. Note that
        this method is slow (has exponential time complexity) and should not be
        used for practical purposes; however, it is useful for explaining
        Chinese remainder theorem.\n
        Further reading about Chinese remainder theorem:\n
        .. _Wolfram MathWorld:
            https://mathworld.wolfram.com/ChineseRemainderTheorem.html
        * `Wolfram MathWorld`_

        :param remainders: The remainders of (num // moduli)
        :type remainders: list[int]
        :param moduli: Coprime integers where (num % moduli = remainders)
        :type moduli: list[int]
        :raises ZeroDivisionError: integer division or modulo by zero
        :return: num, the smallest positive integer where
         (num % moduli = remainders)
        :rtype: int
        """
        product_mod = 1
        for r, m in zip(remainders, moduli):
            product_mod *= m
            if r >= m:
                r %= m
        moduli, remainders = zip(
            *sorted(zip(moduli, remainders), reverse=True))
        product_mod_current = moduli[0]
        num = remainders[0]
        for r, m in zip(remainders[1:], moduli[1:]):
            for j in range(product_mod):
                if (num + (j * product_mod_current)) % m == r:
                    num += j * product_mod_current
                    break
            product_mod_current *= m
        return num

    @staticmethod
    def Chinese_remainder_theorem(remainders: list[int], moduli: list[int]):
        """
        Applies Chinese remainder theorem
        Further reading about Chinese remainder theorem:\n
        .. _Wolfram MathWorld:
            https://mathworld.wolfram.com/ChineseRemainderTheorem.html
        * `Wolfram MathWorld`_

        :param remainders: The remainders of (num // moduli)
        :type remainders: list[int]
        :param moduli: Coprime integers where (num % moduli = remainders)
        :type moduli: list[int]
        :raises ZeroDivisionError: integer division or modulo by zero
        :return: num, the smallest positive integer where
         (num % moduli = remainders)
        :rtype: int
        """
        from functools import reduce
        total_sum = 0
        moduli, remainders = zip(*sorted(zip(moduli, remainders),
                                         reverse=True))
        product_mod = reduce(lambda a, b: a*b, moduli)
        for r, m in zip(remainders, moduli):
            p = product_mod // m
            Bezout_coefficient = FactoringFunctions.\
                extended_Euclidean_algorithm(p, m)[0]
            total_sum += r * Bezout_coefficient * p
        return total_sum % product_mod

    @staticmethod
    def extended_Euclidean_algorithm(x: int, y: int):
        """
        Extension to Euclid's algorithm for computing the coefficient of
        Bezout's identity corresponding to [x, y]\n
        Further reading about extended Euclidean algorithm:\n
        .. _Khan Academy: https://www.khanacademy.org/computing/
            computer-science/cryptography/modarithmetic/a/
            the-euclidean-algorithm
        .. _Wikipedia:
            https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
        * `Khan Academy`_
        * `Wikipedia`_

        :param x: A number with that has at least 1 factor in common with y
        :type x: int
        :param y: A number with that has at least 1 factor in common with x
        :type y: int
        :return: The coefficients of Bezout's identity corresponding to [x, y]
        :rtype: list[int]
        """
        r_0, r_1 = x, y  # remainders
        B_0, B_1 = 1, 0  # Bezout coefficients
        while r_1:
            r_temp = r_0 // r_1
            r_0, r_1 = r_1, r_0 - (r_temp * r_1)
            B_0, B_1 = B_1, B_0 - (r_temp * B_1)
        if y == 0:
            return [B_0, 0]
        else:
            return [B_0, (r_0 - (B_0 * x)) // y]
