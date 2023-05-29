def print_results(*args, action=None, result=None):
    """
    Вывод в табличном виде результатов вычислений

    Функция принимает переменное число значений, которые нужно вывести в табличном виде. 
    последний аргумент в упакованном кортеже - результат вычислений, 
    предпоследний - действие, которое выполнилось,остальные — аргументы, с которыми это действие выполнилось.
    """

    operands = args[:len(args)]

    print('inp_args in pretty mode', operands, action, result)

    from string import ascii_lowercase
    def argsPrint(operands):
        lst=[]
        for i in operands:
            lst.append(f"| {i} |")
        return lst 
    def actionPrint(operands, action):
        lst=[]
        for i in range(operands[0],operands[-1]):
            lst.append(f"{i} {action}")
        lst.append(f"{operands[-1]}")
        return lst


    arg_list=(" ".join((argsPrint(operands))))
    action_list=(" ".join(actionPrint(operands, action)))
    st = f"{arg_list} {action_list} = {result} |"
    print('-' * len(st))    
    print(st)
    print('-' * len(st))

# Пример вывода большого количества аргументов
# inp = 100, 200, 300, action = +
#
# ************************************
# *   A, B, C      *    A + B + C    *
# ************************************
# *  100, 200, 300 *    13579        *
# ************************************
