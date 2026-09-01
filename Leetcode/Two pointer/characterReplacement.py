from collections import defaultdict

def characterReplacement(s, k):
    mapp = defaultdict(int)
    i = j = 0
    n = len(s)
    ans = 0
    max_freq = 0

    while j < n:
        mapp[s[j]] += 1
        max_freq = max(max_freq, mapp[s[j]])

        while (j - i + 1) - max_freq > k:
            mapp[s[i]] -= 1
            i += 1

        ans = max(ans, (j - i + 1))

        j += 1

    return ans 