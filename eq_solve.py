from sympy import Symbol
from sympy.solvers import solve

from text_detecting import detect_text


class EquationError(Exception):
    pass


class ExpressionError(Exception):
    pass


#  detect and solve equation
def das_eq(
        img
) -> str:
    eq = ''.join(detect_text(img))
    eq = eq.lower()
    x = Symbol('x')
    try:
        eq = eq.split('=')  # getting an expression
        first_part = eq[0]
        sec_part = eq[1].strip()
        if sec_part[0] == '-':  # if expression is negative, we put it with plus on the left side
            sec_part = sec_part.strip('-')
            eq = first_part + '+' + sec_part
        else:
            eq = first_part + '-' + sec_part
    except:
        raise ExpressionError

    try:
        result = solve(eq, x)
        return result
    except:
        raise EquationError
