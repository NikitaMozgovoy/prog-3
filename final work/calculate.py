from calcprint import print_results, write_log
import unittest

PARAMS = {
    'precision': None,
    'output_type': None,
    'possible_types': None
}


def load_params(file="params.ini"):
    ''' Функция загружает параметры вычислений из внешнего файла, 
    которым по умолчанию является params.ini '''

    global PARAMS
    try:
        f = open(file, 'r', errors='ignore')
        f.close()
    except FileNotFoundError:
        print("Такого файла с параметрами не существует")
    else:
        with open(file, 'r', errors='ignore') as f:
            lines = f.readlines()
            for l in lines:
                param = l.split('=')
                param[1] = param[1].strip('\n')
                param[1] = eval(param[1])
                PARAMS[param[0]] = param[1]


def convert_precision(prec):
    ''''
    Преобразует точность данную в виде числа с плавающей точкой в целое число, возможное для использования с функцией round.
    >>> convert_precision(0.00001)
    5
    >>> convert_precision(0.0000000001)
    10
    >>> convert_precision('s')
    None
    '''
    try:
        prec = str(prec)
        for i in prec:
            if i == 'e':
                x = prec.split('-')
                return int(x[1])
            if i == ".":
                x = prec.split('.')
                return int(len(x[1]))
    except ValueError:
        print("Неверно указана точность, проверьте данные")


def user_input():
    args = []
    
    while True:
        val = input("Enter value: ")
        try:
            if val == "":
                break
            val = float(val)
        except ValueError:
            print(
                "Введите число в правильном формате (разделитель дробной части '.') "
            )
        else:
            args.append(val)

    print(args)
    if len(args) <= 1:
        return

    print("Введите один из знаков действия: +, -, *, /, ^ ")
    action = input("action: ")

    try:
        res = calculate(*args, action=action, **PARAMS)
    except Exception:
        print("Ошибка вычисления. Результат не определен")
    else:
        print_results(*args, action=action, result=res)


def calculate(*args, action=None, **kwargs):
    ''' Главная функция приложения калькулятора, в которой и производятся все вычисления, 
    а также запись в историю вычислений. Результат приводится к заданному типу данных и округляется до заданного количества знаков

    >>> calculate(*list(range(1, 10)), action = "+", **PARAMS)
    45.0
    >>> calculate(*list(range(1, 10)), action = "-", **PARAMS)
    -45
    >>> calculate(*list(range(1, 5)), action = "/", **PARAMS)
    0.04167
    >>> calculate(*[1.0001, 2.2345], action = "*", **PARAMS)
    2.23472
    '''

    load_params()
    global result
    precision = convert_precision(kwargs['precision'])
    output_type = kwargs['output_type']

    if action == '+':
        result = sum(args)

    if action == '-':
        result = args[0]
        for n in args[1:(len(list(args)))]:
            result -= n

    if action == '*':
        result = 1
        for n in args:
            result *= n

    if action == '/':
        result = args[0]
        try:
            for n in args[1:(len(list(args)))]:
                result /= n
        except ZeroDivisionError:
            return "Ошибка деления на ноль"
    
    if action == '^':
        result = args[0]
        for n in args[1:len(args)]:
            result = result ** n

    if type(result) is not output_type:
        result = output_type(result)
    
    result = round(result, precision)
    write_log(*args, action=action, result=result)
    return result


if __name__ == "__main__":
    load_params()
    user_input()
