import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def largestOddNumber(num):
    ans = ""
    n = len(num)
    i = n - 1

    while i >= 0:
        if int(num[i]) % 2 == 1:
            ans = num[:i + 1]
            break

        i -= 1

    return ans
    


test_cases = [
    # LeetCode examples
    (("52",), "5"),
    (("4206",), ""),
    (("35427",), "35427"),

    # Single digit
    (("1",), "1"),
    (("2",), ""),
    (("9",), "9"),
    (("0",), ""),

    # Two digits
    (("51",), "51"),
    (("15",), "15"),
    (("50",), "5"),
    (("10",), "1"),
    (("12",), "1"),
    (("21",), "21"),

    # Already odd
    (("13579",), "13579"),
    (("99999",), "99999"),

    # Ends with even
    (("135790",), "13579"),
    (("24681",), "24681"),

    # Leading zeros
    (("00135",), "00135"),
    (("00042",), ""),
    (("00001",), "00001"),

    # Rightmost odd in the middle
    (("12345678",), "1234567"),
    (("1000008",), "1"),
    (("8000001",), "8000001"),

    # Multiple odd digits
    (("7312468",), "731"),
    (("2468135790",), "246813579"),
    (("9876543210",), "987654321"),

    # Large numbers
    (("123456789123456789",), "123456789123456789"),
]

run_tests(largestOddNumber, test_cases)