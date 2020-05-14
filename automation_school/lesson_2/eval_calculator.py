from typing import Callable, Union

# Никогда так не делайте

OPERATORS = ('+', '-', '*', '/')
STOP_WORD = 'stop'


def get_operand() -> float:
    val = input('Введите число: ')
    try:
        return float(val)
    except ValueError:
        print('Вы подали на ввод не число.\n')


def get_operator() -> str:
    op = input(f'Введите знак операции {OPERATORS}: ')
    if op in OPERATORS:
        return op
    print('Вы ввели неверный знак операции.\n')


def get_input(getting_func: Callable) -> Union[float, str]:
    while True:
        _input = getting_func()
        if _input is not None:
            return _input


def __evaluate_expression(operand_first, operand_second, operation) -> Union[float, str]:
    try:
        return eval(f'{operand_first}{operation}{operand_second}', {})
    except ZeroDivisionError:
        return 'undefined (на ноль делить нельзя)'


while True:
    operand_01 = get_input(get_operand)
    operand_02 = get_input(get_operand)
    operator = get_input(get_operator)
    print(f'\n{operand_01} {operator} {operand_02} = {__evaluate_expression(operand_01, operand_02, operator)}\n')
    if input(f'Введите {STOP_WORD}, чтобы завершить работу, все остальное, чтобы продолжить: \n') == STOP_WORD:
        break
    else:
        continue