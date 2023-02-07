# vvod

# from PY.home008.keys import key_gen
from keys import key_gen
from random import randint


def get_surname():
    return input('Фамилия: ')

def get_name():
    return input('Имя: ')

def get_class():
    # return input('Класс: ')
    return str(randint(1,11))

def get_status():
    # return int(input('Средний балл: '))
    return randint(2,5)

def name():
    # return [get_surname(), get_name()]
    return (get_surname(), get_name())

def new_student():
    return (name(),
    get_class(),
    get_status())


def write_file(data):
    n, c, s, k = data
    string = '{}. Ученик {} класса {}. Средний балл {}'.format(k, c, n, s)
    with open('catalog.txt', 'a') as file:
        file.write(f'{string}\n')
    return ((k,n,c,s))

def view_data(stud, title, status):
    print(f'Ученик {title}А класса ', end = '')
    print(*stud)
    print(f'Средний балл: {status}')
    return (stud, title, status)


# view_data(name(), get_class(), get_status(), key_gen())



def log(data):
    k, n, c, s = data
    with open('logs.csv','a') as file:
        file.write('{};{};{}"a";{}\n'.format(k, n, c, s))
    # return ((k,n,c,s))

# новый ученик
log(write_file((name(), get_class(), get_status(), key_gen())))
