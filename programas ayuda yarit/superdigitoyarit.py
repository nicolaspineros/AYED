from sys import stdin
def whil(a):
  suma=0
  while a!=0:
    suma+=a%10
    a=a//10
  return suma
def digito(n):
  if n//10==0:
    return n
  else:
    return digito(whil(n))
def main():
  a,b=stdin.readline().strip().split()
  a,b=int(a),int(b)
  digito(a*b)
main()
