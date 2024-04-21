import poly
import spline
import matplotlib.pyplot as plt


def to_table(filename):
    x_l, y_l = [], []
    with open(filename, "r") as f:
        # f.readline()
        for i in f:
            x, y = [float(j) for j in i.split()]
            x_l.append(x)
            y_l.append(y)

    return x_l, y_l


def plot(x_or, y_or, x, y):
    plt.scatter(x_or, y_or)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x)')

    plt.show()


if __name__ == "__main__":
    filename = "data.txt"
    x, y = to_table(filename)

    div0, divn = 0, 0

    x_search = float(input("Введите искомое значение x: "))

    mode = int(input("Введите режим\n"
                     "0. Стандартный\n"
                     "1. x0 = 0, xn = p\"\n"
                     "2. x0 = p\", xn = 0\n"
                     "3. x0 = p\", xn = p\"\n"))

    match mode:
        case 0:
            pass
        case 1:
            divn = poly.calc_dir_2(x[-1], 4, filename)
        case 2:
            div0 = poly.calc_dir_2(x[0], 4, filename)
        case 3:
            div0, divn = poly.calc_dir_2(x[0], 4, filename), poly.calc_dir_2(x[-1], 4, filename)

    y_found = spline.interpolate(x, y, x_search, div0, divn)

    nx, ny = [], []

    i = 0
    step = 0.01
    while i < 7:
        nx.append(i)
        ny.append(spline.interpolate(x, y, i, div0, divn))
        # ny.append(poly.calc(i, 4, "data.txt"))
        i += step

    plot(x, y, nx, ny)

    print(f"Найденный y = {y_found}")
