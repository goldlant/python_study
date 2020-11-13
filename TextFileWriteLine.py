outFp=None
outstr=""

outFp=open("C:/Temp/data2.txt","w")

while True:
    outstr=input("내용을 입력하세요")

    if outstr!="":
        outFp.writelines(outstr+"\n")

    else:
        break

outFp.close()
print("---정상적으로 파일에 씀---")
