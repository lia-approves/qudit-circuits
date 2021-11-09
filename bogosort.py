"""
bogosort

Uses a highly efficient permutation based classical algorithm to
sort via a permutation based classical algorithm

Author: Alex Lim
Date of Initial Creation: October 21, 2021

"""

from random import shuffle

__author__      = "Alex Lim"
__credits__     = "Alex Lim"
__maintainer__  = "Alex Lim"

import numpy as np


class bogosort:
    """
    Uses a highly efficient permutation based classical algorithm to
    sort via a permutation based classical algorithm
    """
    @staticmethod
    def is_sorted(data):
        """
        Determine whether the data is sorted.

        :param data: A list of data
        :type data: list
        :type data: np.ndarray
        :return: Whether the data is sorted
        :rtype: list
        """
        newData = data
        if type(data) == np.ndarray:
            newData1 = newData.sum(axis=0)
            newData = []
            for elements in newData1:
                newData.append(elements)
        return all(a <= b for a, b in zip(newData, newData[1:]))

    @staticmethod
    def permutatioOrdino(data):
        """
        Applies a classical algorithm to organize data

        :param data: A list of data
        :type data: list
        :type data: np.ndarray
        :return: A sorted list
        :rtype: list
        """
        newData = data
        if type(data) == np.ndarray:
            newData1 = newData.sum(axis=0)
            newData = []
            for elements in newData1:
                newData.append(elements)
        while not bogosort.is_sorted(newData):
            shuffle(newData)
        return newData
