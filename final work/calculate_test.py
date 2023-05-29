import calculate


def test_sum_two_int():
    assert calculate.calculate(1, 2, "+") == 3, "Неверная сумма"


def test_minus_neg_n():
    assert calculate.calculate(1, -1, "-") == 2, "Вычитание отрицательных чисел (по сути - сложение)"


def test_div_by_zero():
    assert calculate.calculate(10, 0, "/") == "деление на ноль невозможно", "Деление на ноль"


def test_sum_two_float():
    assert calculate.calculate(1.0, 1.0, "+") == 2.0, "Неверная сумма чисел с плавающей точкой"


def test_op2_invalid_type():
    assert calculate.calculate(1, "0",
                               "+") == "ошибка во втором операнде", "тип операнда int или float"


def test_op1_invalid_type():
    assert calculate.calculate("1", 0,
                               "+") == "ошибка в первом операнде", "тип операнда int или float"
