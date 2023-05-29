def print_results(*args, action=None, result=None):
    """
    Вывод в табличном виде результатов вычислений

    Функция принимает переменное число значений, которые нужно вывести в табличном виде. 
    последний аргумент в упакованном кортеже - результат вычислений, 
    предпоследний - действие, которое выполнилось,остальные — аргументы, с которыми это действие выполнилось.
    """

    operands = args[:len(args)]
    print('inp_args in pretty mode', operands, action, result)

    def argsPrint(operands):
        lst=[]
        for i in operands:
            lst.append(f"| {i} |")
        return lst 
    
    def actionPrint(operands, action):
        lst=[]
        for i in list(operands[0:-1]):
            lst.append(f"{i} {action}")
        lst.append(f"{operands[-1]}")
        return lst

    arg_list=(" ".join((argsPrint(operands))))
    action_list=(" ".join(actionPrint(operands, action)))
    st = f"{arg_list} {action_list} = {result} |"
    print('-' * len(st))    
    print(st)
    print('-' * len(st))

def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    from datetime import datetime
    try:
        f = open(file, mode='a', errors='ignore')
        f.write(f"{datetime.now()} : {action} : {args} = {result} \n")
        f.close()
    except:
        print("Невозможно открыть или создать файл")
        