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
    if len(sys.argv[1]) < 2:
        print "Please specify an input file to run argument on"
    else:
        with open(sys.argv[1], 'r') as my_file:
            lines = sum(1 for line in my_file)
            keystrk_passlen = [int(i) for i in range(1, lines) if i % 2 == 1 ]
            with open(sys.argv[1], 'r') as my_file:
                file_rd = my_file.readlines()
                case = 1
                out = ''
                # clock duration of execution
                start = time.clock()
                for i in keystrk_passlen:
                    keystrk_strls = (file_rd[i]).replace('\n','').split(' ')
                    key_strk_fls = [int(j) for j in keystrk_strls]

                    prob_strls = (file_rd[i+1]).replace('\n','').split(' ')
                    prob_fls =  [ float(k) for k in  prob_strls]
                    add_keystrk = check(key_strk_fls[0],key_strk_fls[1], prob_fls)
                    out +=  "Case # %s: %s \n" %( str(case), str(add_keystrk))
                    case +=1
                print out
                end = time.clock()
                print "This solution ran in %s seconds" %(str(end-start))