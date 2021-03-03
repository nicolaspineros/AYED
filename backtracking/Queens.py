from sys import stdin
# Determine if the K-solution is viable
def validBoard(sParcial, phase):
    isValid = True
    for x in range(0, phase):
        if sParcial[x] == sParcial[phase] or abs(sParcial[x] - sParcial[phase]) == abs(x - phase):
            isValid = False
            break
    return isValid
#Use backtracking to iterate over all posible solutions
def bactrackNQueens(sParcial, phase, N):
    if phase < N:
        print('=============== ETAPA %d %s =============' % (phase, str(sParcial)))
        for x in range(N):
            sParcial[phase] = x
            print(sParcial)
            if validBoard(sParcial[:], phase):
                if phase < N-1:
                    bactrackNQueens(sParcial[:], phase + 1, N)
                    print('=============== BACTRACK %s ============' % (str(sParcial)))
                else:
                    print('=============== SOLUCION ===============')
                    print(sParcial)
                    print('========================================')


# Initialize phase Zero in order to solve n-queens using backtracking
def solveNQueens(N):
    sParcial, phase = [int(-1) for x in range(0, N)], 0
    bactrackNQueens(sParcial[:], phase, N)


# Given an N size chess-board program solve n-queens problems using backtracking technique
def m

def revisar(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[0][0]=='*':
                noreina=lista[i][j]
                print(noreina)
def crear(line):
    sParcial, phase = [int(-1) for x in range(0, line)], 0
    return(sParcial)
def main():
    line = int(stdin.readline().strip())
    while line != '':
        lista=[]
        for i in range(line):
            a=[stdin.readline().strip()]
            lista.append(a)
            print(solveNQueens(line))
            revisar(lista)
        break
  
    
        

main()
