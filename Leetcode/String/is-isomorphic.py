import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def isIsomorphic(s: str, t: str) -> bool:
    mapping = {}
    rev_mapping = {}

    for i in range(len(s)):
        ss = s[i]
        st = t[i]

        if ss not in mapping:
            mapping[ss] = st
        else:
            if mapping[ss] != st:
                return False
            
        if st not in rev_mapping:
            rev_mapping[st] = ss
        else:
            if rev_mapping[st] != ss:
                return False
            
    return True


test_cases = [
    # LeetCode examples
    (("egg", "add"), True),
    (("foo", "bar"), False),
    (("paper", "title"), True),

    # Single character
    (("a", "b"), True),
    (("a", "a"), True),

    # Same strings
    (("abc", "abc"), True),
    (("aaaa", "aaaa"), True),

    # Repeated characters
    (("ab", "aa"), False),
    (("aa", "ab"), False),
    (("abab", "baba"), True),
    (("abab", "bbaa"), False),

    # Different mapping conflicts
    (("badc", "baba"), False),
    (("abca", "zbxz"), True),
    (("abca", "zbxy"), False),

    # Reverse mapping conflicts
    (("ab", "cc"), False),
    (("abc", "ddd"), False),
    (("abcd", "eeee"), False),

    # Unique mappings
    (("abcd", "wxyz"), True),
    (("xyz", "abc"), True),

    # Longer examples
    (("abcdefghijklmnopqrstuvwxyz",
      "bcdefghijklmnopqrstuvwxyza"), True),

    # Multiple repeated groups
    (("aabbcc", "xxyyzz"), True),
    (("aabbcc", "xxyyzy"), False),

    # Numbers as characters
    (("1212", "3434"), True),
    (("1212", "3444"), False),

    # Mixed characters
    (("ab!a", "cd#c"), True),
    (("ab!a", "cd#d"), False),

    # Empty strings
    (("", ""), True),

    # Longer conflicting mapping
    (("paperpaper", "titletitle"), True),

    # Edge cases
    (("zzzz", "aaaa"), True),
    (("zzzz", "aaab"), False),
]
run_tests(isIsomorphic, test_cases)