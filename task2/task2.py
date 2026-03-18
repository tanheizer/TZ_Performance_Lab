import sys
#объявляем функцию, которая будет определять принадлежность точки к эллипсу
def dot_in_circle(x, y, x_d, y_d, m, n):
    f = ((x - x_d)**2 / m**2) + ((y - y_d)**2 / n**2)    #формула эллипса была честно загуглена, ибо я ее не помню
    if f < 1:
        print(1)
    elif int(f) == 1:      # не уверен, что это правильная реализация повышения точности для сравнения float и int, 
        print(0)           # но просто округление будто бы еще хуже 
    else:
        print(2)         
circle_path = sys.argv[1]
dot_path = sys.argv[2]
with open('circle.txt') as file:
    centre_coord = file.readline().split()
    rad_coord = file.readline().split()
with open(dot_path) as file:
    for line in file:
        dot_coord = line.split()
        dot_in_circle(int(centre_coord[0]), int(centre_coord[1]), int(dot_coord[0]), int(dot_coord[1]), int(rad_coord[0]), int(rad_coord[1]))