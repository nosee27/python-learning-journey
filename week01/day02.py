year=int(input())
if year%4==0 and year %100!=0 or year %400==0:
    print("闰年")
else:
    print("不是闰年")
result=0
for i in range(1,101):
    result +=i
print(result)
a=1
count=0
while a<=100:
    count+=a
    a+=1
print(count)

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end="\t")
    print()