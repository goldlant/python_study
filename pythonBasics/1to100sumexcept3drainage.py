sum, i =0,0

for i in range(1,101):
    if i%3==0:
        continue
    sum+=i

print("1부터 100의 합계(3의배수 제외) : %d" % sum)

