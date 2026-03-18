import sys
#объявляем функцию, которая будет определять принадлежность точки к эллипсу
def dot_in_circle(x, y, x_d, y_d, m, n):
    left_side = (x - x_d)**2 * n**2 + (y - y_d)**2 * m**2           #формулу эллипса привели к одному знменаателю, чтобы избавиться от float
    right_side = m**2 * n**2                                        #и поделили на 2 части, которые и будем срравнивать
    if left_side < right_side:
        print(1)
    elif left_side == right_side:
        print(0)
    else:
        print(2)

if len(sys.argv) != 3:
        print("Ошибка: Неверное количество аргументов.")
        sys.exit(1)
      
circle_path = sys.argv[1]
dot_path = sys.argv[2]

with open(circle_path) as file:
    centre_coord = file.readline().split()
    rad_coord = file.readline().split()

with open(dot_path) as file:
    for line in file:
        dot_coord = line.split()
        dot_in_circle(int(centre_coord[0]), int(centre_coord[1]), int(dot_coord[0]), int(dot_coord[1]), int(rad_coord[0]), int(rad_coord[1]))