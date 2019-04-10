# Week 1 Python Overview

- KAIST 문일철교수님의 [[데이터 구조 및 분석] 강의](https://www.edwith.org/datastructure-2017f/joinLectures/11178)를 듣고 필기한 노트입니다. 



#### 1주차 강의 구성

> 1-1. Programming and Execution Environment
>
> 1-2. Hello World in Python
>
> 1-3. Naming, Styling and Comments
>
> 1-4. Variable Statements and Operators
>
> 1-5. String
>
> 1-6. List, Tuple, Dictionary
>
> 1-7. Condition and Loop Statement
>
> 1-8. Function Statement
>
> 1-9. Assignment and Equivalence
>
> 1-10. Class and Instance
>
> 1-11. Module and Import



--------------------

### 1-1. Programming and Execution Environment

#### Programming and Data Structure & Algorithms

- 집을 지으려면(프로그래밍을 하려면) 설계도를 그려야 함(UML)

- 설계도를 그리려면 데이터의 구조와 알고리즘을 알고 있어야함
- ***엔지니어로서 구조를 어떻게 잘 설계할 수 있을까?*** 고민해야 함!
- 이 강의에서 쓰는 언어는 Python!



#### Python은?

- interpreter 언어(compiler 언어 아님)
- object-oriented 언어
- Dynamic typing 지원. (보통 compiler 언어는 지원 x)
- industry와 academia에서 모두 많이 쓰이고 있음
- 코드 규칙이 잘 짜여있음!
- 데이터 분석에 특화되어있음!



---------------------------

### 1-2. Hello World in Python

- `print Hello world`를 해보자

  

***Style 1: Procedure-oriented programming***

- 보통은 함수 기반으로 구성.   
- definition part 랑 execution part 로 구성. 

```python
# definition part
def main():
	print("hello world")

# execution part
main()
```



***Style 2: Object-oriented programming***

- object 기반으로 구성. 
- class와 methods 이용
- definition part 랑 execution part 로 구성
- `__init__`: class를 통해 instance가 생성되게 함
- `__del__` : class를 통해 생성된 instance를 지움
- class안에 들어가는 미리 정의된, 특별한 함수들(앞뒤에 `__` 붙음)

```python
# definition part
class HelloWorld:
    def __init__(self): #클래스 안에서 어떤 정보를 가져오라고 할 때 self 이용
        print("Hello World")
    def __del__(self):
        print("Good Bye")
    def performAverage(self, score1, score2):
        average = (score1 + score2) / 2
        print("average score is : ", average)
        
def main():
    world = HelloWorld() # 인스턴스 생성
    score1, score2 = input("Enter two scores :")
    world.performAverage(score1, score2) 
    
  
# execution part
main()
```



--------------------------

### 1-3. Naming, Styling and Comments

- 회사, 연구실마다 규칙은 다르지만 의미 전달을 잘 할 수 있는 일관된 '규칙'을 가지고 작성해야 함

**Naming**

- Class 이름: 클래스의 컨셉을 설명하는 명사 위주로. 첫 글자는 대문자로(낙타 등처럼 단어시작은 대문자로! = *camel casing*)

- Variable 이름 : 저장되는 명사 위주. 소문자로 시작. 
- Method 이름 : method action을 설명하는 동사로. 소문자로 시작. 

**Indentation**

- 4칸 띄기 --> 추천
- tab 쓰기


**Comments**

- `` ''' 따옴표 3개로 코멘트 달기. '''``
- 혹은 # 으로 



--------------------------

### 1-4. Variable Statements and Operators

***Data Types***

- Numeric Data Type : integer, float, long integer, octal integer, ...
- String Data Type 
- Collection Type : tuple, list, set, ...

***Operators*** : +, - , *, /, %, ==, != 

***변수형태 변환(type casting)*** : `int("1")` , `str(100)`

***Swaping statement***: `num1, num2 = num2, num1`



-------------------------------------

### 1-5. String

- 따옴표로 만들어줌. 예: `test_word = "hello world"`

- 개별 문자는 index 를 가지고 있음. indexing 가능

  ```python
  test_world[0]
  >>> "h"
  ```

- 덧셈 = 스트링 연결 
- 곱셈 = 횟수만큼 반복



--------------------------

### 1-6. List, Tuple, Dictionary

####  (1) Index in Sequence

- 시작은 0부터
- 범위는 : 으로. X:Y면 X 부터  Y 직전까지
- `[x:]` x 부터 끝까지
- `[:y]` 처음부터 y직전까지
- `[x:y:z]` x부터 y-1까지 z씩 건너서
  - [1:9:2] --> 1,3,5,7번째를 가져옴
  - range(x,y,z)로도 표현 가능
- `[::z]` 처음부터 끝까지 z씩 건너서

```python
sample =['가', '나', '다', '라', '마']
print(sample[4::-1])
>> 마부터 반대로 끝까지
print(sample[5::-1])
>> 마부터 반대로 끝까지(마지막 인덱스를 초과하면 마지막자리부터 시작)
```

- ` 5부터  반대로 처음까지 1개씩 건너서 -->  순으로 출력/(negative stelist 와 string 모두 이 방식으로 잘라옴



#### (2) List

> *List is another type of sequence variable*

- 대괄호 `['e1', 'e2', 3]` 로 정의
- List + List ==> 리스트 2개 연결
- List*3 ==> 리스트 3개 연결
- 리스트에 포함되어 있는가 ==> `4 in List` 
- `List.append('추가해')` :단어 추가 
- `del list[0]` 첫번째 단어 삭제
- `list.remove(4)` 리스트 안에 4라는 요소 삭제

- `list.reverse()` 리스트를 반대 순서로  바꿔
- `list.sort()` 오름차순으로 정렬!
- 리스트 안에는 여러 데이터 유형이 한번에 들어갈 수 있음



#### (3) Tuple

> *Tuple and list are almost alike*
>
> *Only different in changing values.* 
>
>  Item assignment 불가능

- 리스트와의 차이점 : 튜플은 변수 바꿀 수 없음
- 인댁싱 방법 리스트와 동일
- +, * 사용 방법도 동일



#### (4) Dictionary 

> *Dictionary is also collection variable type*
>
> *But, Not SEQUENTIAL!*
>
> *works by a pair of keys and values.*

```python
dicTest = {1: 'one', 3:'three', 4: 'what?'}
print(dicTest[1])
>> 'one'
dicTest[4] = 'four' # 새로운 요소 집어넣기
dicTest[1] = 'new' # 기존 변수 바꾸기

dicTest.keys() # key를 리스트로
dicTest.values() # values를 리스트로
dicTest.items() # 각각의 key와 values 를 튜플로 묶어 리스트로 출력
```



------------------------------

### 1-7. Condition and Loop Statement

- 컨트롤을 하기 위한 명령어
- Control
  - if
  - for
  - while 등이 있음

#### (1) if

> *Condition statement*

- if, elif, else

- 파이썬은 switch case를 지원하지 않음
- indentation 주의! end를 indentation으로 구분!

#### (2) for

> *Loop statement*

- for loop 의 `continue`와 `else` 사례

```python
for variable in seuqence: 
    print('statements for loop')
    if variable == something:
        continue # 같은 레벨의 for loop으로 다시 올라가라. 
    else:
        print(variable)
    #이 if - else구분에서는 something에 해당하는 variable을 제외한 나머지를 출력
else: # for loop의 else
    print('when for-loop is finished without a break!')
```

- for loop의 `break` 사례

```pytho
for itr in range(5):
    if itr == 3:
    	break # for loop을 끝내버려
```



-------------------------------

### 1-8. Function Statement

- Control 안에 들어가서 돌아갈 내용을 정의해주어야 함
- return은 어떤 형태로든, 몇개든 가능. 단, 순서는 주의하기

```python
def name(params): 
    statement
    return val1, val2

'''
name  : 함수 이름
params : input
val1, val2 : output 순서 중요!
'''
```

- one line function : ***lambda***

```python
lambdaAdd = lambda numParam1, numParam2 : numParam1 + numParam2
# 콜론 앞에 애들을 받아서 콜론 뒤의 애들을 내보내겠다!
numH = lambdaadd(numA, numB)
```



**Sample Program : Finding Prime Numbers**

```python
def isPrimeNumber(numParam1):
    for itr in range(2, numParam1):
        if numParam1 % itr == 0:
            break
        else: 
            return True
        return False
    
def findPrimes(numParam1, numParam2):
    numCount = 1
    for itr in range(numParam1, numParam2):
        if isPrimeNumber(itr) == True:
            print(numCount, "Prime: ", itr)
            numCount = numCount+1
            
findPrime(1,10)
```



--------------------------------

### 1-9. Assignment and Equivalence

- 상수 비교 말고 리스트 비교, 오브젝트 비교 등도 할 수 있음

#### (1) Reference in Nested List

```python
x = [1,2,3]
y = [100, x, 120] # [100, [1,2,3], 120] Nested List
z = [x, 'a', 'b'] # [[1,2,3], 'a', 'b'] Nested List
```

```python
x[1] = 1717  # x = [1, 1717, 3]
# y, z 도 변화할까? YES!
print(y) # [100, [1, 1717, 3], 120]
print(z) # [[1, 1717, 3], 'a', 'b']
```

#### (2) Equvalence : `==`  or `is`

```python 
x[1] = 2 # x = [1,2,3]
x2 = [1,2,3]


# == checks the equvalance of two referenced **values**
if x == x2:
    print("Values are equivalent")
else:
    print("Values are not equivalent")
# >> "Values are equivalent"

# ---------------------
# is checks the equvalenct of two referenced **objects' IDs**
if x is x2:
    print("Values are stored at the same place")
else: 
    print("Values are not Stored at the same place")
# >> "Values are not Stored at the same place"
  
# ---------------------    
# example
if x[1] is y[1][1]:
    print("Values are stored at the sampe place")
else:
    print("Values are not Stored at the same place")
# >> "Values are stored at the sampe place"
```



---------------------------------

### 1-10. Class and Instance

#### (1) Basic Concept of 'class' & 'instance'
- class는 설계도, instances는 설계도를 따라 만들어진 집과 같은 역할을 한다!
- class라는 blcok 안에는 변수, 함수 등이 들어감
- class를 정의 하는 것으로는 행동은 발생하지 않음
- class를 call 해야 행동이 일어남
- 거푸집에서 찍어내듯이 같은 인스턴스를 여러개 찍어낼 수 있음
  - Class가 설계도, Instances 는 찍어낸 집

Class 를 정의해보자 

```python 
class MyHome: 
    
    # variables
	colorRoof = 'red'
	stateDoor = 'closed'
    
    # functions
	def paintRoof(self,color):
		self.colorRoof = color # Red라고 되어있는 것을 바꿀 떄 사용

	def openDoor(self):
		self.stateDoor = 'open'

	def closeDoor(self):
		self.stateDoor = 'close'

	def printStatus(self):
		print("Roof color is", self.colorRoof, \
			", and door is", self.stateDoor)
```



class를 써보자. 

```python
# MyHome이라는 인스턴스를 homeAtSeoul로 받은 것
homeAtSeoul = MyHome() # MyHome의 생성자를 return 해줌
homeAtDaejeon = MyHome()

homeAtDaejeon is homeAtSeoul
# >> False. 서로 다른 곳에 저장된 인스턴스!

# homeAtDaejeon이라는 인스턴스의 openDoor 함수를 불러옴. 
# openDoor함수는 open으로 stateDoor 변수를 바꿔줌
homeAtSeoul.openDoor()
homeAtSeoul.printStatus() 

# homeAtDaejeon이라는 인스턴스의 paintRoof 함수를 불러옴. 
# paintRoof함수는 colorRoof를 blue로 바꿔줌.
homeAtDaejeon.paintRoof('blue') 
homeAtDaejeon.printStatus()
```



#### (2) Important Methods in class: constructor & destructor

- class의 안에 들어가는 함수를 ***member function*** 이라고 함. 그 중에서 `__init__` 과 `__del__` 을 알아보자
- ``__init__``이라고 하는 멤버 펑션을 ***constructor***라고 부름
  - class가 instantiated될 때, 즉, 인스턴스가 만들어질 때 부르자고 약속한 함수!
  - 모든 집을 찍어낼 때 불러진다. 
  - **인스턴스를 만들어낼 때 반드시 받아야 할 파라미터가 있다면 init에서 파라미터로 받으면 된다.** 
  - constructor의 self 는 존재하지 않음. 자기 자신을 뜻함. 
  - class를 콜할 때 넣어진 파라미터를 `__init__`의 파라미터로 받음

```python 
def __init__(self, strAddress):
	print("Built on", strAddress)
	print("Built at", ctime())
```



- 인스턴스를 다 써서, 없애주세요! 할 때 부르는 함수는? ***destructor***을 쓰자
  - `__del__`이라고 하는 멤버 펑션은 "destructor"라고 부름. 
  - instance가 사라질 때 불러짐
  - 사라질 때, "나 이제 파일을 안쓰고 있어요~"라는 문구를 출력해서 정리하는 용으로 쓸 수 있음
  - 많이 쓰진 않지만 안전한 프로그래밍을 위해서 사용하기도 함. 

```python
def __del__(self):
	print("Destroyed at", ctime())

# 이걸 실행할 때 __del__이라는 desturctor 가 불러지는 것. 
del homeAtDaejeon 
```



---------------

### 1-11. Module and Import

#### (1) Module

- 한 파일 안에 Class를 여러개 만들면 복잡해짐. 하나의 파일 안에는 하나의 클래스를 넣기를 추천함
- 그럼 여러개의 클래스를 불러야 할때는 어떻게 쓸까? 
  - 파일을 하나 만들어서 import 파일이름으로 불러옴

모듈 파일의 구성을 살펴보자 

```python
# Home.py  ---------------------------------
"""
# 이런식으로 모듈에 대한 정보를 적어두자 
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

```

이제 모듈을 불러와서 써보자

```python
import Home #이 순간 Home.py의 모든 코드가 실행되는 것. class MyHome이 구동되는 것.
homeAtSuwon = Home.MyHome("Korea, Suwon") 
# Home이라는 모듈 속의 class definition을 불러서 사용!
# >> Built on Korea, Suwon
# >> Buit at 시간

homeAtSuwon.printStatus() 
# >> Roof color is red, and door is closed. 
# 그리고 종료되면서 
# >> Destroyed at 시간 
# 이것이 자동으로 출력되는 것! 
```



#### (2) Organizing Modules by Package

- 파일을 불러서 여러 클래스를 불러올 수 있음 

- 그럼, 파일이 여러개가 되면? 
  - 디렉토리로 path 를 정의하고, "from" 으로 정의하여 그 안에 있는 파일을 불러올 수 있음 

- src >> edu >> lecture >> DSA >> `__init__.py` :
  -  `__init__.py`는 "DSA"라는 디렉토리가 파이썬 패키지라는 것을 의미함!

- src >> edu >> lecture >> DSA >> `Home.py` :
  - DSA 아래에 클래스를 저장한 파이썬 파일
- 모듈이 많이 모여있는 꾸러미, 디렉토리를 ***package***라고 부름!

```python
# from 뒤에 디렉토리를 지정
# import에 불러올 .py 파일명 지정
from package import module

# 예를 들어
from src.edu.lecture.DSA import Home

# 디렉토리 안에 있는 모든 모듈을 가져오고 싶다면? import * 이용
from src.edu.lecture.DSA import * 


# 같은 디렉토리 안에 있는 모듈을 가져올 때는 from을 생략 가능!
import Home

```

-- 끝

