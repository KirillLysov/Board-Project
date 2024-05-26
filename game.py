from inspect import getsource
from game_parts import Board


def main():
    game_1 = Board()
    game_1.make_move(0, 1, 'x')
    print('Ход сделан!')
    game_1.display()
    print(game_1)


if __name__ == __name__:
    main()

game_1 = Board()
print(getsource(Board))