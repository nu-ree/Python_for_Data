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
- 소프트웨어를 설계하는 표준을 배워야 함 --> **Unified Modeling Language(UML)**을 배워보자
- 다양한 UML이 존재하지만 Class를 활요하는 UML을 알아보자

### (2)  UML notation : Calss and Instance

- 하나의 클래스는 member variable 과 member functions 으로 구성된다. 
- 

- 