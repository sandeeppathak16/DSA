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


def infix_to_postfix(string):
    ans = ''
    stack = []

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
            while stack and stack[-1] != '(' and pref(s) <= pref(
                stack[-1]
            ):
                ans += stack.pop()

            stack.append(s)

    while stack:
        ans += stack.pop()

    return ans 


test_cases = [
    # Basic expressions
    ("A+B", "AB+"),
    ("A-B", "AB-"),
    ("A*B", "AB*"),
    ("A/B", "AB/"),

    # Operator precedence
    ("A+B*C", "ABC*+"),
    ("A*B+C", "AB*C+"),
    ("A+B-C", "AB+C-"),
    ("A*B/C", "AB*C/"),

    # Parentheses handling
    ("(A+B)*C", "AB+C*"),
    ("A*(B+C)", "ABC+*"),
    ("(A+B)*(C-D)", "AB+CD-*"),
    ("((A+B))", "AB+"),

    # Nested parentheses
    ("A+(B*(C-D))", "ABCD-*+"),
    ("((A+B)*C)-D", "AB+C*D-"),
    ("A+((B+C)*D)", "ABC+D*+"),

    # Multiple operators
    ("A+B*C-D/E", "ABC*+DE/-"),
    ("A*B+C/D-E", "AB*CD/+E-"),

    # Exponent precedence
    ("A^B", "AB^"),
    ("(A+B)^C", "AB+C^"),

    # Mixed operators
    ("A+B*C^D", "ABCD^*+"),
    ("(A+B)*(C+D)", "AB+CD+*"),
    ("A+B*(C^D-E)", "ABCD^E-*+"),

    # Single operand
    ("A", "A"),

    # Lowercase and digits
    ("a+b", "ab+"),
    ("1+2", "12+"),
    ("a+b*c", "abc*+"),

    # Long expression
    ("A+B*C-D/E+F*G", "ABC*+DE/-FG*+"),
]

run_tests(infix_to_postfix, test_cases)