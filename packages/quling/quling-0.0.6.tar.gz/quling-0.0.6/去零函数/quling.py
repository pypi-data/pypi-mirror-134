def ql(s):
    n=s
    i=0
    for a in n:
        if a=="0":
            i=i+1
        else:
            break
    if i==0:
        n=eval(n)
    else:
        if i==1:
            if n[1]==".":
                n=eval(n)
            else:
                n=eval(n[1:])
        else:
            n=eval(n[i:])
    return n