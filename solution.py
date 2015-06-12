import sys
import time
def check(a, b, p):
    dp = []
    dp.append(0.0)
    for i in range(1, a+1):
        dp.append((1 - p[i-1]) + p[i-1] * dp[i-1])
    
    giveup = 2 + b
    
    finish = (b - a) + 1 + dp[a]*(1 + b)
    backspace = finish;

    for back in range(1, a+1): 
        backspace = min(backspace, back + (b - a + back) + 1 + dp[a-back]*(1 + b) )
    
    return min(giveup, backspace)
    

if __name__ == '__main__':
    pass