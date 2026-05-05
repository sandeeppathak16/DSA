def solve(filename='17.txt'):
    with open(filename, 'r') as file:
        containers = [int(line.strip()) for line in file.readlines()]

    ans = [0, {}] 

    def combination(containers, target, ans, k, l):
        if target == 0:
            ans[0] += 1
            ans[1][l] = ans[1].get(l, 0) + 1
            return
        
        if target < 0:
            return
        
        for i in range(k, len(containers)):
            combination(
                containers=containers,
                target=target - containers[i],
                ans=ans,
                k=i + 1,
                l=l + 1
            )

        return ans

    return combination(
        containers=containers,
        target=150,
        ans=ans,
        k=0,
        l=0
    )


print(solve())