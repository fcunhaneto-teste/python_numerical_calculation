#!/pyvenv/mypython/bin/python
"""
Program for solving linear equations.

Programa para solução de equações lineares.
"""
from os import system
from sys import platform, exit
import numpy as np

if 'linux' in platform:
    def clear(): system('clear')
if 'win' in platform:
    def clear(): system('cls')

def cal_det(a):
    """
    matrix determinant
    :param a: numpy array
    :return: number
    """

    i, j = np.shape(a)

    if i != j:
        print('Invalid matrix')
        exit(1)

    return np.linalg.det(a)


def solve_lineq(lines):
    """
    Solve linear equation
    :param lines: string list that represent matrix
    """
    l1 = []
    l2 = []

    for line in lines:
        line = line.split()
        line = [float(x) for x in line]
        l2.append(line.pop())
        l1.append(line)

    a = np.array(l1)
    b = np.array(l2)

    if cal_det(a) == 0:
        print('System without solution or without unique solution')
        exit(1)

    print(np.linalg.solve(a, b))


def file_input(arq):
    with open(arq) as f_obj:
        lines = f_obj.readlines()

    solve_lineq(lines)


def keyboard_input(nl):
    """
    Input the lines of matrix by keyboard
    :param nl: number of matrix lines
    """

    lines = []

    clear()
    print('You enter with the whole matrix a + b')
    print(
        "Enter one row of the matrix at a time, with the coefficients separated by spaces example:")
    print("line #: 2 4.2 7.5 8")
    print(
        '*****************************************************************************************')
    for i in range(0, nl):
        print("line", i + 1, ": ", end="")
        line = input()
        lines.append(line)

    solve_lineq(lines)


clear()

print('This program solves linear equations through the matrices of coefficients a '
      'and the matrix of independent terms b: ax = b.')
print('You enter with the whole matrix a + b')
print('The matrix can be input by keyboard or by text file\n')

while True:
    mode = int(input('Enter 1 for keyboard or 2 for text file 0 for exit: '))

    if mode == 1:
        lines = int(input("Enter the number of system rows: "))
        keyboard_input(lines)
    elif mode == 2:
        arq = input('Enter the name of file: ')
        file_input(arq)
        break
    elif mode == 0:
        print('Good by')
        break
    else:
        print("Invalid option try again")