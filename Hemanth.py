print(True and True)
print(True and False)
print(False and True or False)


num=2
if num%2==0:
    print('even')
else:
    print('not even')

for i in range(1,101,):
    if i%2==0:
      print(i)
num=100
while num>=1:
   print(num)
num+=1
num=122
tem=num
rev=0
while tem>0:
    rev=rev*10+tem%10
    tem=tem//10
print(rev)

str='apple'
rev=''
for i in str(len(str),-1):
    rev=i+rev
    print(rev)


