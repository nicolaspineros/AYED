from sys import stdin

coins = [1,5,10,25,50]

def main():
   global coins,memo
   #Memorizacion
   memo = [[None] * (30001) for x in range(6)]
   #Base cases
   for c in range(30001):
      memo[5][c]=0  #Case 1
   for m in range(5):
      memo[m][0]=1  #Case 2
   for m in range(4,-1,-1):
      for c in range(1,30001):
         if(c-coins[m] < 0): #Case 3
            memo[m][c] = memo[m+1][c]
         else:
            memo[m][c] = memo[m+1][c]+memo[m][c-coins[m]]
   while True:
      n = stdin.readline().strip()
      if not n:
         break
      n = int(n)
      if n<=4:
         #El cambio
         print('There is only',memo[0][n],'way to produce', n, 'cents change.')
      else:
         #El cambio
         print('There are',memo[0][n],'ways to produce',n,'cents change.')
main()
