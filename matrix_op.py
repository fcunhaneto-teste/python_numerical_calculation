import numpy as np


def mult_mats(li1, li2):
    """
    multiply matrix x matriz
    :param li1: list
    :param li2: list
    :return: list
    """
    a = np.matrix(li1)
    b = np.matrix(li2)

    i, j = np.shape(a)
    k, l = np.shape(b)

    if j == k:
        result = np.matmul(a,b)
        return result.tolist()
    else:
        return None


def mult_const_mat(k, li):
    """
    multiply const x matrix
    :param k: number
    :param li: list
    :return: list
    """
    a = k * np.matrix(li)
    return a.tolist()


def sum_mats(li1, li2):
    """
    add matrix + matrix
    :param li1: list
    :param li2: list
    :return: list
    """
    a = np.matrix(li1)
    b = np.matrix(li2)

    if np.shape(a) == np.shape(b):
        result = np.add(a, b)
        return result.tolist()
    else:
        return None


def sub_mats(li1, li2):
    """
    sub matrix - matrix
    :param li1: list
    :param li2: list
    :return: list
    """
    a = np.matrix(li1)
    b = np.matrix(li2)

    b = mult_const_mat(-1, li2)

    if np.shape(a) == np.shape(b):
        result = np.add(a, b)
        return result.tolist()
    else:
        return None

def determinant(li):
    """
    matrix determinant
    :param li:
    :return: number
    """
    a = np.matrix(li)

    i, j = np.shape(a)

    if i == j:
        return np.linalg.det(a)
    else:
        return None

def trans_mat(li):
    """
    matrix transpose
    :param li: list
    :return: matrix transpose
    """
    a = np.matrix(li)
    return a.transpose()


li = [[1, 0, 3], [4, 2, 1], [0, 1, 2]]
# l2 = [[0, 3, -5], [2, 0, 0], [-1, -5, 3]]
# print(sub_mats(l1, l2))
print(trans_mat(li))