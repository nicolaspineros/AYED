from sys import stdin

x_pos = [-1,0,0,1,-1,1,-1,1]
y_pos = [0,-1,1,0,1,1,-1,-1]

def DFS(i, j):
    global mat, aux
    s = []
    s.append((i,j))
    n = len(mat)
    while(len(s)!=0):
        node = s.pop()
        for x in range(0, len(x_pos)):
            temp_x = node[0]+x_pos[x]
            temp_y = node[1]+y_pos[x]
            if temp_x<n and temp_x>=0 and temp_y<len(mat[0]) and temp_y>=0 and mat[temp_x][temp_y]=='1' and aux[temp_x][temp_y]==False:
                s.append((temp_x,temp_y))
            aux[node[0]][node[1]] = True

def main():
    image = 0
    while(True):
        n = stdin.readline().strip()
        if n == '':
            break
        n = int(n)
        image = image + 1
        global mat, aux
        mat = []
        aux = []
        for i in range(0,n):
            data = stdin.readline().strip()
            mat.append([s for s in data])
            aux.append([False for s in data])
        cont = 0
        for i in range(0,n):
            for j in range(0, len(mat[0])):
                if aux[i][j]==False and mat[i][j]=='1':
                    cont = cont + 1
                    DFS(i, j)
        print('Image number ' + str(image) + ' contains ' + str(cont) + ' war eagles.')

main()
