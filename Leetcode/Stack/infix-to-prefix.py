import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def pref(s):
    if s == '^':
        return 3

    if s in {'*', '/'}:
        return 2

    if s in {'+', '-'}:
        return 1

    return -1


def infix_to_prefix(string):
    ans = ''
    stack = []

    string = string[::-1]

    string = string.replace('(', '#')
    string = string.replace(')', '(')
    string = string.replace('#', ')')

    for s in string:

        if s.isalnum():
            ans += s

        elif s == '(':
            stack.append(s)

        elif s == ')':

            while stack and stack[-1] != '(':
                ans += stack.pop()

            stack.pop()

        else:
            if s == '^':
                while (
                    stack
                    and stack[-1] != '('
                    and pref(stack[-1]) >= pref(s)
                ):
                    ans += stack.pop()

            else:
                while (
                    stack
                    and stack[-1] != '('
                    and pref(stack[-1]) > pref(s)
                ):
                    ans += stack.pop()

            stack.append(s)

    while stack:
        ans += stack.pop()

    return ans[::-1]




test_cases = [
    # Basic expressions
    ("A+B", "+AB"),
    ("A-B", "-AB"),
    ("A*B", "*AB"),
    ("A/B", "/AB"),

    # Operator precedence
    ("A+B*C", "+A*BC"),
    ("A*B+C", "+*ABC"),
    ("A+B-C", "-+ABC"),
    ("A*B/C", "/*ABC"),

    # Parentheses handling
    ("(A+B)*C", "*+ABC"),
    ("A*(B+C)", "*A+BC"),
    ("(A+B)*(C-D)", "*+AB-CD"),
    ("((A+B))", "+AB"),

    # Nested parentheses
    ("A+(B*(C-D))", "+A*B-CD"),
    ("((A+B)*C)-D", "-*+ABCD"),
    ("A+((B+C)*D)", "+A*+BCD"),

    # Multiple operators
    ("A+B*C-D/E", "-+A*BC/DE"),
    ("A*B+C/D-E", "-+*AB/CDE"),

    # Exponent precedence
    ("A^B", "^AB"),
    ("A^B^C", "^A^BC"),  # right associative
    ("(A+B)^C", "^+ABC"),

    # Mixed operators
    ("A+B*C^D", "+A*B^CD"),
    ("(A+B)*(C+D)", "*+AB+CD"),
    ("A+B*(C^D-E)", "+A*B-^CDE"),

    # Single operand
    ("A", "A"),

    # Lowercase and digits
    ("a+b", "+ab"),
    ("1+2", "+12"),
    ("a+b*c", "+a*bc"),

    # Long expression
    ("A+B*C-D/E+F*G", "+-+A*BC/DE*FG"),
]

run_tests(infix_to_prefix, test_cases)