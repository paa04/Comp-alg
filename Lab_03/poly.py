import math


def get_ans(x0, matrix):
    rez = 0
    for i in range(len(matrix)):
        ac = matrix[i][0].k
        # print(ac, end="")
        for j in range(i):
            ac *= (x0 - matrix[0][j].dydx[0])
            # print(f"(x - {matrix[0][j].dydx[0]})", end="")
        # print()
        rez += ac

    return rez


class Element:

    def __init__(self):
        self.dydx = []
        self.dn = 1
        self.k = None
        self.name = None
        self.lx = None
        self.rx = None

    def add(self, el):
        rez = Element()
        if self.name == el.name and self.name is not None and el.name is not None:
            rez.dn = self.dn + 1
            rez.dydx = self.dydx.copy()
            rez.k = rez.dydx[rez.dn] / math.factorial(rez.dn - 1)
            rez.lx = self.lx
            rez.rx = self.rx
            rez.name = self.name
        else:
            rez.k = (el.k - self.k) / (el.rx - self.lx)
            rez.lx = self.lx
            rez.rx = el.rx
            rez.dydx = self.dydx.copy()
        return rez

    def copy(self):
        cop = Element()
        cop.name = self.name
        cop.dydx = self.dydx.copy()
        cop.k = self.k
        cop.dn = self.dn
        cop.lx = self.lx
        cop.rx = self.rx
        return cop

    def __str__(self):
        return str(self.k)


def read_file(name, n, x):
    f = open(name)

    # f.readline()

    arr = []

    for i in range(n):
        line = f.readline()
        if not line.split():
            n = len(arr)
            break
        tmp = [float(i) for i in line.split()]
        arr.append(tmp)

    line = f.readline()

    while arr[n // 2][0] < x and line.split() != []:
        tmp = [float(i) for i in line.split()]
        arr = arr[1:]
        arr.append(tmp)
        line = f.readline()

    return arr


def search_conf(arr, n, x):
    if len(arr) <= n:
        return arr

    conf = arr[:n]

    i = n

    while conf[n // 2] < x and i < len(arr):
        conf.append(arr[i])
        i += 1
        conf = conf[1:]

    return conf


def get_mtr(arr):
    mtr = [[]]

    num = 0

    for i in arr:
        cnt = len(i) - 1
        tmp = Element()

        tmp.name = num
        tmp.dydx = i.copy()
        tmp.k = i[1]
        tmp.lx = i[0]
        tmp.rx = i[0]
        tmp.dn = 1

        num += 1

        for j in range(cnt):
            mtr[0].append(tmp.copy())

    true_size = len(mtr[0])

    for j in range(1, true_size):
        mtr.append([])
        for i in range(true_size - j):
            mtr[j].append(mtr[j - 1][i].add(mtr[j - 1][i + 1]))

    return mtr


def calc(x, n, name):
    arr = read_file(name, n, x)
    mtr = get_mtr(arr)

    # for j in range(len(mtr)):
    #     for i in range(len(mtr[j])):
    #         print(mtr[j][i], end=" ")
    #     print()

    return get_ans(x, mtr)


def calc_dir_2(x, n, name):
    arr = read_file(name, n, x)
    mtr = get_mtr(arr)

    res = 2 * mtr[2][0].k + mtr[3][0].k * (6 * x - 2 * mtr[0][0].dydx[0] -
                                           2 * mtr[1][0].dydx[0] - 2 * mtr[2][0].dydx[0])

    return res


def newton_2d_interpolation(mtr, x, y, nx, ny):
    n = len(mtr)
    arr = []

    #TODO 





if __name__ == "__main__":
    n = int(input("Введите количество узлов: "))
    x = float(input("Введите искомое значенеи x: "))
    fname = input("Введите название файла: ")
    print(calc(x, n, fname))
