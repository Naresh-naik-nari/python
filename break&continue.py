#jump statements - bresk continue and pass

#break and continue-use in loop
for i in range(0,21):
    if i%2==0:
     print(i)
    if i==20:
       break
for j in range(1,21):
   if j==4 or j==5:
      break
   print(j)
for d in range(2,23):
   break

#continue
for s in range(1,10):
   print(s)
   if s==5:
      continue
   print('biox')

for u in range(1,10):
   continue
for n in range(1.10):
   print(n)
   if n==5:
      continue
   print('s')

#break and continue in nested loop

for j in range(1,10):
   for m in range(1,23):
      if j==5:
         break
      print(j,m)

for cls1 in range(1,20):
   for roll in range(1,20):
      if cls1==5 and roll>10:
         continue
      print(cls1,roll)  

for m in range(0,10):
   for n in range(1,10):
      if m==5:
         break
      print(m,n)

#pasa-->no statement written
#terinary operater
num1=5
num2=10
if num2%10==0:
   num1=10
else:
   num1=8
time=13
