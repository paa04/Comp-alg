from typing import TextIO

import poly
import spline
import mixed


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

    mtr = read_mtr_3d(5, file)

    file.close()

    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    value = 1

    method = int(input("1. Сплайн\n"
                       "2. Полином Ньютона\n"
                       "3. Смешанный метод\n"
                       "Введите метод: "))

    match method:
        case 1:
            print(f"U(x, y, z) = {spline.spline_3d_interpolation(mtr, x, y, z)}")
        case 2:
            nx = int(input("Введите количество узлов по x: "))
            ny = int(input("Введите количество узлов по y: "))
            nz = int(input("Введите количество узлов по z: "))

            print(f"U(x, y, z) = {poly.newton_3d_interpolation(mtr, x, y, z, nx, ny, nz)}")
        case 3:
            ny = int(input("Введите количество узлов по y: "))

            print(f"U(x, y, z) = {mixed.mixed_3d(mtr, x, y, z, ny)}")


if __name__ == "__main__":
    main()
