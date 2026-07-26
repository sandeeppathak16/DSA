def romanToInt(s: str) -> int:
        prev = 0

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for c in s[::-1]:
            v = mapping[c]

            if v < prev:
                ans -= v
            else:
                ans += v

            prev = v

        
        return ans