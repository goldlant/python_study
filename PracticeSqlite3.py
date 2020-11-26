import sqlite3
con = sqlite3.connect("C:/CookPyton/naverDB") #소스코드가 저장된 폴더에 생성, 연결자명 : con
cur = con.cursor() #커서(cursor) : 데이터베이스에 sql 문 실행하거나 또는 실행된 결과를 돌려받는 통로
cur.execute("CREATE TABLE userTable(id char(4), userName char(15), email char(15), birthYear int)")
cur.execute("INSERT INTO userTable VALUES('john','john Bann','john@naver.com',1990)")
cur.execute("INSERT INTO userTable VALUES('kim','kim Chi','kim@daum.net',1992)")
cur.execute("INSERT INTO userTable VALUES('lee','lee Pal','lee@paran.com',1988)")
cur.execute("INSERT INTO userTable VALUES('park','park Su','park@gmail.com',1980)")
con.commit() #입력한 데이터 저장
con.close() #데이터베이스 닫