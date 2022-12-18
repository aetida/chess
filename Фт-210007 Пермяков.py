import logging

logging.basicConfig(filename = "chess_log.log", level=logging.INFO)

while True:
    try:
        hor = int(input('Введите координату клетки фигуры по горизонтали: '))
        assert hor < 9 and hor > 0 
        logging.info(f'пользователь ввел горизонтальную координату: {hor}')
        break
    except ValueError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {hor} ')
    except AssertionError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {hor} ')

while True:
    try:
        vert = int(input('Введите координату клетки фигуры по вертикали: '))
        assert vert < 9 and vert > 0 
        logging.info(f'пользователь ввел вертикальную координату: {vert}')
        break
    except ValueError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {vert}')
    except AssertionError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {vert}')

while True:
    try:
        enemy_hor = int(input('Введите координату клетки фигуры противника по горизонтали: '))
        assert enemy_hor < 9 and enemy_hor > 0 
        logging.info(f'пользователь ввел горизонтальную координату противника: {enemy_hor}')
        break
    except ValueError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {enemy_hor}')
    except AssertionError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {enemy_hor}')

while True:
    try:
        enemy_vert = int(input('Введите координату клетки фигуры противника по вертикали: '))
        assert enemy_vert < 9 and enemy_vert > 0 
        logging.info(f'пользователь ввел вертикальную координату противника: {enemy_vert}')
        break
    except ValueError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {enemy_vert}')
    except AssertionError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {enemy_vert}')

sup_fig = ['Ферзь','Ладья','Слон','Конь']

while True:
    try:
        figure = int(input('''Какую фигуру вы хотите использовать?
        1 - Ферзь
        2 - Ладья
        3 - Слон
        4 - Конь
        Ваш выбор: '''))
        assert figure < 5 and figure > 0
        logging.info(f'пользователь выбрал фигуру: {sup_fig[figure-1]}')
        break
    except ValueError:
        print('Введены некорректные данные. Попробуйте снова.')
        logging.info(f'некорректный ввод. пользователь ввел: {figure}')
    except AssertionError:
        print('некорректный ввод')
        logging.info(f'некорректный ввод. пользователь ввел: {figure}')

# Проверка на совпадение цвета полей
if (hor + vert) % 2 == (enemy_hor + enemy_vert) % 2:
    if (hor + vert) % 2 == 0:
        print('Оба поля белого цвета')
        logging.info('Оба поля белого цвета')
    else:
        print('Оба поля черного цвета')
        logging.info('Оба поля черного цвета')
else:
    print('Поля разных цветов')
    logging.info('Поля имеют разные цвета')

# Расстояние по горизонтали и вертикали
dx = abs(hor - enemy_hor)
dy = abs(vert - enemy_vert)

# Проверка угрожает ли фигура полю, а так же второй ход
if figure == 1:     # Ферзь
    if hor == enemy_hor or vert == enemy_vert or dx == dy:
        print(f'Ферзь угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Ферзь угрожает полю ({enemy_hor}; {enemy_vert})')
    else:
        print(f'Ферзь не угрожает полю ({enemy_hor}; {enemy_vert})')
        print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({enemy_hor}; {vert})')
        logging.info(f'Ферзь не угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({enemy_hor}; {vert})')
elif figure == 2:   # Ладья
    if hor == enemy_hor or vert == enemy_vert:
        print(f'Ладья угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Ладья угрожает полю ({enemy_hor}; {enemy_vert})')
    else:
        print(f'Ладья не угрожает полю ({enemy_hor}; {enemy_vert})')
        print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({enemy_hor}; {vert})')
        logging.info(f'Ладья не угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({enemy_hor}; {vert})')
elif figure == 3:   # Слон
    if dx == dy:
        print(f'Слон угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Слон угрожает полю ({enemy_hor}; {enemy_vert})')
    else:
        print(f'Слон не угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Слон не угрожает полю ({enemy_hor}; {enemy_vert})')
        if (hor + vert) % 2 != (enemy_hor + enemy_vert) % 2:
            print(f'Слон никаким образом не может угрожать полю ({enemy_hor}; {enemy_vert})')
            logging.info(f'Слон никаким образом не может угрожать полю ({enemy_hor}; {enemy_vert})')
        else:
            m0 = enemy_hor
            n0 = enemy_vert
            m1 = 0
            n1 = 0
            while 0 < m0 < 9 and 0 < n0 < 9:
                m0 += 1
                n0 += 1
                if abs(hor - m0) == abs(vert - n0):
                    m1 = m0
                    n1 = n0
            m0 = enemy_hor
            n0 = enemy_vert
            while 0 < m0 < 9 and 0 < n0 < 9:
                m0 -= 1
                n0 += 1
                if abs(hor - m0) == abs(vert - n0):
                    m1 = m0
                    n1 = n0
            m0 = enemy_hor
            n0 = enemy_vert
            while 0 < m0 < 9 and 0 < n0 < 9:
                m0 += 1
                n0 -= 1
                if abs(hor - m0) == abs(vert - n0):
                    m1 = m0
                    n1 = n0
            m0 = enemy_hor
            n0 = enemy_vert
            while 0 < m0 < 9 and 0 < n0 < 9:
                m0 -= 1
                n0 -= 1
                if abs(hor - m0) == abs(vert - n0):
                    m1 = m0
                    n1 = n0
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
            logging.info(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
else:   # Конь
    if abs(dx - dy) == 1:
        print(f'Конь угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Конь угрожает полю ({enemy_hor}; {enemy_vert})')
    else:
        print(f'Конь не угрожает полю ({enemy_hor}; {enemy_vert})')
        logging.info(f'Конь не угрожает полю ({enemy_hor}; {enemy_vert})')
