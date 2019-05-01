# Week 2 Object-oriented paradigm and software design

이번주차 학습 목표

- 남이 그려놓은 설계도를 읽을 줄은 알아야 한다! 
- 좋은 설계도를 알아보는 안목을 길러야 한다!

**강의 목차**

- [**Design and Programming**](https://www.edwith.org/datastructure-2018F/lecture/31067/)
- [**UML notation 1**](https://www.edwith.org/datastructure-2018F/lecture/31068/)
- [**Encapsulation and Inheritance**](https://www.edwith.org/datastructure-2018F/lecture/31069/)
- [**Polymorphism and Abstract Class**](https://www.edwith.org/datastructure-2018F/lecture/31070/)
- [**UML notation 2**](https://www.edwith.org/datastructure-2018F/lecture/31072/)
- [**Structure and Relationship**](https://www.edwith.org/datastructure-2018F/lecture/31071/)



## 2-1. Design and Programming

- 설계(design)를 기반으로 개발을 하게 된다
- 설계는 조금 바꿔서 다시 사용할 수도 있고.

### (1) 소프트웨어 설계에서 중요한 것은? 

- Correctness : 클라이언트의 목표에 부합해야 한다. 
- Robustness : 쉽게 고장나면 안된다. 예상되는 사용자의 습관에 대해 잘 대응해야 한다. 
- Flexibility : 업데이트 및 확장이 잘 되어야 한다
- Usability & Reusability : 다른 환경이나 목적에서도 쉽게 사용할 수 있게 디자인해야 한다. 
- Efficiency : 작게 만들고, 쉽게 만들고, 빠르게 execute 해야 한다. 



### (2) Object-Oriented Design

- 디자인 컨셉 중, 객체 지향 디자인을 알아보자. 

- 현실을 추상화 하여서 소프트웨어에 반영해야 한다. 

  예를 들어, 은행에 '고객'이 돈을 넣었다가 빼고('입출금'), '계좌'를 가지고 있음. 고객, 입출금, 계좌 등과 같은 real world concept을 모두 추상화할 수 있음. 추상화한 entity는 이름, 특성, 행동 등을 가짐. 

  - 개념 이름 : 고객 / 거래 
  - 개념 특성 : 고객특성(고객 ID, 계좌번호) / 거래 특성 (거래 지점IT, 거래금액)
  - 개념 행동 : 고객의 행동(otp를 입력하라) / 거래 행동(돈을 줘라)

- ***추상화***란 무엇인가? 목적에 맞게끔 관심 대상을 간략화한 것.

- Class와 Instance는 무엇인가? 

  - 모든 인스턴스는 그래스에 있는 여러 행동을 동일하게 수행할 수 있음

  > Class : Result of Design and Implementation / conceptualization  / corresponds to design abstractions
  >
  > Instance : Result of execution / Realization / Corresponds to real world entities



## 2-2. UML notation 1

### (1) Software Design as House Floorplan

- 소프트웨어를 설계하고 개발하려면 설계도를 읽을 줄 알아야 함
- 소프트웨어를 설계하는 표준을 배워야 함
  - OMG그룹에서 만든 **Unified Modeling Language(UML)**을 배워보자
- 다양한 UML이 존재하지만 Class를 활용하는 UML을 알아보자

### (2)  UML notation : Calss and Instance

- 클래스를 다루는 설계도는 이렇게 설계한다. 
- 기본적인 클래스의 얼계를 짜놓은 형태. 
- Class & Instance의 종류:
  - Abstract class: e.g.`Person`
  - Class: e.g. `Customer` 
  - Named instance: e.g. `Park::Customer`
  - Unnamed instance: e.g. `Customer`
- 하나의 클래스는 attribute(=member variable, property)과 member functions(=methods) 으로 구성
- Instance name:
  - `(InstanceName)`::`(ClassName)`
  - e.g. `Park::Customer` <이렇게 쓰면 이게Named Instance가 되는 것
- Visibility options : 
  - `+` : public
  - `#` : protected
  - `-`: private **현실에서 선호되는 방식**. *"내 클래스는 내가 책임질게. 다른 데이터들은 method를 이용해서 접근해 "* 안전하게 데이터를 관리하는 방식. 
-  Member variables
  - `+`,`#`, `-` `(name)`:`(type)`=`(default value)`
  - e.g. `-ID:String` , `#AccountNum:Integer`, `+Name:String=Hey`(= 'Hey'를 디폴트 값으로 넣어두고 나중에 method를 통해서 바꿔줄 수 있다는 의미)
- Member methods:
  - `+`,`#`, `-` `(name)` `(arguments)`:`(type)`
  - e.g. `+login():void`, `+requestWithdrawal(arg):Boolean`



### 2-3. Encapsulation and Inheritance

#### (1) Encapsulation

> Encapsulation이란? *클래스 내부에 모든 내용이 싸여있고, 외부에선 methods로 접근하게 한다는 개념이다*

- Object는 Data와 Behavior로 구성되어 있음
  - *Behavior라는 function을 통해서만 데이터에 접근해야 해! 데이터 변형은 내 behavior로만 하겠어. 캡슐로 만들어서 그 안에 있는 건 내가 다 컨트롤 할거야.*
- visibility option을 통해서 통제함 
  - `private - protected - public`
  - Method는 public으로. data는 private로 해서 method를 이용해서 관리
- **파이썬은 vitibility option을 제공하지 않음!!!** (그렇군..!!) 즉, 파이썬에서 모든 attribute는 외부에서 accessible함. 하지만, 몇 가지 약속이 있음. `__var1`이렇게 쓰는건, 외부에서 접근하지 않았으면 좋겠다는 표현! 파이썬에선 이런 변수나 함수명의 표현으로 visibility option의 의미를 전달함. 반면 C나 자바에서는 `private - protected - public` 등을 통해 visibility를 조정할 수 있음. 

#### (2) Inheritance

- 유전, 유산? 클래스끼리 무슨 유산? 

> Inheritance란? 클래스가 가진 attributes(=member variables & methods)를 descendants에게 물려주자

- descendants는 새로운 attributes를 가질 수도 있고 기존에 물려받은 attribute를 변형해서 가질 수 있음. 그런 경우가 아니라면 물려준 특징을 그대로 가짐

- Superclass  :  

  - 조상님! 상위에 계심. 새로운 것은 없음. 좀 더 general 한 클래스.
  - *Generalized view*

- Subclass : 

  - 자손 클래스
  - Specialized from the conceptual view

- 그럼 여러 클래스에서 inheritance를 받을 수 있음?? (=Multiple Inheritance)

  - Java : 여러 클래스에서 받을 수 었음. 하나에서만 가능
  - C++이나 Python: 여러 클래스에서 받을 수 있음. 

  ```python
  Person
  +NatRegionNum
  +loin()
  
  
  Customer
  +ID
  +A
  ```



#### (3) Inheritance in Python

- 언어마다 inheritance라는 개념이 있음. 파이썬에선 어떻게 할까? 

```python
class Father(object): 
    # superclass에서 상속받을 다른 superclass가 없을 때 'object'를 인자로 받음
    strHometown = 'Jeju'
    # __init__은 따로 method로 불러오지 않아도 
    # 이 class로 instance를 만들어 낼 때 실행된다(Constructor! 1주차에서 배움)
    def __init__(self):
        print('Father is created')
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")
        
        
class Mother(object): 
    strHometown = 'Seoul'
    def __init__(self):
        print('Father is created')
    def doMotherThing(self):
        print("Father's action")
        
class Child(Father, Mother):
    strName = 'Moon'
    def __init__(self):
        super(Child, self).__init__()
        # Child라는 class를 call할 때 나의 superclass를 call함
        # 즉, Father의 constructor를 실행)
        print("Child is Created")
    def doRunning(self):
        # superclass인 Father 에도 doRunning이 있지만, subclass의 method가 우선
        print("Fast")
        
        
 me = Child ()
# >> Father is created
# >> Child is created

me.doFatherThing()
# >> Father's action

me.doMotherThing()
# >> Mother's action

me.doRunning()
# >> Fast

print(me.strHometown)
# >> Jeju
# 상속받은 두 superclass 중 먼저 상속받은 클래스(=Father)의 값이 나옴

print(me.strName)
# >> Moon
```



#### (4) *self* and *super*

- *self*

  > *reference variable pointing the instance itself*

  - 인스턴스 자기 자신을 가리킴

- *super* 

  > *reference variable pointing the base class instance*

  ```python
  class Child(Father, Mother):
      strName = 'Moon'
      def __init__(self, paramName, paramHome):
          super(Child, self).__init__(paramHome)
          self.strName = paramName
              
  ```

  위 코드에서 `super(Child, self)`는 `Child`가 상속받는 두 클래스 중, 먼저 받은 `Father` 클래스를 찾가가게 되고, `.__init__`은 거기서 constructor를 찾아옴

```python
me = Child('Nuree', 'Suwon') # __init__의 파라미터로 'Nuree'와 'Suwon'이 들어가게 된다
# me라는 인스턴스를 생성함과 동시에 __init__은 실행이 된다.
# 이에 paramHome은 Child의 super class 중 첫번째 super class였던 Father의 __init__을 실행하게 되는데, 이때 파라미터로 paramHome 자리에 넣은 'Suwon'을 받아가서 strHometown에 집어넣게 된다. 
print(me.strHometown)
# >> "Suwon"
print(me.strName)
# >> "Nuree"
```







### 2-4. Polymorphism and Abstract Class

#### (1) Polymorphism

- Poly = Many, Morph = Shape. 다양한 모양?!???

- 같은 모양을 가지지만, 완전히 다르게 행동할 때, '폴리모피즘'이 적용되었다고 한다. ?!

- 메소드 이름 & 파라미터 리스트를 **'Sinature'**(메소드가 어떤 메소드인지 알아낼 수 있고, 구분할 수 있게 해주는)가 된다!

- **Polymorphism** 아래에는 'Method Overriding'과 'Method Overloading'이라는 하위 개념이 있음 

  **Method Overriding**

  - Base class(parent class)에 있는 Method이름과 동일한 이름의 method가 child class에 있으면, child 클래스에 있는 것이 엎어쳐져서 콜된다. 즉, method signature가 겹치는 경우 이전(parent)의 method는 무시하고 child class에서 새롭게 정의된 method를 불러온다.

  **Method Overloading**

  - class가 다양한 method를 가질 수 있는데, method이름은 동일하지만 파라미터가 달라서 다양한 형태로 실행 가능하다. 한 메소드가 다양하게 operating 된다는 뜻. 



```python 
class Building : 
    strAddress = 'Daejeon'
    def openDoor(self):
        print("Door Opened")
        
class Hotel:
    def openDoor(self):
        print("Bellboy opens 4 doors")
    def checkIn(self):
        print("Someone checks in for 1 day")
    def checkIn(self, days): # << Overloading 되는 경우 
        print("Someone checks in for ",days, "days" )
        
lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkin()
lotteHotel.checkin(2)


class Hotel(Building):
    def openDoor():# << Overriding 되는 경우(Base Class "Building"에 엎어치기)
        print("OVERRIDING!!")
    def checkIn(self, days = 1): # << default 값 이용해서 method를 overloading 해줌!!
        print("Someone checks in for ",days, "days" )
    

```



#### (2) Abstract Class

> *Abstract Class란? abstract method를 가지는 class*

- abstract method 란? 

  - signature 파트(= 메소드 이름 & 파라미터)는 잘 정의되어 있고 실행하는 것(=implementation)은 없는 메소드. 그래서 instance를 만들 수는 없음..!!
  - ***그럼 동작을 안할텐데? 왜 필요할까?***
  - 여럿이 작업을 할 때, 큰 틀의 얼개를 공통적으로 짤 때 쓸 수 있음! 

  - 체계적으로 class의 구조를 디자인하고 구현을 할 때 활용

  > 예를 들어, '창문'이라는 클래스를 만들 때 어떤 모양의 '창문'클래스를 만들건, xxx라는 method와 yyy라는 method는 넣어서 만들어. 라는 얼개를 짜주는 것. (=*half-made!*)

  - 먼저 abstract class를 만들고, 이를 base class(parent)로 받아 자식 class에 full로구현. 이 자식 클래스로 instance를 만들면 된다!

```python
import abc

# 얘는 Abastract metod!
class Room(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def openDoor(self):
        pass
    @abc.abstractmethod
    def openWindow(self):
        pass

# abstract method를 받아 실제 작동하는 class를 만든다
class BedRoom(Room):
    def openDoor(self):
        print("Open bedroom door")
    def openWindow(self):
        print("Open bedroom window")
room1 = Bedroom()
print(issubclass(BedRoom, Room), isinstance(room1, Room)
     
# 근데 만일 아래와같이 abstract class의 method를 모두 구현하지 않으면? 
class BedRoom(Room):
    def openDoor(self):
        print("Open bedroom door")
      
room1 = Bedroom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))
# >> 오류가 나옴!
```



#### (3) Overriding Methods in `object`

- 모든 파이썬 클래스는 `object`의 자식 클래스. 따로 써주지 않아도 기본적으로 받게 됨. 
- 즉, `class Room: ` 라는것은 곧, `class Room(object):`와 동일함
- 그럼 `objcect` 클래스에는 어떤 메소드들이 있을까? 
  - `__init__` : construtor. 내가 `__init__`을 쓰면,`object`클래스에 있는 `__init__`을 override해서 구현되는 것. 
  - `__del__ ` : 
  - `__eq__`: `==`활용 방법 정의. 같은 class로 만들어진 instances 들이 가진  attribute들이 동일한지 equality 비교할 때 이용. 본래 `==`는  `is`랑 달라서 memory space를 비교하진 않음. 그냥 그 값 자체 비교. 즉, 이 경우에도 두 인스턴스를 가지고 `instance1 == instance2`를 실행하면, `__eq__` 메소드를 콜해서 실행. 
  - `__cmp__ ` : `>`, `<` 활용 방법 정의 
  - `__add__` : `+` 활용 방법 정의



[*Duck Typing* : 막 프로그래밍 한 것..?!]

```python
def __eq__(self, other):
    if isinstance(other, Room):
        if(self.getVolume() == other.getVolume()): # 이 단계에서 other 이라는 것이 Room으로 만들어진 인스턴스인지 알 길은 없음. 그래도 일단 막 프로그래밍 함. 오류는 나중에 실행해서 발생하면 그때 고치자! 는 것이 파이썬의 정신. 
```





### 2-5. UML Notation 2

#### (1) More about UML Notations

- 지금까진 class의 다이어그램을 주로 살펴봤는데, 현실엔 다양한 다이어그램이 있음

  - 예: use case diagram, state diagram, deployment diagram 등등

  - 우린 object-oriented programming을 하다보니 class diagram에 집중했던 것

![1556704635315](C:\Users\nrchu\AppData\Roaming\Typora\typora-user-images\1556704635315.png)

[복습]

- visibility option --> 인캡슐레이션
- methods 시그니쳐가 super class와 subclass에서 동일한 경우에는 method override 가능
- methods 시그니쳐가 비슷한경우(파라미터만 다른 경우) method overloading 가능(default 값 넣어서 구현)



큰 프로그램은 여러 클래스를 묶어서 구현해야 함



![1556704806605](C:\Users\nrchu\AppData\Roaming\Typora\typora-user-images\1556704806605.png)

- 직선 = association 관계. 그냥 뾰족한 화살표
- generalization : 속이 빈 화살표. class를 interite 할 떄. 3개의 다른 방법으로 공통된 속성(amount)을 뱉어 냄
- 마름모꼴 화살표 : aggregation 

