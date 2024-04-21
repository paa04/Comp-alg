from typing import TextIO

import poly
import spline


def read_mtr(matrix: [list], n, file: TextIO):
    for i in range(n):
        line = [int(j) for j in file.readline().split()]

        matrix[i].extend(line)


def read_mtr_3d(n, file):
    mtr = [[[] for __ in range(n)] for _ in range(n)]
    for i in range(n):
        read_mtr(mtr[i], n, file)

    return mtr


def main():
    file = open("data.txt")

    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    mtr = read_mtr_3d(5, file)

    print(f"U(x, y, z) = {spline.spline_3d_interpolation(mtr, x, y, z)}")

    file.close()


if __name__ == "__main__":
    main()
