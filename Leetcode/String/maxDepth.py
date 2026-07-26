def maxDepth(s: str) -> int:
    max_counter = 0

    counter = 0

    for ch in s:
        if ch == '(':
            counter += 1
        elif ch == ')':
            counter -= 1

        
        max_counter = max(max_counter, counter)

    
    return max_counter