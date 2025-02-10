num1=[]
for i in range(0,11,2):
    if i%2==0:
        num1.append(i)
print(num1)

even=0
odd=0 
input=[1,2,3,4,5]
for i in input:
    if i%2==0:
      even=even+i
    else:
       odd=odd+i
print(even)
print(odd)


input=["abcd","efghi","ghifh","dskf","sdddfsdf"]
result="".join(i[0] for i in input)
print(result)


num='Python'
print(num[::-1])



