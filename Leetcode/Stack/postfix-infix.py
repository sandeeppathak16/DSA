import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def postfix_to_infix(string):
    if len(string) <= 1:
        return string
    
    stack = []

    for s in string:
        if s.isalnum():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()

            stack.append(f'({b}{s}{a})')

    return stack[0]


test_cases = [
    # Basic expressions
    ("AB+", "(A+B)"),
    ("AB-", "(A-B)"),
    ("AB*", "(A*B)"),
    ("AB/", "(A/B)"),
    ("AB^", "(A^B)"),

    # Operator precedence style cases
    ("ABC*+", "(A+(B*C))"),
    ("AB*C+", "((A*B)+C)"),
    ("AB+C-", "((A+B)-C)"),
    ("AB*C/", "((A*B)/C)"),

    # Parentheses-style structures
    ("AB+C*", "((A+B)*C)"),
    ("ABC+*", "(A*(B+C))"),
    ("AB+CD-*", "((A+B)*(C-D))"),

    # Nested expressions
    ("ABCD-*+", "(A+(B*(C-D)))"),
    ("AB+C*D-", "(((A+B)*C)-D)"),
    ("ABC+D*+", "(A+((B+C)*D))"),

    # Multiple operators
    ("ABC*+DE/-", "((A+(B*C))-(D/E))"),
    ("AB*CD/+E-", "(((A*B)+(C/D))-E)"),

    # Exponentiation
    ("ABC^^", "(A^(B^C))"),
    ("AB+C^", "((A+B)^C)"),
    ("AB^C*", "((A^B)*C)"),
    ("ABC^*", "(A*(B^C))"),

    # Mixed complex expressions
    ("ABCD^E-*+", "(A+(B*((C^D)-E)))"),
    ("AB+CD+*", "((A+B)*(C+D))"),
    ("ABC/-AK/L-*", "((A-(B/C))*((A/K)-L))"),

    # Single operand
    ("A", "A"),
    ("x", "x"),
    ("7", "7"),

    # Lowercase and digits
    ("ab+", "(a+b)"),
    ("12+", "(1+2)"),
    ("abc*+", "(a+(b*c))"),

    # Long expressions
    ("ABC*+DE/-FG*+", "(((A+(B*C))-(D/E))+(F*G))"),
]

run_tests(postfix_to_infix, test_cases)