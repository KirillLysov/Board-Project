from inspect import getsource
from game_parts import Board, FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'
    running_flag = True
    game.display()

    while running_flag:
        print(f'Ход делает игрок - {current_player}')
        while True:
            try:
                row = int(input('Введите номер номер ряда: '))
                col = int(input('Введите номер столбца: '))
                if (row > 2 or row < 0) or (col > 2 or col < 0):
                    raise FieldIndexError
                if isinstance(row, int) == False or isinstance(col, int) == False:
                    raise ValueError
                if game.board[row][col] != ' ':
                    raise CellOccupiedError
            except CellOccupiedError:
                print('Ячейка занята - выберите другую')
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except FieldIndexError:
                print(f'Ошибка: {FieldIndexError}')
                print(f'Значение должно быть меньше '
                      f'{game.field_size} и больше 0 ')
                print('Введите новое значение')
                continue
            except Exception:
                print(f'Произошла непредвиденная ошибка - {Exception}')
                continue
            else:
                break

        game.make_move(row, col, current_player)
        print('Ход сделан!')
        print()
        game.display()
        if game.check_win(current_player):
            print(f'Победил игрок - {current_player}')
            running_flag = False
        elif game.is_board_full():
            print('Ничья!')
            running_flag = False
        current_player = 'O' if current_player == 'X' else 'X'
        print()


if __name__ == __name__:
    main()
