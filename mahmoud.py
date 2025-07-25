def signe(a,b):
    if(a*b>0):
     print(a,"et",b,"sont le meme signe")
    else:
     print(a,"et",b,"sont pas le meme signe")

a=int(input("entrer a :"))
b=int(input("netrer b :"))
signe(a,b)
def min(a,b):
  if (a-b>0):
    min=b
  else:
    min=a
  return min
print("le minimum est :",min(a,b))
def max(a,b):
  if(a-b<0):
    max=b
  else:
    max=a
  return max
print("le maximumu est : ",max(a,b))