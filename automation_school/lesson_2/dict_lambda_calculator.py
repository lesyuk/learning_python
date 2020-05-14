from typing import Callable, Union

"""
Ключевое слово lambda используется для создания функций и возврата их значения во
время выполнения программы. lambda принимает параметр, за которым следует одно
выражение, которое становится телом функции, а значение этого выражения возвращается новой функцией.
"""
OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
STOP_WORD = 'stop'


def get_operand() -> float:
    val = input('Введите число: ')
    try:
        return float(val)
    except ValueError:
        print('Вы подали на ввод не число.\n')


def get_operator() -> str:
    op = input(f'Введите знак операции {tuple(OPS.keys())}: ')
    if op in OPS:
        return op
    print('Вы ввели неверный знак операции.\n')


def get_input(getting_func: Callable) -> Union[float, str]:
    while True:
        _input = getting_func()
        if _input is not None:
            return _input


while True:
    operand_01 = get_input(get_operand)
    operand_02 = get_input(get_operand)
    operator = get_input(get_operator)
    result = OPS.get(operator)(operand_01, operand_02)

    print(f'\n{operand_01} {operator} {operand_02} = {result}\n')
    if input(f'Введите {STOP_WORD}, чтобы завершить работу, все остальное, чтобы продолжить: ') == STOP_WORD:
        break
    else:
        continue