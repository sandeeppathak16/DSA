import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def removeKdigits(num, k):
    stack = []
    removed = 0

    for digit in num:
        while stack and removed < k and digit < stack[-1]:
            stack.pop()
            removed += 1

        stack.append(digit)

    
    while removed < k:
        stack.pop()
        removed += 1

    result = "".join(stack).lstrip("0")

    return result or "0"



test_cases = [
    # LeetCode examples
    (("1432219", 3), "1219"),
    (("10200", 1), "200"),
    (("10", 2), "0"),

    # Single digit
    (("9", 1), "0"),
    (("1", 0), "1"),

    # Remove nothing
    (("12345", 0), "12345"),

    # Remove all digits
    (("12345", 5), "0"),

    # Increasing digits
    (("12345", 2), "123"),

    # Decreasing digits
    (("54321", 2), "321"),

    # All digits equal
    (("11111", 2), "111"),

    # Leading zeros after removal
    (("100200", 1), "200"),
    (("1000", 1), "0"),
    (("10001", 1), "1"),

    # Internal zeros
    (("120340", 2), "340"),

    # Repeated digits
    (("112", 1), "11"),
    (("221", 1), "21"),

    # Alternating digits
    (("121212", 3), "111"),

    # Large leading digit
    (("987654321", 4), "54321"),

    # Many zeros
    (("1000000", 1), "0"),
    (("1000001", 1), "1"),

    # Edge cases
    (("0", 0), "0"),
    (("0", 1), "0"),
    (("0000", 2), "0"),
]
run_tests(removeKdigits, test_cases)
