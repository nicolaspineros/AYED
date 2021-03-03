class node:
    def __init__(self):
        self.p=self
    def find(self):
        while self.p!=self.p.p:
            self.p=self.p.find()
        return self.p
    
n,m=[int(i) for i in input().split()]
while not(n==m==0):
    total=0
    edges=[]
    nodes=[node() for i in range(n)]
    for i in range(m):
        n1,n2,w=[int(i) for i in input().split()]
        edges.append((w,n1,n2))
        total+=w
    edges=sorted(edges)
    for w,n1,n2 in edges:
        if nodes[n1].find()!=nodes[n2].find():
            nodes[n1].p.p=nodes[n2].p.p
            total-=w
    print(total)
    n,m=[int(i) for i in input().split()]
