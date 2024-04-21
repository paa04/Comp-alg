import main
import spline
import poly

x = float(input("Введите значение x: "))

filename = "data.txt"

x_l, y = main.to_table(filename)

div0, divn = poly.calc_dir_2(x_l[0], 4, filename), poly.calc_dir_2(x_l[-1], 4, filename)


print("Сплайн при x0 = 0, xn = 0", spline.interpolate(x_l, y, x, 0, 0))
print("Сплайн при x0 = p, xn = 0", spline.interpolate(x_l, y, x, div0, 0))
print("Сплайн при x0 = 0, xn = p", spline.interpolate(x_l, y, x, 0, divn))
print("Сплайн при x0 = p, xn = p", spline.interpolate(x_l, y, x, div0, divn))
print("Полином Ньютона при n = 4", poly.calc(x, 4, filename))
