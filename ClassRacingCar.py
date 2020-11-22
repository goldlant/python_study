import time
import threading
#클래스 선
class RacingCar:
    carName=""
    def __init__(self,name):
        self.carName=name
    def runCar(self):
        for _ in range(0,3):
            carStr=self.carName+"~~달립니다~~\n"
            print(carStr,end="")
            time.sleep(0.7)
#메인코드
car1=RacingCar("벤츠")
car2=RacingCar("아우")
car3=RacingCar("bmw")

#쓰레드 생성
th1=threading.Thread(target=car1.runCar())
th2=threading.Thread(target=car2.runCar())
th3=threading.Thread(target=car3.runCar())

th1.start()
th2.start()
th3.start()