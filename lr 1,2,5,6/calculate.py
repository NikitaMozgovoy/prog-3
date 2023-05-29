from calcprint import print_results
PARAMS = {'precision': 0.00001, 'output_type': float, 'possible_types': (int, float)}


def convert_precision(prec):
    ''''
    Преобразует точность данную в виде числа с плавающей точкой в целое число, возможное для использования с функцией round.
    '''    
    prec=str(prec)
    for i in prec:
        if i=='e':
            x=prec.split('-')
            return int(x[1])
        if i==".":
            x=prec.split('.')
            return int(len(x[1]))

def calculate(*args, **kwargs):
    precision = convert_precision(kwargs['precision'])  
    output_type = kwargs['output_type']
    print(precision)

    if args[-1] == '+':
        result_sum = sum(args[0:-1])
        if type(result_sum) is not output_type:
            result_sum = output_type(result_sum)
        return result_sum

    if args[-1] == '-':
        result_diff=0
        for n in args[0:-1]:
            result_diff -= n
        if type(result_diff) is not output_type:
            result_sum = output_type(result_diff)
        return result_diff

    if args[-1] == '*':
        result_mult = 1
        for n in args[0:-1]:
            result_mult *= n
        if type(result_mult) is not output_type:
            result_mult = output_type(result_mult)
        return round(result_mult, precision)

    if args[-1] == '/':
        result_division = args[0]
        for n in args[1:-1]:
            result_division /= n
        if type(result_division) is not output_type:
            result_division = output_type(result_division)
        return round(result_division, precision)


def test_packed_calc_sum():
    inp1, action = [1, 2, 3, 4, 5, 6, 7, 8, 9], "+"
    assert calculate(*inp1, action,
                     **PARAMS) == 45.0, 'Sum of list of ints from 1 to 9'
    assert type(calculate(*inp1, action, **
                     PARAMS)) is type(45.0), 'Type of sum is incorrect'


if __name__ == "__main__":
    assert calculate(*list(range(1, 10)), "+", **PARAMS) == 45.0 # 1 + 2 + 3 + .. + 9
    assert calculate(*list(range(1, 10)), "-", **PARAMS) == -45
    assert calculate(*list(range(1, 5)), "/", **PARAMS) == 0.04167 
    assert calculate(*[1.0001, 2.2345], "*", **PARAMS)== 2.23472
    print_results(*list(range(1, 10)), action = "+", result=calculate(*list(range(1, 10)), "+", **PARAMS))