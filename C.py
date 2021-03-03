from sys import stdin
def popCL(UK):
    global CL
#    print("UK CL",UK)
    P = UK[-1]
    CL.append(P)
def popCC(UK):
    global CC
#    print("UK CC", UK)
    P = UK[0]
    CC.append(P)
def popCCP(UK):
    global CCP
#    print("UK CCP", UK)
    P = UK[UK.index(max(UK))]
    CCP.append(P)
def main():
    global CL, CC, CCP
    n = str(stdin.readline().strip())
    while n != "":
        n = int(n)
        UK = []
        pops = []
        CL = []
        CC = []
        CCP = []
        for i in range(n):
            a,b = [int(i) for i in stdin.readline().strip().split()]
            if a == 1:
                UK.append(b)
            else:
                pops.append(b)
                if b in  UK:
                    popCL(UK)
                    popCC(UK)
                    popCCP(UK)
##                print(CL)
##                print(CC)
##                print(CCP)
                    P = UK.index(b)
                    UK.pop(P)
        if CL == pops and not (CC == pops) and not (CCP == pops):
            print("stack")
        elif CC == pops and not (CL == pops) and not (CCP == pops):
            print("queue")
        elif CCP == pops and not (CL == pops) and not (CC == pops):
            print("priority queue")
        elif CCP == pops or CL == pops or CC == pops:
            print("not sure")
        else:
            print("impossible")
        n = str(stdin.readline().strip())
main()
