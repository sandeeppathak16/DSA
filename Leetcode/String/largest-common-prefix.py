import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    for i, ch in enumerate(strs[0]):
        for word in strs:
            if i == len(word) or word[i] != ch:
                return strs[0][:i]
            
    return strs[0]
    


test_cases = [
    # LeetCode examples
    ((["flower", "flow", "flight"],), "fl"),
    ((["dog", "racecar", "car"],), ""),

    # Single string
    ((["hello"],), "hello"),
    (([""],), ""),

    # Two strings
    ((["abc", "abc"],), "abc"),
    ((["abc", "abd"],), "ab"),
    ((["abc", "xyz"],), ""),

    # One string is prefix
    ((["app", "apple", "application"],), "app"),
    ((["apple", "app"],), "app"),

    # All identical
    ((["test", "test", "test"],), "test"),

    # Empty string present
    ((["", "abc"],), ""),
    ((["abc", ""],), ""),
    ((["", ""],), ""),

    # Different lengths
    ((["a", "ab", "abc"],), "a"),
    ((["ab", "a"],), "a"),
    ((["abcd", "abc", "ab"],), "ab"),

    # No common prefix
    ((["a", "b", "c"],), ""),
    ((["xyz", "abc"],), ""),

    # Case sensitivity
    ((["Flower", "flow"],), ""),
    ((["Flow", "Flowing"],), "Flow"),

    # Long common prefix
    ((["interstellar", "internet", "internal"],), "inter"),

    # Prefix disappears gradually
    ((["abcdef", "abcxyz", "abc123"],), "abc"),
    ((["abcdef", "abxyz", "a123"],), "a"),

    # All single characters
    ((["a", "a", "a"],), "a"),
    ((["a", "b"],), ""),

    # Edge case
    (([],), ""),
]

run_tests(longestCommonPrefix, test_cases)