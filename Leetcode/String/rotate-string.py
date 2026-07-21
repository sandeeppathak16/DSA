import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def rotateString(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)
        


test_cases = [
    # LeetCode examples
    (("abcde", "cdeab"), True),
    (("abcde", "abced"), False),

    # Same strings
    (("abc", "abc"), True),
    (("a", "a"), True),
    (("", ""), True),

    # Single character
    (("a", "b"), False),

    # Two characters
    (("ab", "ba"), True),
    (("ab", "ab"), True),
    (("ab", "aa"), False),

    # Different lengths
    (("abc", "ab"), False),
    (("ab", "abc"), False),
    (("", "a"), False),
    (("a", ""), False),

    # Multiple valid rotations
    (("waterbottle", "erbottlewat"), True),
    (("rotation", "tionrota"), True),
    (("rotation", "tationro"), True),

    # Repeated characters
    (("aaaa", "aaaa"), True),
    (("aaaa", "aaab"), False),
    (("abab", "baba"), True),
    (("abab", "abba"), False),

    # Rotation by one position
    (("abcdef", "fabcde"), True),
    (("abcdef", "bcdefa"), True),

    # Rotation by n-1 positions
    (("abcdef", "efabcd"), True),

    # No possible rotation
    (("abcd", "acbd"), False),
    (("xyz", "zyx"), False),

    # Larger strings
    (("abcdefghijklmnopqrstuvwxyz",
      "mnopqrstuvwxyzabcdefghijkl"), True),

    # Edge cases
    (("z", "z"), True),
    (("z", "x"), False),
]
run_tests(rotateString, test_cases)