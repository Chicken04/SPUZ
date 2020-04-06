#import scipy as scipy #Should pip install scipy files
import random
q = int(input("Enter vector size: "))
r = int(input("Enter number of sims: "))
l=[]
for i in range (0,r+1):
  n=0
  null = False
  a=[]
  for i in range(0,q):
    a.append(random.randint(0, 10))
  f=0 
  while null != True:
    m=0
    for j in range (0,len(a)):
      a[j]=random.randint(0, 10)*a[j]
    for k in range (0,len(a)):
      if a[k]==0:
        m+=1
    if m==10:
      null = True
    f+=1
  l.append(f)
print(l)
print(min(l))
print(max(l))

with open("data.txt", "w") as output_file:
  for i in range(0,len(l)):
    output_file.write(str(l[i]) + "\n")