import spline
import poly


def mixed_2d(mtr, x, y, ny):
    n = len(mtr)
    arr = []

    for i in range(n):
        arr.append(spline.interpolate([j for j in range(n)], mtr[i], x))

    return poly.calc_with_reg_arr(arr, y, ny)


def mixed_3d(mtr, x, y, z, ny):
    n = len(mtr)
    arr = []

    for k in range(n):
        arr.append(mixed_2d(mtr[k], x, y, ny))

    return spline.interpolate([i for i in range(n)], arr, z)
