def A_f(h):
    return [0 if i < 2 else h[i - 1] for i in range(len(h))]


def B_f(h):
    return [0 if i < 2 else -2 * (h[i - 1] + h[i]) for i in range(len(h))]


def D_f(h):
    return [0 if i < 2 else h[i] for i in range(len(h))]


def F_f(h, y):
    return [0 if i < 2 else -3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1])
            for i in range(len(h))]


def calc_y(a, b, c, d, xi, x_val):
    x = x_val - xi
    return a + b * x + c * (x ** 2) + d * (x ** 3)


def intr(x, x_s):
    for i in range(1, len(x)):
        if x[i - 1] <= x_s <= x[i]:
            return i

    return None


def interpolate(x, y, x_value, start=0, end=0):
    n = len(x)

    i_near = intr(x, x_value)

    h = [0 if not i else x[i] - x[i - 1] for i in range(n)]  # step value

    A = A_f(h)
    B = B_f(h)
    D = D_f(h)
    F = F_f(h, y)

    ksi = [0 for _ in range(n + 1)]
    theta = [0 for _ in range(n + 1)]

    ksi[1] = theta[1] = start / 2

    for i in range(2, n):
        ksi[i + 1] = D[i] / (B[i] - A[i] * ksi[i])
        theta[i + 1] = (A[i] * theta[i] + F[i]) / (B[i] - A[i] * ksi[i])

    c = [0 for _ in range(n + 1)]

    c[-1] = end / 2

    for i in range(n - 1, -1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + theta[i + 1]

    a = [0 if i < 1 else y[i - 1] for i in range(n)]
    b = [0 if i < 1 else (y[i] - y[i - 1]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3 for i in range(n)]
    d = [0 if i < 1 else (c[i + 1] - c[i]) / (3 * h[i]) for i in range(n)]

    return calc_y(a[i_near], b[i_near], c[i_near], d[i_near], x[i_near - 1], x_value)


def spline_2d_interpolation(mtr, x, y):
    n = len(mtr)
    arr = []

    for i in range(n):
        arr.append(interpolate([j for j in range(n)], mtr[i], x))

    return interpolate([i for i in range(n)], arr, y)


def spline_3d_interpolation(mtr, x, y, z):
    n = len(mtr)
    arr = []

    for k in range(n):
        arr.append(spline_2d_interpolation(mtr[k], x, y))

    return interpolate([i for i in range(n)], arr, z)
