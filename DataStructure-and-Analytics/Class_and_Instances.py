# Class and Instance

## 1. Basic Concept of 'class' & 'instance'
# - class는 설계도, instances는 설계도를 따라 만들어진 집과 같은 역할을 한다!
# - class라는 blcok 안에는 변수, 함수 등이 들어감
# - class를 정의 하는 것으로는 행동은 발생하지 않음
# - class를 call 해야 행동이 일어남

class MyHome: 
	colorRoof = 'red'
	stateDoor = 'closed'

	def paintRoof(self,color):
		self.colorRoof = color # Red라고 되어있는 것을 바꿀 떄 사용

	def openDoor(self):
		self.stateDoor = 'open'

	def closeDoor(self):
		self.stateDoor = 'close'

	def printStatus(self):
		print("Roof color is", self.colorRoof, \
			", and door is", self.stateDoor)


#MyHome이라는 인스턴스를 homeAtSeoul로 받은 것. 거푸집에서 찍어내듯이 같은 인스턴스를 여러개 찍어낼 수 있음
homeAtSeoul = MyHome()
homeAtDaejeon = MyHome()

 #homeAtDaejeon이라는 인스턴스의 openDoor 함수를 불러옴. open으로 stateDoor 변수를 바꿔줌
homeAtSeoul.openDoor()
homeAtSeoul.printStatus() 

#homeAtDaejeon이라는 인스턴스의 paintRoof 함수를 불러옴. colorRoof를 blue로 바꿔줌.
homeAtDaejeon.paintRoof('blue') 
homeAtDaejeon.printStatus()


## 2. Important Methods in class: constructor & destructor
# - class의 안에 들어가는 함수를 member function 이라고 함 
# - "__init__"이라고 하는 멤버 펑션을 "constructor"라고 부름. instantiated될 때, 즉, 인스턴스가 만들어질 때 불러짐. 
# 	- 모든 집을 찍어낼 때 불러진다. 
# 	- 인스턴스를 만들어낼 때 반드시 받아야 할 파라미터가 있다면 init에서 파라미터로 받으면 된다. 
# 	- constructor의 self 는 존재하지 않음. 자기 자신을 뜻함. 
# 	- class를 콜할 때 넣어진 파라미터를 __init__의 파라미터로 받음

def __init__(self, strAddress):
	print("Built on", strAddress)
	print("Built at", ctime())

# - "__del__"이라고 하는 멤버 펑션은 "destructor"라고 부름. instance가 사라질 때 불러짐.
# 	- "내가 사라질 때 파일을 저장해주세요"라는 의미로도 사용할 수 있음. 
# 	- 고수들이 사용...? 

def __del__(self):
	print("Destroyed at", ctime())
del homeAtDaejeon # 이걸 실행할 때 __del__이라는 desturctor 가 불러지는 것. 


