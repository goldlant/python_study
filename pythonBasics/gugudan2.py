##전역 변수 선억 부분##
i,k,guguline=0,0,""

##메인 코드 부분##
for i in range(2,10):
    guguline=guguline+("#  %d  # " %i)

print(guguline)


for i in range(1,10):
    guguline=""
    for j in range(2,10):
        guguline = guguline + str("%2d*%2d=%2d"%(j,i,j*i))
    print(guguline)


"""
for i in range(1,10):
    for j in range(2,10):
        print("%d * %d = %2d" % (j,i,j*i),end=" ")
    print("\n")
"""
