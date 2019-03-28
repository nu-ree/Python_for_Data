# Week 1 Python Overview

- KAIST 문일철교수님의 [데이터 구조 및 분석] 강의를 듣고 필기한 노트입니다. 

--------------------

### 1-1. Programming and Execution Environment

#### Programming and Data Structure & Algorithms

- 집을 지으려면(프로그래밍을 하려면) 설계도를 그려야 함(UML)

- 설계도를 그리려면 데이터의 구조와 알고리즘을 알고 있어야함
- ***엔지니어로서구조를 어떻게 잘 설계할 수 있을까?*** 고민해야 함!
- 이 강의에서 쓰는 언어는 Python!



#### Python은?

- interpreter 언어(compiler 언어 아님)
- object-oriented 언어
- Dynamic typing 지원. (보통 compiler 언어는 지원 x)
- industry와 academia에서 모두 많이 쓰이고 있음
- 코드 규칙이 잘 짜여있음!
- 분석에 특화되어있음!



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



### 1-3. Naming, Styling and Comments

- 회사, 연구실마다 규칙은 다르지만 의미 전달을 잘 할 수 있는 일관된 '규칙'을 가지고 작성해야 함



**Naming**

- Class 이름: 클래스의 컨셉을 설명하는 명사 위주로. 첫 글자는 대문자로(낙타 등처럼 단어시작은 대문자로! = *camel casing*)

- Variable 이름 : 저장되는 명사 위주. 소문자로 시작. 
- Method 이름 : method action을 설명하는 동사로. 소문자로 시작. 



**Indentation**

- 4칸 띄기
- tab 쓰기


**Comments**

- `` ''' 따옴표 3개로 코멘트 달기. '''``
- 혹은 # 으로 



### 1-4. Variable Statements and Operators

