import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def prefix_to_infix(string):
    if len(string) <= 1:
        return string
    
    stack = []

    for s in string[::-1]:
        if s.isalnum():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            exp = f'({a}{s}{b})'
            stack.append(exp)

    return stack[0] 

test_cases = [
    # Basic expressions
    ("+AB", "(A+B)"),
    ("-AB", "(A-B)"),
    ("*AB", "(A*B)"),
    ("/AB", "(A/B)"),
    ("^AB", "(A^B)"),

    # Operator precedence style cases
    ("+A*BC", "(A+(B*C))"),
    ("+*ABC", "((A*B)+C)"),
    ("-+ABC", "((A+B)-C)"),
    ("/*ABC", "((A*B)/C)"),

    # Parentheses-heavy structures
    ("*+ABC", "((A+B)*C)"),
    ("*A+BC", "(A*(B+C))"),
    ("*+AB-CD", "((A+B)*(C-D))"),

    # Nested expressions
    ("+A*B-CD", "(A+(B*(C-D)))"),
    ("-*+ABCD", "(((A+B)*C)-D)"),
    ("+A*+BCD", "(A+((B+C)*D))"),

    # Multiple operators
    ("-+A*BC/DE", "((A+(B*C))-(D/E))"),
    ("-+*AB/CDE", "(((A*B)+(C/D))-E)"),

    # Exponentiation
    ("^A^BC", "(A^(B^C))"),
    ("^+ABC", "((A+B)^C)"),
    ("*^ABC", "((A^B)*C)"),
    ("*A^BC", "(A*(B^C))"),

    # Mixed complex expressions
    ("+A*B-^CDE", "(A+(B*((C^D)-E)))"),
    ("*+AB+CD", "((A+B)*(C+D))"),
    ("*-A/BC-/AKL", "((A-(B/C))*((A/K)-L))"),

    # Single operand
    ("A", "A"),
    ("x", "x"),
    ("7", "7"),

    # Lowercase and digits
    ("+ab", "(a+b)"),
    ("+12", "(1+2)"),
    ("+a*bc", "(a+(b*c))"),

    # Long expressions
    ("+-+A*BC/DE*FG", "(((A+(B*C))-(D/E))+(F*G))"),
]

run_tests(prefix_to_infix, test_cases)