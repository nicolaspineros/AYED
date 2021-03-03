from collections import deque
from heapq import *
import sys
n=sys.stdin.readline().strip()
while n!="":
    l=deque()
    tail=deque()
    heap=[]
    x=""
    y=""
    s=""
    r=""
    for i in range(int(n)):
        a,b=[int(i) for i in input().split()]
        if a==1:
            l.append(b)
            tail.append(b)
            heappush(heap,-1*b)
            print("l:",l)
            print("tail:",tail)
            print("heap:",heap)
        else:
            x+=str(tail.popleft())
            y+=str(-1*heappop(heap))
            s+=str(l.pop())
            r+=str(b)
            print(x)
            print(y)
            print(s)
            print(r)
    if r==s and s!=x and s!=y:
        print("stack")
    elif r==x and s!=x and x!=y:
        print("queue")
    elif r!=x and r!=s and r!=y:
        print("impossible")
    elif r==y and s!=y and x!=y:
        print("priority queue")
    else:
        print("not sure")
    n=sys.stdin.readline().strip()
