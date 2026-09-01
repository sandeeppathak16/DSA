from collections import defaultdict

def totalFruit(fruits):
    i = j = 0

    n = len(fruits)
    check = defaultdict(int)
    ans = 0

    while j < n:
        check[fruits[j]] += 1

        while len(check) > 2:
            check[fruits[i]] -= 1
            if check[fruits[i]] == 0:
                del check[fruits[i]]
            i += 1

        ans = max(ans, j - i + 1)

        j += 1


    return ans 