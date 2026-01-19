# A. Blackslex and Password
# time limit per test1 second
# memory limit per test256 megabytes
# Blackslex is designing a log-in system for Gean Dev and discovered that most users use weak passwords.
#
# To resolve this issue, he posed the following conditions, dependent on two variables k
#  and x
# , for all passwords. Each password is a string s
#  of length n
#  satisfying these properties.
#
# s
#  uses only the first k
#  lowercase letters of the English alphabet.
# For every pair of indices 1≤i<j≤n
#  such that (j−i)
#  is divisible by x
# , the letters si
#  and sj
#  are different.
# Find the smallest integer n
#  such that no valid string of length n
#  exists.
#
# Input
# The first line contains a single integer t
#  (1≤t≤500
# ) — the number of test cases.
#
# The first and only line of each test case contains two integers k
#  and x
#  (1≤k≤26
# , 1≤x≤15
# ).
#
# Output
# For each test case, output the minimal n
# .
#
# Example
# InputCopy
# 3
# 2 1
# 3 2
# 1 5
# OutputCopy
# 3
# 7
# 6
# Note
# For the first test case, there are no valid strings of length n=3
# . For n=2
# , one such valid example is ab. Note that the only pair (i,j)
#  that (j−i)
#  is divisible by x=1
#  and 1≤i<j≤n
#  for n=2
#  is (1,2)
# .
#
# For the second test case, there are no valid strings of length n=7
# . For n=6
# , one such valid example is aabccb. Note that all pairs (i,j)
#  that (j−i)
#  is divisible by x=2
#  and 1≤i<j≤n
#  for n=6
#  include (1,3)
# , (1,5)
# , (2,4)
# , (2,6)
# , (3,5)
# , and (4,6)
# .
#
# For the third test case, there are no valid strings of length n=6
# . For n=5
# , one such valid example is aaaaa. Note that there are no pairs (i,j)
#  that (j−i)
#  is divisible by x=5
#  and 1≤i<j≤n
#  for n=5

def solve():
    t = int(input())
    for _ in range(t):
        k, x = map(int, input().split())

        n = 1
        while True:
            max_chain = (n + x - 1) // x

            if max_chain > k:
                print(n)
                break

            n += 1


solve()



# After his IMO medalist friend showered for two hours so that "he doesn't have to shower this again this week," Blackslex will be late for class!
#
# In order to get to class, Blackslex must take the crowded elevator to many floors in a certain order. Because he is a hacker, he can skip visiting up to one floor without the other people knowing. His time taken is the sum of the absolute differences between consecutive floor numbers. Find the minimum time taken, given that he can skip up to one floor.
#
# More formally, given an array a=[a1,a2,…,an]
#  of n
#  integers, you can choose up to one index k∈{1,2,…,n}
#  to erase such that the sum
# ∑i=1n−2|bi−bi+1|
# is minimized, where b=[a1,…,ak−1,ak+1,…,an]
#  is the array after erasing element ak
# . Report the minimum sum.
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains one integer n
#  (3≤n≤2⋅105
# ) — the size of the array.
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤100
# ).
#
# It is guaranteed that the sum of n
#  does not exceed 2⋅105
#  over all test cases.
#
# Output
# For each test case, output a single real number — the minimum time taken.
#
# Example
# InputCopy
# 3
# 5
# 4 15 1 7 9
# 3
# 2 4 8
# 6
# 11 13 17 19 23 29
# OutputCopy
# 11
# 2
# 12
# Note
# For the first test case, one optimal index to remove from [4,15,1,7,9]
#  is k=2
# . The array becomes [4,1,7,9]
#  and the time taken is 11
# . For the second test case, the optimal index to remove is k=3
# .






#
#
# Blackslex worked too hard and started dreaming about numbers. Solve the following task from his dreams.
#
# You are given an array a1,a2,…,an
# .
#
# In one operation you choose an index i
#  (1≤i≤n
# ) and an integer x
#  which is at least k
#  and set
# ai:=aimodx,
# where umodv
#  denotes the remainder of dividing u
#  by v
# .
#
# Your goal is to make all elements of the array identical. Among all positive integers k
# , determine the maximum k
#  for which there exists a finite sequence of the above operations that makes all array elements equal.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (2≤n≤2⋅105
# ).
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# , all values of a
#  are distinct).
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, print a single integer — the maximum positive integer k
#  such that it is possible to make all elements of the array identical using any number of operations with moduli x
#  restricted to k≤x
# .
#
# Example
# InputCopy
# 3
# 3
# 5 7 9
# 2
# 2 3
# 7
# 11 74 5 22 52 97 82
# OutputCopy
# 5
# 2
# 6


# Penguins are civilized creatures that communicate using permutations. Blackslex, as a penguin researcher, must study their means of communication.
#
# For a given integer n
# , consider permutations∗
#  p
#  of the array [0,1,…,2n−1]
# . Define
# S(p)=∑i=02n−1popcount(p0&p1&⋯&pi),
# where popcount(z)
#  is the number of 1
# -bits in the binary representation of z
#  (for instance, popcount(5)=2
#  because 5=1012
#  has two 1
# -bits in the binary representation), and &
#  denotes the bitwise AND operation. .
#
# A permutation is considered sacred if it maximizes S(p)
# . Find the lexicographically minimal†
#  sacred permutation.
#
# ∗
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).
#
# †
# An array a
#  is lexicographically smaller than an array b
#  of the same size if and only if the following holds:
#
# in the first position where a
#  and b
#  differ, the array a
#  has a smaller element than the corresponding element in b
# .
# Input
# The first line contains a single integer t
#  (1≤t≤16
# ) — the number of test cases.
#
# Each test case contains a single integer n
#  (1≤n≤16
# ).
#
# It is guaranteed that the sum of 2n
#  over all test cases does not exceed 216
# .
#
# Output
# For each test case, output 2n
#  integers p0,p1,…,p2n−1
#  — the required permutation.
#
# Example
# InputCopy
# 2
# 1
# 2
# OutputCopy
# 1 0
# 3 1 0 2
# Note
# For the first test case, there are two possible permutations.
#
# p=[0,1]
# , S(p)=0
# p=[1,0]
# , S(p)=1
# For the second test case, S([3,1,0,2])=3
#  is sacred. There are other permutations p
#  that are sacred, such as p=[3,2,0,1]
# , but those are not lexicographically minimal.

#
# E. Blackslex and Girls
# time limit per test2 seconds
# memory limit per test256 megabytes
# After failing to pick up a girl using De Bruijn sequence of fixed-length bitstrings, Blackslex has turned his attention towards politics.
#
# Due to his high charisma, he is now in charge of drawing borders for the n
#  voting districts of his country. In Blackslex's country, there are x
#  voters for party A and y
#  voters for party B. Using his amazing drawing skills, he can allocate voters from any party into any district of his choice.
#
# His history with bitstrings has led him to wonder if he can allocate voters such that the winner of each district follows a certain bitstring pattern. To avoid suspicion, he must also allocate at least pi
#  voters into each district. Tell him if it is possible!
#
# Formally, you are given a binary string s
#  of length n
# , an array p
#  of length n
# , and two integers x
#  and y
# .
#
# You want to determine whether there exist two arrays of nonnegative integers a
#  and b
#  of length n
#  that satisfy the following conditions:
#
# a1+a2+⋯+an=x
# b1+b2+⋯+bn=y
# For every 1≤i≤n
# , ai+bi≥pi
# For every 1≤i≤n
# :
# If si=0
#  then ai>bi
# If si=1
#  then bi>ai
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains three integers n
# , x
# , and y
#  (1≤n≤2⋅105
# , 1≤x,y≤109
# ).
#
# The second line contains a binary string s
#  of length n
# .
#
# The third line contains n
#  integers p1,p2,…,pn
#  (1≤pi≤109
# ).
#
# The sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, print (case-insensitive) YES if there exist arrays a,b
#  satisfying all conditions, or NO otherwise.
#
# Example
# InputCopy
# 6
# 3 5 5
# 010
# 2 4 3
# 4 2 3
# 0001
# 1 1 1 1
# 2 4 2
# 00
# 3 3
# 4 23 20
# 1111
# 2 2 2 2
# 1 25 26
# 0
# 51
# 2 4 2
# 00
# 3 4
# OutputCopy
# YES
# NO
# YES
# NO
# NO
# NO
# Note
# In the first test case, one of the possible distributions of voters is: a=[2,0,3]
#  and b=[0,4,1]
# .
#
# In the third test case, one of the possible distributions of voters is: a=[2,2]
#  and b=[1,1]
# .
#
# For the other test cases, it can be shown that there are no distributions of voters that satisfy the conditions.



# F. Blackslex and Another RGB Walking
# time limit per test5 seconds
# memory limit per test256 megabytes
# This is a run-twice (communication) problem.
#
# There are two players: Player A (Agent) and Player B (Blackslex). The jury will first interact with player A. After player A ends their interaction, the jury will interact with player B. Note that player A and player B may not directly pass information to each other; both players are only able to send information or receive information from the jury, but they may agree on the strategy they will use to communicate.
#
# The Penguin Republic is a bipartite connected undirected graph G
#  with n
#  vertices and m
#  edges. Blackslex is going to conduct forbidden field research at vertex 1
# . Due to travel restrictions, he will be dropped off at an unknown vertex v
#  (2≤v≤n
# ). He must get to vertex 1
#  while having no information on the graph.
#
# For his journey, he has bribed a penguin agent and agreed to some communication strategy using the following method; the agent will discreetly mark each vertex in one of the three colors: red, green, or blue. From Blackslex's perspective, he will see only the color ci
#  of each neighbor ui
#  (1≤i≤d(v)
# ∗
# ) of v
# . He must choose some j
#  (1≤j≤d(v)
# ) and move to vertex uj
#  such that he is closer to vertex 1
# .
#
# Note that the neighbors are arbitrarily ordered. He sees only the colors of the neighboring vertices, and not the vertex that he is on. Additionally, he does not know the index of the vertex he's on, the neighboring vertices, or any other vertex.
#
# Your task is to implement the strategy for both the agent and Blackslex. For the agent, you must color each vertex in one of the three colors. For Blackslex, you are given q
#  queries. In each query, you are dropped off at an arbitrary and unknown vertex v
#  and given the color of the neighboring vertices. You must determine a vertex to go to such that you are closer to vertex 1
# .
#
# ∗
# The number of neighbors of vertex v
# .
#
# Input
# Your code will be ran exactly two times on each test. On the first run, you will be Player A (Agent), and on the second Player B (Blackslex).
#
# First Run Input
#
# The first line of the input contains the string first. The purpose of this is so your program recognizes that this is its first run, and it should act as Player A.
#
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and m
#  (2≤n≤105
# , n−1≤m≤105
# ) — the number of vertices and edges respectively.
#
# The following m
#  lines contain information about the edges. The i
# -th (1≤i≤m
# ) line has two integers ai
#  and bi
# . (1≤ai,bi≤n
# , ai≠bi
# ) — vertex ai
#  is connected to vertex bi
#  by edge i
# .
#
# It is guaranteed that:
#
# The sum of n
#  and the sum of m
#  does not exceed 105
#  over all test cases.
# The graph in each test case is bipartite and connected. It has no duplicate edges and no self-loops.
# Second Run Input
#
# The first line of the input contains the string second. The purpose of this is so your program recognizes that this is its second run, and it should act as Player B.
#
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ) — the same value of t
#  in the first run. The description of the test cases follows.
#
# The first line of each test case contains one integer q
#  (1≤q≤105
# ) — the number of queries in this test case.
#
# The first line of each query contains one integer d(v)
#  (1≤d(v)≤105
# ) — the number of neighbors of the vertex v
#  that Blackslex is currently on.
#
# The next line of each query contains a string c
#  of length d(v)
#  — the i
# -th (1≤i≤d(v)
# ) character of the string is the color of the neighboring vertex ui
# . The characters in the string are r, g, or b representing red, green, or blue.
#
# It is guaranteed that:
#
# The sum of q
#  does not exceed 105
#  over all queries in all test cases.
# The sum of d(v)
#  does not exceed 2⋅105
#  over all queries in all test cases.
# v≠1
# The input of the second run is not adaptive. In other words, the input of the second run will not change in different runs.
#
# Hacks
#
# To make hacks, use the following format:
#
# The first line contains two integers t
#  (1≤t≤104
# ) — the number of test cases.
#
# The description of the test cases for the first run follows.
#
# The first line of each test case contains two integers n
#  and m
#  (2≤n≤105
# , n−1≤m≤105
# ) — the number of vertices and edges respectively.
#
# The following m
#  lines contain information about the edges. The i
# -th (1≤i≤m
# ) line has two integers ai
#  and bi
# . (1≤ai,bi≤n
# , ai≠bi
# ) — vertex ai
#  is connected to vertex bi
#  by edge i
# .
#
# After that, the description of the test cases for the second run follows.
#
# The first line of each test case contains one integer q
#  (1≤q≤105
# ) — the number of queries in this test case.
#
# The first line of each query contains one integer v
#  (2≤v≤n
# ) — the vertex the Blackslex is dropped off.
#
# The second line of each query contains d(v)
#  integers p1,p2,…,pd(v)
#  (1≤pi≤d(v)
# , each number in p
#  is distinct) — the ordering of the neighbor is as follows; let q1<q2<…<qd(v)
#  be the neighbors of v
# , then the input order of the neighbor is ui=qpi
# .
#
# It must hold that:
#
# The sum of n
#  and the sum of m
#  does not exceed 105
#  over all test cases in the first run.
# The graph in each test case is bipartite and connected. It has no duplicate edges and no self-loops.
# The sum of q
#  does not exceed 105
#  over all queries in all test cases.
# The sum of d(v)
#  does not exceed 2⋅105
#  over all test cases in the second run.
# Output
# For the first run, for each test case, output a single string s
#  of length n
#  — si
#  (1≤i≤n
# ) is the color of the i
# -th vertex, painted by the agent. The characters in the string are r, g, or b representing red, green, or blue.
#
# For the second run, for each query in each test case, output a single integer j
#  (1≤j≤d(v)
# ) — uj
#  is the neighboring vertex that Blackslex will go to next.
#
# Examples
# InputCopy
# first
# 2
# 7 8
# 1 2
# 1 6
# 3 2
# 4 2
# 6 4
# 4 7
# 5 6
# 5 7
#
# 4 4
# 1 2
# 1 4
# 3 2
# 3 4
# OutputCopy
# rrgbggr
# rbbb
# InputCopy
# second
# 2
# 2
# 3
# grr
# 3
# gbr
#
# 1
# 2
# rb
# OutputCopy
# 1
# 3
# 1
# Note
# Graph and coloring of both tests.
# In the sample, there are two test cases. The graph and the sample's vertex coloring are demonstrated in the picture above.
#
# In the second run, the first test case has two queries.
#
# The first query is on vertex 4
#  with the neighbors ordered as vertex 6
# , 2
# , and 7
# . Choosing the first neighbor is walking to vertex 6
# .
#
# The second query is on vertex 6
#  with the neighbors ordered as vertex 5
# , 4
# , and 1
# . Choosing the third neighbor is walking to vertex 1
# .
#
# The second test case has a single query on vertex 2
#  with the neighbors ordered as vertex 1
#  and 3
# . Choosing the first neighbor is walking to vertex 1
# .
#
# Note that the empty lines are made to assist reading. Actual test cases do not have empty lines.



# G. Blackslex and Penguin Migration
# time limit per test5 seconds
# memory limit per test256 megabytes
# IOI 2025 - Migrations
# This is an interactive problem.
#
# The species of penguins that Blackslex is researching lives on an island that is a grid with n
#  rows and n
#  columns. Exactly one penguin lives in each one cell of the grid.
#
# He labelled each penguin as an integer from 1
#  to n2
# . After some time, some penguins migrated to another cell. After migration, every penguin will still be in some cell on the grid, and every cell contains exactly one penguin. He needs the current position of every penguin.
#
# To do so, he can ask a penguin how far another penguin is from it.
#
# Formally, for a possible grid x
#  representing the position of all penguins, denote dist(x,i,j)
#  as the Manhattan distance of the penguin i
#  to the penguin j
#  in x
# ∗
# .
#
# There is a hidden grid a
#  with n
#  rows and n
#  columns. You need to find a grid b
#  that satisfies
#
# b
#  has n
#  rows and n
#  columns.
# Each cell of b
#  contains an integer from 1
#  to n2
# , which is a penguin's label. Each integer will be in a single cell.
# For all 1≤i,j≤n2
# , it holds that dist(a,i,j)=dist(b,i,j)
# .
# To do so, you may make the following query no more than 3n2+150
#  times.
#
# Given i
# , j
#  (1≤i,j≤n2
# ), receive the value of dist(a,i,j)
# .
# ∗
# Let ri
# , ci
#  denote the row and column that the penguin i
#  is in, and denote the same for rj
# , cj
# , then the Manhattan distance is |ri−rj|+|ci−cj|
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤200
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the size of the island.
#
# It is guaranteed that the total sum of all values of n
#  across all test cases does not exceed 500
# .
#
# Interaction
# To ask a query, pick two integer i
# , j
#  (1≤i,j≤n2
# ) and print "? i
#  j
# " (without quotes) to a line.
#
# You will receive a single integer, which is the distance between penguins i
#  and j
# .
#
# You may make no more than 3n2+150
#  queries in each test case.
#
# After you finish your queries, output "!" in a line, then output n
#  lines, each containing n
#  integers, the j
# -th integer on the i
# -th line is bi,j
# .
#
# Your output must satisfy the conditions given, and you may output any such b
#  if multiple are possible. Note that this is not considered a query and is not taken into account when counting the number of queries asked.
#
# After this, proceed to the next test case.
#
# The interactor in this task is not adaptive. In other words, the grid does not change during the interaction.
#
# If you make more than 3n2+150
#  queries in a test case during an interaction, your program must terminate immediately, and you will receive the Wrong Answer verdict. Otherwise, you can get an arbitrary verdict because your solution will continue to read from a closed stream.
#
# After printing a query do not forget to output the end of line and flush the output. Otherwise, you will get Idleness limit exceeded. To do this, use:
#
# fflush(stdout) or cout.flush() in C++;
# System.out.flush() in Java;
# flush(output) in Pascal;
# stdout.flush() in Python;
# see the documentation for other languages.
# Hacks
#
# To hack, follow the test format below.
#
# The first line contains the number of test cases t
#  (1≤t≤200
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the size of the island.
#
# The next n
#  lines contain n
#  integers, the j
# -th integer on the i
# -th line is ai,j
#  — the label of the penguin on row i
# , column j
# .
#
# It must hold that the total sum of all values of n
#  across all test cases does not exceed 500
# .
#
# Example
# InputCopy
# 2
# 2
#
# 1
#
# 2
#
# 1
#
# 1
#
# 2
#
# 1
#
# 3
#
# 3
# OutputCopy
# ? 1 2
#
# ? 1 3
#
# ? 1 4
#
# ? 2 3
#
# ? 2 4
#
# ? 3 4
#
# !
# 3 4
# 2 1
#
# ? 1 8
#
# !
# 9 1 3
# 4 2 7
# 8 5 6
# Note
# Note that additional lines are for ease of reading. Your solution should not output these additional lines.
#
# In the first test case, the grid a
#  is
#
# 1	4
# 2	3
# In the second test case, the grid a
#  is
#
# 9	1	3
# 4	2	7
# 8	5	6
# The interaction is as follows.
#
# Contestant	Judge	Description
# 2	Start of the first test case. The island has size n=2
# .
# ? 1 2		The contestant asks for the distance of penguin labelled 1
#  and 2
# .
# 1	The distance of penguin labelled 1
#  and 2
#  is 1
# .
# ? 1 3		The contestant asks for the distance of penguin labelled 1
#  and 3
# .
# 2	The distance of penguin labelled 1
#  and 3
#  is 2
# .
# ? 1 4		The contestant asks for the distance of penguin labelled 1
#  and 4
# .
# 1	The distance of penguin labelled 1
#  and 4
#  is 1
# .
# ? 2 3		The contestant asks for the distance of penguin labelled 2
#  and 3
# .
# 1	The distance of penguin labelled 2
#  and 3
#  is 1
# .
# ? 2 4		The contestant asks for the distance of penguin labelled 2
#  and 4
# .
# 2	The distance of penguin labelled 2
#  and 4
#  is 2
# .
# ? 3 4		The contestant asks for the distance of penguin labelled 3
#  and 4
# .
# 1	The distance of penguin labelled 3
#  and 4
#  is 1
# .
# !		The contestant determined a possible grid b
# .
# 3 4		Note that the grid need not be exactly the same, but it must hold that dist(a,i,j)=dist(b,i,j)
#  for all 1≤i,j≤n2
# .
# 2 1
# 3	Start of the second test case. The island has size n=3
# .
# ? 1 8		The contestant asks for the distance of penguin labelled 1
#  and 8
# .
# 3	The distance of penguin labelled 1
#  and 8
#  is 3
# .
# !		The contestant determined a possible grid b
# .
# 9 1 3
# 4 2 7
# 8 5 6


# H. Blackslex and Plants
# time limit per test2 seconds
# memory limit per test512 megabytes
# Blackslex has found solace in plants and trees amidst accumulated stress from strained relationships, stressful politics, and strenuous research.
#
# Blackslex has n
#  plants ordered in a straight line, consisting of plant 1,2,3,…n
# . Initially, every plant contains 0
#  millilitres of water.
#
# He wants to perform q
#  watering operations as follows :
#
# Given l,r
#  for each operation
# water f(i−l+1)
#  millilitres of water onto the i
# -th plant for every l≤i≤r
# where f(x)
#  denotes the product of x
#  and the value of the least significant bit of x
#  ∗
#  Your task is to figure out the amount of water in each plant after all watering operations are done.
#
# ∗
# The value of the least significant bit of x
#  is the value of the rightmost bit in the binary representation of x
# . For instance, the value of the least significant bit of 10=10102
#  is 00102=2
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
# , q
#  (1≤n,q≤2⋅105
# ) — the number of plants and the number of watering operations, respectively.
#
# The next q
#  lines of each test case contain two integers l
# , r
#  (1≤l≤r≤n
# ) — the left bound and the right bound for each watering operation.
#
# It is guaranteed that the sum of all values of n
#  and the sum of all values of q
#  across all test cases do not exceed 2⋅105
# .
#
# Output
# For each test case, output n
#  integers representing the amount of water in the i
# -th plant for each i=1,2,3,…,n
#
# Example
# InputCopy
# 2
# 5 3
# 1 5
# 2 3
# 2 5
# 7 7
# 1 3
# 1 6
# 3 7
# 4 7
# 7 7
# 1 6
# 5 5
# OutputCopy
# 1 6 11 19 21
# 3 12 10 37 18 43 22
# Note
# In the first case, each operation will be performed as follows :
#
# The first operation will :
# water the 1
# -st plant using f(1−1+1)=f(1)=1
#  millilitres of water.
# water the 2
# -nd plant using f(2−1+1)=f(2)=4
#  millilitres of water.
# water the 3
# -rd plant using f(3−1+1)=f(3)=3
#  millilitres of water.
# water the 4
# -th plant using f(4−1+1)=f(4)=16
#  millilitres of water.
# water the 5
# -th plant using f(5−1+1)=f(5)=5
#  millilitres of water.
# The second operation will :
# water the 2
# -nd plant using f(2−2+1)=f(1)=1
#  millilitres of water.
# water the 3
# -rd plant using f(3−2+1)=f(2)=4
#  millilitres of water.
# The third operation will :
# water the 2
# -nd plant using f(2−2+1)=f(1)=1
#  millilitres of water.
# water the 3
# -rd plant using f(3−2+1)=f(2)=4
#  millilitres of water.
# water the 4
# -th plant using f(4−2+1)=f(3)=3
#  millilitres of water.
# water the 5
# -th plant using f(5−2+1)=f(4)=16
#  millilitres of water.
# Hence, the total amount of water in each plant is :
#
# 1
#  millilitres
# 4+1+1=6
#  millilitres
# 3+4+4=11
#  millilitres
# 16+3=19
#  millilitres
# 5+16=21
#  millilitres
