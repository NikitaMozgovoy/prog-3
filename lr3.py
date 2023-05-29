def check_types(op, allowed_types):
    return type(op) in allowed_types

def calculate(op1, op2, act, allowed_types=(int, float, list, tuple)):
    if not check_types(op1, allowed_types) and op1 is not None:
        r=("ошибка в первом операнде")
    elif not check_types(op2, allowed_types) and op2 is not None:
        r=("ошибка во втором операнде")
    else:
        if type(op1) != float and type(op2) != float:
            if type(op1) in (int,str):
                op1=float(op1)
            if type(op2) in (int,str):
                op2=float(op2)
            if (type(op1) is list and type(op2) is list)or (type(op1) is tuple and type(op2) is tuple):
                if act == "+":
                    r = op1+op2
                else:
                    print("Действие невозможно")
            if type(op1) in (list, tuple) and op2==None:
                if act=="+":
                    r=0
                    for i in op1:
                        r+=i
                    return r
                else:
                    print("Действие невозможно")
                    pass
        if act == "+":
            r = op1 + op2
        elif act == "-":
            r = op1 - op2
        elif act == "*":
            r = op1 * op2
        elif act == "/":
            if op2!=0:
                r = op1 / op2
            else:
                r="деление на ноль невозможно"
        else:
            r = "Операция не распознана"
    return r


def main():
    operand1 = float(input("Enter 1 value: ")) 
    operand2 = float(input("Enter 2 value: "))
    action = input("Enter type of operation: ")
    result=(calculate(operand1, operand2, action))
    print("Result is: " + str(result))

if __name__ == "__main__":
    main()
    print("running by interpreter")