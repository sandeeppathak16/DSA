def longestPalindrome(s: str) -> str:

    resI = 0
    resL = 0

    n = len(s)

    for i in range(n):
        j, k = i, i

        while j >= 0 and k < n and s[j] == s[k]:
            if (k - j + 1) > resL:
                resL = (k - j + 1)
                resI = j

            j -= 1
            k += 1

        j, k = i, i + 1

        while j >= 0 and k < n and s[j] == s[k]:
            if (k - j + 1) > resL:
                resL = (k - j + 1)
                resI = j

            j -= 1
            k += 1

    return s[resI: resL + resI]