import sys
import time
def check(a, b, p):
    """Check for average number of expected keystrokes"""
    f = []
    f.append(0.0)
    
    for i in range(1, a+1):
        f.append((1 - p[i-1]) + p[i-1] * f[i-1])
    
    enter = 2 + b
    finish =  (b - a) + 1 + f[a]*(1 + b) 
    backsp = finish
    for back in range(1, a+1): 
        backsp = min(backsp, back + (b - a + back) + 1 + f[a-back]*(1 + b) )
    
    return min(enter, backsp)
    
def writeresult(out):
    """ Write results to file """
    with open(".output","w") as results:
        results.write(out)

def getparam(inp, i):
    """ Get params form .input file """
    
    with open(inp) as paramf:
        p = paramf.readlines()
        return p[i]

if __name__ == '__main__':
    if len(sys.argv[1]) < 2:
        print "Please specify an input file to solve"
    else:
        fname = sys.argv[1]
        with open(fname, 'r') as params:
            frd = params.readlines()
            tc = int(frd[0])
        report_buf = ''
        # Clock duration of execution
        start = time.clock()
        odd = [ i for i in range(1,2*tc +1) if  i % 2 != 0]
        even = [ i for i in range(1,2*tc +1) if i % 2 == 0]

        for x in range(0, tc):
            prob_strls = (getparam(fname, even[x])).replace('\n','').split(' ')
            
            ksslen = (getparam(fname, odd[x])).replace('\n','').split(' ')

            ksfls = [int(j) for j in ksslen]
            prob_fls =  [ float(k) for k in  prob_strls]
            # Run check
            
            add_keystrk = check(ksfls[0], ksfls[1], prob_fls)
            report = "Case # %s: %s \n" %( str(x+1), str(add_keystrk))
            report_buf += report
        end = time.clock()
        writeresult(report_buf)
        print report_buf
        print "This solution ran in %s seconds" %(str(end-start))
