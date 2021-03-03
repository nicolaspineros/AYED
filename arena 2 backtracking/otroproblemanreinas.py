from sys import stdin
global lis
# Determine if the K-solution is viable
def validBoard(sParcial, phase,m):
    isValid = True
    for x in range(0, phase):
        if sParcial[x] == sParcial[phase] or abs(sParcial[x] - sParcial[phase]) == abs(x - phase):
            isValid = False
            break
    return isValid

#Use backtracking to iterate over all posible solutions
def bactrackNQueens(sParcial, phase, N,m,matriz):
    if phase < N:
        global c
        #print('=============== ETAPA %d %s =============' % (phase, str(sParcial)))
        for x in range(N):
            sParcial[phase] = x
            #print(sParcial)
            if validBoard(sParcial[:], phase,m)  and (x,phase) not in matriz:
                if phase < N-1:
                    bactrackNQueens(sParcial[:], phase + 1, N,m,matriz)
                    #print('=============== BACTRACK %s ============' % (str(sParcial)))
                else:
                    #print('=============== SOLUCION ===============')
                    c+=1
                    #print(sParcial)

                    #print('========================================')


# Initialize phase Zero in order to solve n-queens using backtracking
def solveNQueens(N,m,matriz):
    global c
    sParcial, phase = [int(-1) for x in range(0, N)], 0
    bactrackNQueens(sParcial[:], phase, N,m,matriz)


# Given an N size chess-board program solve n-queens problems using backtracking technique
def main():
    global c
    '''line = stdin.readline()
    while line != '':'''
    N =int( stdin.readline())
    e=1
    while N != 0:
        m=[]
        c=0
        
        for i in range(N):
            a=stdin.readline().strip()
            tab=[]
            for j in range(len(a)):
                tab.append(a[j])
            m.append(tab)
        matriz=[]
        for x in range(len(m)):
            for y in range(len(m)):
                if m[x][y]=="*":
                    matriz.append((x,y))
        solveNQueens(N,m,matriz)
        print('case '+str(e)+':',c)
        
        N =int(stdin.readline().strip())
        e+=1
       # line = stdin.readline()


main()
