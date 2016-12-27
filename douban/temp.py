def removeDuplicates(A):
    if not A:
        return 0
    x=0
    last=A[0]
    times=0
    while x<len(A):
        print A[x]
        if A[x]==last:
            if times==2:
                print "del",A[x]
                del A[x]
                x-=1
            else:
                times+=1
                print "times",times
        else:
            last=A[x]
            times=1
            print "last",last
            print "times",times
        x+=1
        print times
    return len(A)
A=[14,14,14,14,13,13,13,13]
removeDuplicates(A)
print A