# Module and Import

# 1. Module
# - 한 파일 안에 Class를 여러개 만들면 복잡해짐. 하나의 파일 안에는 하나의 클래스를 넣기를 추천함
# - 그럼 여러개의 클래스를 불러야 할때는 어떻게 쓸까? 
# 		- 파일을 하나 만들어서 import 파일이름으로 불러옴
# Home.py  ---------------------------------
"""
Created on 2019.08.01.
@author : Nuree Chung
"""
from time import ctime 

class MyHome:

	# Member variables. class의 상태 저장
	colorRoof = 'red'
	stateDoor = 'closed'

	# Member functions
	def paintRoof(self, color):
		self.colorRoof = color
	def openDoor(slef):
		self.stateDoor = 'open'
	def closeDoor(self):
		self.stateDoor = 'close'
	def printStatus(self):
		print("Roof color is", self.colorRoof \
			", and door is", self.stateDoor)

	# Constructor
	def __init__(self, strAddress):
		print("Built on", strAddress)
		print("Built at", ctime())

	# Destructor
	def __del__(self):
		print("Destroy at", ctime())



# UsingHome.py ---------------------------------
import Home #이 순간 Home.py의 모든 코드가 실행되는 것. class MyHome이 구동되는 것.
homeAtSuwon = Home.MyHome("Korea, Suwon") # Home이라는 모듈 속의 class definition을 불러서 사용!
# >> Built on Korea, Suwon
# >> Buit at 시간

homeAtSuwon.printStatus() 
# >> Roof color is red, and door is closed. 
# 그리고 종료되면서 
# >> Destroyed at 시간 
# 이것이 자동으로 출력되는 것! 



# 2. Organizing Modules by Package
# - 파일을 불러서 여러 클래스를 불러올 수 있음 
# - 그럼, 파일이 여러개가 되면? 
# 		- 디렉토리로 path 를 정의하고, "from" 으로 정의하여 그 안에 있는 파일을 불러올 수 있음 
# 
src >> edu >> lecture >> DSA >> __init__.py # __init__.py는 "DSA"라는 디렉토리가 파이썬 패키지라는 것을 의미함!
src >> edu >> lecture >> DSA >> Home.py # DSA 아래에 클래스를 저장한 파이썬 파일

from src.edu.lecture.DSA import Home
from package import module
# from 뒤에 디렉토리를 지정
# import에 불러올 .py 파일명 지정


import Home 
# from 은 언제 생략 가능? 
# 같은 디렉토리에 있는 것을 가져올 때는 생략 가능. 




# 3. Sample Program : Interaction with Your Program
class CasherLine:
	lstLine = [] # list 형태의 변수
	def addCustomer(self, strName):
		self.lstLine.append(strName)
	def processCustomer(self):
		strReturnName = self.lstLine[0]
		self.lstLine.remove(strReturnName)
		return strReturnName
	def printStatus(self):
		strReturn = ""
		for itr in range(len(self.lstLine)):
			strReturn += self.lstLine[itr] + " "
		return strReturn


binLoop = True  # Binary Loop
line = CasherLine() # CahserLine의 constructor를 콜함. 하나의 인스턴스를 만듦. 
while binLoop:
	strName = raw_input("Enter Customer Name : ") # input을 받아서 strName에 저장해라 
	if strName == '.':
		break
	elif strName == "->":
		print("Processed: ", line.processCustomer())
		print("Line: ", line.printStatus())
	else:
		line.addCustomer(strName)
		print("Line:", line.printStatus())

print("Number of remaining customers : ", len(line.lstLine))
