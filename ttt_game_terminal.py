from random import randint, random

mas = [['_'] * 4 for i in range(4)]
mas[0][0] = ' '
abc_list = ['a', 'b', 'c']
x_o = ['X', 'O']

for col in range(1, 4):
    mas[col][0] = col

for row in range(1, 4):
    mas[0][row] = abc_list[row - 1]

for i in mas:
    print(' ' * 10, *i)

def next_move(col: int, row: int, xo: str) -> None:
    mas[col][row] = xo

def next_move_computer():
    col = randint(1, 3)
    row = randint(1, 3)
    if mas[col][row] == '_':
        mas[col][row] = 'V'
    else:
        next_move_computer()


first_move = x_o[randint(0, 1)]
rand_move = randint(1, 2)
while True:
    
    if rand_move % 2 == 0:
        move = input(f'Ваш ход! Вы играете {first_move} Введите координаты клетки(Пример: b1): ')
        coor_1 = int(move[1])
        coor_2 = abc_list.index(move[0]) + 1

        if coor_1 not in range(1, 4) or move[0] not in abc_list:
            print(f'Неправильные координаты поля - {move}')

        elif mas[coor_1][coor_2] != '_':
            move = input(f'Это поле занято! Введите другие координаты: ')
        else:
            next_move(coor_1, coor_2, first_move)
            

        for i in mas:
            print(' ' * 10, *i)
    else:
        next_move_computer()
        print('Ход противника: ')
        for i in mas:
            print(' ' * 10, *i)
        
    rand_move += 1
    