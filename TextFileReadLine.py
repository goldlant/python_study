inFp = None
inStr, inList = "",[]

inFp=open("C:/Temp/data1.txt","r")



#파일의 내용을 한 행씩 출력
inList=inFp.readlines()
for inStr in inList:
    print(inStr,end="")


#readlines(파일의 내용을 통째로 읽어서 리스트에 저장)
inList=inFp.readlines()
print(inList)



#readline(한줄씩 읽어옴)
while(True):
    inStr=inFp.readline()
    if inStr == "":
        break;
    print(inStr,end="")

#readline 
inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")




inFp.close()
