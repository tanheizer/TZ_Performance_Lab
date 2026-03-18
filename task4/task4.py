import sys

num_path = sys.argv[1]
data = []
with open(num_path) as f:
    for line in f:
        data.append(int(line))

mediana = sorted(data)[len(data)//2]    # информация про медиану взята с просторов интернета, изначально решал прямым перебором,
steps = 0                               # приведением каждого элемента к каждому. очень затратно с точки зрения времени и ресурсов,
for el in data:                         # это решение куда как изящнее
    steps += abs(el-mediana)
if steps <= 20:
    print(steps)
else:
    print('20 ходов недостаточно для приведения всех элементов массива к одному числу.')