import sqlite3

con, cur =None,None
data1, data2, data3, data4 ="","","",""
sql=""

con = sqlite3.connect("C:/CookPyton/naverDB") #연결자
cur = con.cursor() #커서

cur.execute("SELECT * FROM userTable")

print("사용자 ID   사용자 이름    이메일    출생년")
print("-----------------------------------")

while(True):
    row = cur.fetchone() #한줄씩 처리
    if row == None:
        break
    data1=row[0]
    data2=row[1]
    data3=row[2]
    data4=row[3]
    print("%5s   %15s    %15s   %d"%(data1,data2,data3,data4))

con.commit()
con.close()
