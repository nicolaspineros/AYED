from sys import stdin
import math
def valid(wi,W):
    return wi <= W
def maxUtObjects(N,ni,Sp, wi, zi,elements, W):
   if ni < N:
       maxzi = -math.inf
       for e in range(len(elements)) :
           remElements = elements[:]
           element = remElements.pop(e)
           remElements
           modifiedSP = Sp[:]
           modifiedSP.append(element)
           if valid(wi + element[0],W) :
               if ni < N-1:
                   maxzi = max(maxzi, zi + element[1], maxUtObjects(N, ni+1, modifiedSP[:], wi + element[0], zi + element[1], remElements[:], W))
               else:
                   maxzi = max(maxzi, zi + element[1])          
       return maxzi
def main():
    W,N = [int(x) for x in stdin.readline().split()]
    while not (W==0 and N == 0):
        elements = []
        for i in range(N):
            w,z = [int(x) for x in stdin.readline().split()]
            elements.append((w,z))
        print(maxUtObjects( N, 0, [], 0, 0, elements[:], W ))
        W, N = [int(x) for x in stdin.readline().split()]

main()
