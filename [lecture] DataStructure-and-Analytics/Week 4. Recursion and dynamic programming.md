# Week4 Recursion and dynamic programming

이번 주 학습 목표

- 재귀 호출 이해 및 구현

- 재귀 함수의 결과를 재활용하는 다이나믹 프로그래밍 이해 및 구현



## 4.1. Recursion

### (1)  Repeating Problems and Divide and Conquer

- 회사가 연간 예산을 짜면 각 부서별로 예산이 내려감. 그 중 판매 부서는 또 판매 지역별로 예싼을 나눔 ==> 계층적으로 전체 큰 그림이 쪼개져 내려감 ==> '쪼개서 쓴다'는 문제는 조직 아래로 내려가면서 반복. 큰 문제 안에는 쪼개서 보면 반복되는 문제가 있음. 이를 **Repeating Problem**이라고 함
- 문제를 잘게 쪼개어서(Divide) 해결해나가는(Conquer)것을 **Divide & Conquer**라고 함

```python
class Department:
    def calculateBudget(self):
        sum = 0
        dept = ['sales, manu, randd']
        for itr in range(0, numDepartments):
            sum = sum + dept[itr].calculateBudget() # 이 부분이 Recursion!
        return sum
```



- 예제 더 알아보기
  - Factorial도 repeating problem 을 가지고 있음. `n!` = `n * (n-1)!`임. 팩토리얼의 반복
  - Great Common Divisor(최대공약수). 
    - GCD(32,24) = 8
    - Euclid's algorithm: GCD(A,B) = GCD(B, A mod B), GCD(A, 0) = A
    -  `GCD(32, 34)` = `GCD(24, 8)` = `GCD(8, 0)` --> size reducing & GCD function call은 동일
  - 예제들 특징 : 
    - function call 반복  
    - 파라미터 사이즈는 줄어들고
    - 점화식(mathematical induction)과 매우 유사한 방식의 프로그래밍



### (2) Recursion

> *Recursion is a programming method to handle the repeating items in a self-similar way*

- 보통 함수 안에서 그 함수를 불러오는 형태

``` 
#Pseudo Code
def functionA(target):
...
functionA(target')
...
if (excapeCondition)
return A
```

## recursion 피보나치 구현하기

```python
def Fibonacci(n):
    if n== 0:
        return 0
    if n == 1:
        return 1 # n이 0이나 1이 되기 전까지 계속 자기 자신을 호출
    intRet = Fibonacci(n-1) + Fibonacci(n-2)
    return intRet
```

``` python
#Fibonacci(n) = 0, 1, 1, 2, 3



# F(4)=3
    # --> F(3)=2
        #--> F(2)=1
            # --> F(1)=1
            # --> F(0)=0
        #--> F(1)=1
    # --> F(2)=1
        #--> F(1)=1
        #--> F(0)=0
```





