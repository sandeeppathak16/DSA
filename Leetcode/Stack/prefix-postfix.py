import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def prefix_to_postfix(string):
    if len(string) <= 1:
        return string
    
    stack = []

    for s in string[::-1]:
        if s.isalnum():
            stack.append(s)

        else:
            a = stack.pop()
            b = stack.pop()
            exp = f'{a}{b}{s}'
            stack.append(exp)

    return stack[0]


test_cases = [
    # Basic expressions
    ("+AB", "AB+"),
    ("-AB", "AB-"),
    ("*AB", "AB*"),
    ("/AB", "AB/"),
    ("^AB", "AB^"),

    # Operator precedence style cases
    ("+A*BC", "ABC*+"),
    ("+*ABC", "AB*C+"),
    ("-+ABC", "AB+C-"),
    ("/*ABC", "AB*C/"),

    # Parentheses-style structures
    ("*+ABC", "AB+C*"),
    ("*A+BC", "ABC+*"),
    ("*+AB-CD", "AB+CD-*"),

    # Nested expressions
    ("+A*B-CD", "ABCD-*+"),
    ("-*+ABCD", "AB+C*D-"),
    ("+A*+BCD", "ABC+D*+"),

    # Multiple operators
    ("-+A*BC/DE", "ABC*+DE/-"),
    ("-+*AB/CDE", "AB*CD/+E-"),

    # Exponentiation
    ("^A^BC", "ABC^^"),
    ("^+ABC", "AB+C^"),
    ("*^ABC", "AB^C*"),
    ("*A^BC", "ABC^*"),

    # Mixed complex expressions
    ("+A*B-^CDE", "ABCD^E-*+"),
    ("*+AB+CD", "AB+CD+*"),
    ("*-A/BC-/AKL", "ABC/-AK/L-*"),

    # Single operand
    ("A", "A"),
    ("x", "x"),
    ("7", "7"),

    # Lowercase and digits
    ("+ab", "ab+"),
    ("+12", "12+"),
    ("+a*bc", "abc*+"),

    # Long expressions
    ("+-+A*BC/DE*FG", "ABC*+DE/-FG*+"),
]

run_tests(prefix_to_postfix, test_cases)