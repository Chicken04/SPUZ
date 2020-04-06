import random

q = int(input("Enter vector size: "))
r = int(input("Enter number of sims: "))
l = []

for i in range (0, r + 1):  # Start of For Loop

  n = 0
  null = False
  a = []

  for i in range(0, q):  # Start of For Loop
    a.append(random.randint(0, 10))
    # End of For Loop

  f = 0

  while null != True:  # Start of While Loop

    m=0

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

print(l)
print(min(l))
print(max(l))

with open("data.txt", "w") as output_file:
  for i in range(0,len(l)):
    output_file.write(str(l[i]) + "\n")