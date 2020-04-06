import random

q = int(input("Enter vector size: "))
r = int(input("Enter lower interation : "))
s = int(input("Enter upper interation : "))
l = []
filenames = []
for u in range (r,s+1):
  filenames.append(str(u)+".txt")
print(filenames)

def spuz(lower, upper, size):

  for i in range (0, upper):  # Start of For Loop
    print(i)
    n = 0
    null = False
    a = []

    for i in range(0, size):  # Start of For Loop
      a.append(random.randint(0, 10))
      # End of For Loop

    f = 0

    while null != True:  # Start of While Loop

      m = 0

      for j in range (0, len(a)):  # Start of For Loop
        a[j] = random.randint(0, 10) * a[j]
      # End of For Loop

      for k in range (0, len(a)):  # Start of For Loop
        if a[k] == 0:  # Start of If Loop
          m = m + 1
          # End of If Loop

      if m == 10:  # Start of If Loop
        null = True
      # End of If Loop

      f = f + 1
      # End of While Loop

    l.append(f)
    # End of For Loop
  return(l)


for filename in filenames:
    with open(filename, "w") as output_file:
      o = int(filename.replace(".txt",""))
      result = spuz(r, s, q)
      for i in range(0,len(result)):
        output_file.write(str(result[i]) + "\n")