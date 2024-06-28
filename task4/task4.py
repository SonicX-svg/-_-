# python3 -c 'import task4; print(task4.min_steps("data.txt"))'     - для 'Элементы массива читаются из файла, переданного в качестве аргумента командной строки!'

def min_steps(txt_file):
    with open(txt_file) as file:
        data = file.read()

    data_int = [int(i) for i in data.split()]

    mean_ = round(int(sum(data_int) / len(data_int)))
    result = [abs(i-mean_) for i in data_int]

    return f'Наименьшее количество шагов = {sum(result)}'
