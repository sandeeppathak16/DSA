import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def postfix_to_prefix(string):
    if len(string) <= 1:
        return string
    
    stack = []

    for s in string:
        if s.isalnum():
            stack.append(s)

        else:
            a = stack.pop()
            b = stack.pop()

            stack.append(s + b + a)

    return stack[-1]
    
    


test_cases = [
    # Basic expressions
    ("AB+", "+AB"),
    ("AB-", "-AB"),
    ("AB*", "*AB"),
    ("AB/", "/AB"),
    ("AB^", "^AB"),

    # Operator precedence style cases
    ("ABC*+", "+A*BC"),
    ("AB*C+", "+*ABC"),
    ("AB+C-", "-+ABC"),
    ("AB*C/", "/*ABC"),

    # Parentheses-style structures
    ("AB+C*", "*+ABC"),
    ("ABC+*", "*A+BC"),
    ("AB+CD-*", "*+AB-CD"),

    # Nested expressions
    ("ABCD-*+", "+A*B-CD"),
    ("AB+C*D-", "-*+ABCD"),
    ("ABC+D*+", "+A*+BCD"),

    # Multiple operators
    ("ABC*+DE/-", "-+A*BC/DE"),
    ("AB*CD/+E-", "-+*AB/CDE"),

    # Exponentiation
    ("ABC^^", "^A^BC"),
    ("AB+C^", "^+ABC"),
    ("AB^C*", "*^ABC"),
    ("ABC^*", "*A^BC"),

    # Mixed complex expressions
    ("ABCD^E-*+", "+A*B-^CDE"),
    ("AB+CD+*", "*+AB+CD"),
    ("ABC/-AK/L-*", "*-A/BC-/AKL"),

    # Single operand
    ("A", "A"),
    ("x", "x"),
    ("7", "7"),

    # Lowercase and digits
    ("ab+", "+ab"),
    ("12+", "+12"),
    ("abc*+", "+a*bc"),

    # Long expressions
    ("ABC*+DE/-FG*+", "+-+A*BC/DE*FG"),
]

run_tests(postfix_to_prefix, test_cases)