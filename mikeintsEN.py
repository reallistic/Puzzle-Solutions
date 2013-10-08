from sys import stdin as sin
nl = list(sin.readline().rstrip() for i in range(int(sin.readline())))
for num in nl:
    print eval(("*".join(nl)+"*1").replace(num+"*","",1))
