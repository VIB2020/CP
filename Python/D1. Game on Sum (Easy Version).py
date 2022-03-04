#This is the easy version of the problem. The difference is the constraints on n, m and t. You can make hacks only if all versions of the problem are solved.

#Alice and Bob are given the numbers n, m and k, and play a game as follows:

#The game has a score that Alice tries to maximize, and Bob tries to minimize. 
# The score is initially 0. The game consists of n turns. Each turn, Alice picks a real number from 0 to k (inclusive) 
# which Bob either adds to or subtracts from the score of the game. But throughout the game, Bob has to choose to add at least m out of the n turns.

#Bob gets to know which number Alice picked before deciding whether to add or subtract 
# the number from the score, and Alice gets to know whether Bob added or subtracted the number for the previous turn 
# before picking the number for the current turn (except on the first turn since there was no previous turn).

#If Alice and Bob play optimally, what will the final score of the game be?

#Input
#The first line of the input contains a single integer t (1≤t≤1000) — the number of test cases. The description of test cases follows.

#Each test case consists of a single line containing the three integers, n, m, and k 
# (1≤m≤n≤2000,0≤k<109+7) — the number of turns, how many of those turns Bob has to add, and the biggest number Alice can choose, respectively.

#It is guaranteed that the sum of n over all test cases does not exceed 2000.

#Output
#For each test case output a single integer number — the score of the optimal game modulo 109+7.

#Formally, let M=109+7. It can be shown that the answer can be expressed as an irreducible fraction pq,
#  where p and q are integers and q≢0(modM). Output the integer equal to p⋅q−1modM. In other words, output such an integer x that 0≤x<M and x⋅q≡p(modM).

#Example
#inputCopy
#7
#3 3 2
#2 1 10
#6 3 10
#6 4 10
#100 1 1
#4 4 0
#69 4 20
#outputCopy
#6
#5
#375000012
#500000026
#958557139
#0
#49735962
#Note
#In the first test case, the entire game has 3 turns, and since m=3, Bob has to add in each of them.
#  Therefore Alice should pick the biggest number she can, which is k=2, every turn.

#In the third test case, Alice has a strategy to guarantee a score of 758≡375000012(mod109+7).

#In the fourth test case, Alice has a strategy to guarantee a score of 452≡500000026(mod109+7).

t = int(input())
n=[]
m=[]
k=[]
score=0
if t>=1 and t<=1000:
    for i in range(0,t):
        n[i] = int(input())
        m[i] = int(input())
        while m>=n:
            #n.pop(i)
            m.pop(i)
            m[i] = int(input())
        k[i]= int(input())
        
        #1<=m and m<=n and n<=1000 and k>=0 and k <= 10**9 and 
