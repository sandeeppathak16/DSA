def lengthOfLongestSubstring(s):
    n = len(s)
    check = set()
    i, j = 0, 0
    ans = 0

    while j < n:
        while i <= j and s[j] in check:
            check.remove(s[i])
            i += 1

        ans = max(ans, (j - i) + 1)
        check.add(s[j])
        j += 1

    return ans