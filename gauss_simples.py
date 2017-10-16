#!/pyvenv/mypython/bin/python
"""
Program that applies the Gauss Elimination method for solving linear equations.
This program only accepts arrays that do not contain null coefficients of variables.

Programa que aplica o método de Eliminação de Gauss para solução de equações lineares.
Este programa só aceita matrizes que não contenham coeficientes de variáveis nulos.
"""
import numpy as np


def gauss_elimination(li, lines):
    """
    Gauss Elimination Method
    Método de Eliminação de Gauss
    :param li: list that represents the matrix
    :param lines: number of matrix lines
    :return: results matrix
    """
    mat = np.matrix(li)
    col = 0
    line = 0

    while col < lines:
        for l in range(line, lines):
            mat[l] = (1 / li[l][col]) * mat[l]

        t = -1 * mat[line]

        for l in range(line + 1, lines):
            mat[l] = np.add(mat[l], t)

        li = mat.tolist()

        line += 1
        col += 1

    return mat


def input_matrix(lines):
    li = []

    print("Enter one row of the matrix at a time, with the coefficients separated by spaces example:")
    print("line #: 2 4.2 7.5 8")
    print("*****************************************************************************************")
    for i in range(0, lines):
        print("line", i + 1, ": ", end="")
        line = input()
        line = line.split()
        line = [float(x) for x in line]
        li.append(line)

    return li


def main():
    lines = int(input("Enter the number of rows of the matrix: "))
    li = input_matrix(lines)

    print("\nMatrix Result:\n{}".format(gauss_elimination(li, lines)))


main()

