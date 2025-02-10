#for loop
for y in range(0,21):
    print(y)
    print("fgrgrgd")
for i in range(0,100):
    if i%2==0:
        print(i,"even")
    else:
        print(i,'odd')
for x in range(0,20,2):
    print(x)

for w in range(1,20,2):
    print(w)
for d in range(2,5):
    print(d**2)

#nested ioop
for g in range(1,11):
    for b in range(1,21):
        print(g,b)
for g in range(1,11):
    for b in range(1,21):
        print(b)
for n in range(1,8):
    for m in range(1,5):
        print(m,n)
for t in range(2,9):
    if t!=2 and t!=8:
        for y in range(1,5):
            print(y,t)

#while loop
num1=1
while num1<5:
     print('ss')
     num1 += 1
num=15
while num>10:
     print('rr')
num=5
while num<26:
    if num%2==0:
      print(num,'even')
    else:
       print(num,'odd')
    num+=1
num=1
while num<10:
    for i in range(1,11):
        if i!=5 and i!=7:
            print(num,i)
    num += 1
j=1
while j<11:
    i=1
    print(i)
    if j!=5 and j!=7:
      while i<31:
        print(j,i)
        i+=1
    j+=1

