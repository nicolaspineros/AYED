from sys import stdin
from collections import deque

def BFS(s, t, edges):
    global words, dic
    visited = [False for x in range(len(words))]
    distance = [float('inf') for x in range(len(words))]
    cont = 0
    u = dic[s]
    distance[u] = 0
    q = deque()
    q.append(u)
    while q:
        u = q.popleft()
        if words[u] == t:
            print('%s %s %d' % (s, t, distance[u]))
            break
        else:
            if not visited[u]:
                visited[u] = True
                for v in edges[u]:
                    if distance[v] > distance[u] + 1:
                        distance[v] = distance[u] + 1
                        q.append(v)


def build_graph():
    global words
    edges = [[] for x in range(0, len(words))]
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            # Check if the words are one character away
            mismatch = 0
            if len(words[i]) == len(words[j]):
                for k in range(0, len(words[i])):
                    if words[i][k] != words[j][k]:
                        mismatch = mismatch + 1
                    if mismatch > 1:
                        break
            if mismatch == 1:
                edges[i].append(j)
                edges[j].append(i)
    return edges
    

def main():
    cases = int(stdin.readline())
    stdin.readline()
    for c in range(cases):
        global words, dic
        words = []
        dic = {}
        cont = 0
        while True:
            line = stdin.readline().strip()
            if line == '*':
                break
            words.append(line)
            dic[line] = cont
            cont = cont + 1
        # Build Graph
        edges = build_graph()
        if c != 0:
            print('')
        while True:
            line = stdin.readline().strip()
            if line == '':
                break
            visited = [False for x in range(len(words))]
            s1, s2 = line.split()
            BFS(s1, s2, edges)

main()
