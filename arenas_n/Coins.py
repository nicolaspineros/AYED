from sys import stdin
import sys
sys.setrecursionlimit(100000)
def main():
    global coins
    global sols
    sols = {}
    coins = [1,5,10,25,50]
    want = str(stdin.readline().strip())
    while want != "":
        forms = (Comp(int(want),0))
        if forms == 1:
            print("There is only 1 way to produce " + want + " cents change.")
        else:
            print("There are " + str(forms) + " ways to produce " + want + " cents change.")
        want = str(stdin.readline().strip())

def Comp(want,i):
    global coins
    global sols
    if (want,i) in sols:
        return sols[(want,i)]
    if i < len(coins):
        if want == 0:
            ans = 1
        elif want < 0:
            ans = 0
        else:
            ans = Comp(want-coins[i],i) + Comp(want,i+1)
    else:
        ans = 0
    sols[(want,i)] = ans
    return ans
    
main()
