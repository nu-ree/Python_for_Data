#자료구조

# Week3. Linked list, stack and queue
## 3.1. Abstract Data Types
* Abstract Data Types란? 데이터의 구조를 추상화하여 (=간단히) 표현해준다.
* 여기서 ‘데이터의 구조’라 함은 어떤 데이터가 저장되어있는지, 어떤 작업(=operation)이 가능한지 등의 정보를 의미한다. 
* 에러가 날 수 있는 조건을 미리 정할 수도 있다(이번 강좌에선 중요하게 다루지 않음)
* 주머니 속은 알 수 없지만, 속에 어떤 데이터가 있는지, 어떤 작업으로 데이터에 영향을 미칠 수 있는지 정의해놓는 것이 *abstract data type*임

## 3.2. Array
### (1) 파이썬과 다른 언어에서의 array 특징
* Array를 파이썬에서는 List라고 부름
* 일반적으로 array는 동일한 데이터를 인덱스를 활용하여 저장 & 접근 할 수 있는 데이터 유형을 의미함. 각 요소(elements)에는 인덱스가 있어야 함
* 파이썬 list의 특징 : 첫 번째 인덱스는 0부터 시작함. 리스트를 정의하는 것이 매우  간단함. 다른 언어에서는 사이즈나 타입을 미리 정해줘야 함. 파이썬에선 간단히  `X = [‘a’, ‘b’, ‘c’, ‘d’]`로 정의함

### (2) 언제 리스트를 쓸까?
* 사람들 사이에서 ‘정’씨를 찾아야할 때, 한 사람에게 여러번 물어보면 비효율적! 한 줄로 세워놓고 체크하면 좀 더 쉬움. 마구 뒤엉킨 형태를 *선형*으로 정돈해주자
* 화장실을 찾고 싶다. 복도를 따라가면서(=*선형* 공간을 따라가면서)  하나씩 문을 열어서 확인해보면 쉬움.

### (3) Search procedure in array
* 리스트에서 원하는 요소를 찾는 방법은? 
	* 방법1. 리스트 길이 확인 —> for loop을 이용해서 원하는 요소인지 아닌지 확인. 최대 리스트 길이 만큼 루프가 돌아가야 있는지 없는지 확인할 수 있음
	* 방법2. 파이썬에서는 `in` 을 이용해서 원하는 요소를 찾을 수도 있음
```
X = [‘a’, ‘b’, ‘c’, ‘d’]

‘d’ in X 
# >> True
```

### (4) Insert procedure in array
* 리스트에서 데이터를 집어 넣는 방법은?
  * 1) 데이터가 추가된 길이의 새로운 리스트(가짜 데이터 들어있는 리스트) 만들기 
  * 2) 추가하고자 하는 위치까지 각 값을 모두 복붙
  * 3) 추가하려는 위치에 추가
  * 4) 나머지 위치의 각 값을 모두 복붙
* N번의 과정이 필요
```
IdxInsert = 2

Y = range(6) 
for itr in range(0,IdxInset):
    

Y[0] = X[0] # ‘=‘ 는 reference 관계. Reference를 복사해서 넣어라
 
```
### (5) Delete procedure in array
* 리스트에서 데이터를 삭제하는 방법은? 
  * 1) 뺄 데이터가 있는 위치 앞까지 짤라서 받아오기
  * 2) 앞에서 받아온 리스트 뒤에다가 쨀 데이터가 있는 위치 뒤부터 짤라서 붙이기





- Array는 등간격 스페이스에 데이터를 저장함. 인덱스 기반 접근. 
- Linked list는 등간격으로 데이터를 집어넣지 않음. 인덱스 기반(선형적으로 정의된 공간, 등간격으로 정의된 공간)으로 데이터를 저장하지는 않음. 
- 왼쪽에 있는 애들을 밀어서 공간을 만들어냄. 



## 3.3. Linked List

- 앞이나 뒤에 값을 추가하거나 삭제하는 데 O(1)의 시간이 들어감(array는 O(n))
- -

### (0) 복습! Assignment and Equvalence

linked list를 사용하면 인덱스가 아닌 '레퍼런스 구조'로 중간에 공간을 만들어낼 수 있음

- `==` :  '값(value)'이 동일한지 확인
- `is`:  같은 곳에 저장(objects' ID) 되어있는지 확인

```python
x = [1,2,3]
y = [100,x,120]
z = [x, 'a', 'b']

print(x)
>> [1,2,3]

print(y)
>> [100, [1,2,3], 120]

x[1] = 1717 # x의 두 번째 값이 바뀌면?! 
print(y)
>> [100, [1,1717,3], 120]
print(z)
>> [[1,1717,3], 'a', 'b']

```

### (1) Basic structure : singly linked list

> *Construct a singly linked list with nodes and references*

- 어떤 노드로 구성? 
  - 두 가지 variable로 구성(*class로 만들어서 member variable을 2개 가지도록 만들어야 한다는 것을 의미*)
  - 한 가지 variable는 다음 노드가 무엇인지 reference를 저장하는 variable.
  - 다른 하나는  해당 노드의 값을 저장하는 노드. 

- Special nodes : Head & Tail
  - Head 노드는 리스트의 첫 번째 노드. Tail 노드는 마지막 노드. 이 둘에는 값이 저장되어 있진 않음
- Singly linked list 의 구조![views](https://wayhome25.github.io/assets/post-img/cs/linked-list2.png)
  **출처 :** <https://github.com/ythwork/>



- array 로 만든 리스트보다 복잡한데 왜 쓸까? 
  - 레퍼런스 구조로 되어있어서 중간에 공간을 만들 때, 레퍼런스 구조만 사용하여 한번에 공간을 만들어 낼 수 있음

- 노드 클래스를 만들어보자
  - 클래스라는 것이 있어서 두 개의 변수(`nodeNext`와 `objValue`를 하나로 묶어서 관리할 수 있음

```python
class Node:
    nodeNext = ''
    objValue = ''
    binHead = False # head 인지 알려주는 변수
    binTail = False
    
    def __init__(self, objValue = '', nodeNext = '', binHead = False, binTail = False):
        # 값을 받아서 class instance의 member variable로 저장
        self.objValue = objValue
        self.nodeNext = nodeNext
        self.binHead = False
        self.binTail = False
    def getValue(self):
        return self.objValue
    def setValue(self, osbValue):
        self.objValue = objValue
    def getNext(self, nodeNext):
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    def isHead(self):
        return self.binHead
    def isTail(self):
        return self.binTail
    
```

```python
node1 = Node(objValue = 'a')
nodeTail = Node(binTail = True) # 다음 node가 없음
nodeHead = Node(binHead = True, nodeNext = node1) # 다음 노드는 있지만, object value는 없음

# nodeHead >> node1 >> nodeTail 의 구조로 만든 linked list!
```

### (2) Head and Tail 

- head와 tail은 리스트의 처음, 끝에 있는 노드
- 링크드 리스트에 내용이 하나도 없으면 `Head >> Tail`로 구성되는 리스트가 될 것 = **Empty Linked List**
- head와 tail 안에 있는 object는 내용을 저장하고 있지 않음(값이 없음)
- 리스트의 처음과 끝을 알려주는 노드
- head와 tail이 없으면 링크드 리스트를 만들 수 없을까? 
  - 없어도 링크드 리스트를 만들 수는 있지만 iteration을 돌림에 있어서 head와 tail이 있는 것이 유용함

### (3) Search process in singly linked list

- a부터 f까지 값을 가진 리스트가 있다. 
- 여기서 d와 c를 찾으려면? 
- 하나씩 하나씩 체크하며 넘어감. 즉,  n 개가 있는 리스트에서는 최대 n 번 확인해야 끝남. 이 부분은 array 와 동일. 

- array와 다른 점은 'index'를 쓰지 않고 'nextNode' 정보를 얻어서 다음 값으로 넘어감

- search process:
  - 1) next node가 tail node?
  - 2) tail이면 search가 끝
  - 3) tail이 아니면 objValue를 찾아서 'd'가 맞는지 확인
  - 4) 찾으면 끝. 아니면 다시 돌아가서 이 과정을 반복



### (4) Insert process in singly linked list

- 이 부분에서 linked list의 POWER가 발휘!!
- 넣고 싶은 위치(어떤 노드 다음?)는 이미 알고 있는 것으로 간주. 즉, `node_prev`와 `node_next`는 알고 있음
- 새로 넣을 노드 `node_new`를 instance로 만들어서 value를 넣어둔 상태
- `node_prev`의 next node를 `node_new`로 설정 
- `node_new`의 next node를 `node_prev`의 과거 next node로 설정
- 즉, `A >> B >> C >> D >> E >> F` 순의 리스트에서 B와 C사이에 데이터를 넣는다고 했을 때,  A의 레퍼런스 구조와 D의 레퍼런스 구조는 바꿀 게 없음. 오로지 집어 넣는 노드의 앞뒤 내용만 바뀌게 되는 것.  

### (5) Delete process in singly linked list

- 이 부분에서도 linked list의 POWER가 발휘!!
- 지울 노드의 위치, 즉`node_prev`는 이미 알고 있는 것으로 간주
-  `node_next`를 가져와서 `node_prev`의 다음 노드로 설정

```python
class SinglyLinkedList:
    nodeHead=''
    nodeTail=''
    size = 0
    def __init__(self):
        self.nodeTail = Node(binTail = True)
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)
        
    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1
        
    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()
    
    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurren.getNext()
            print(nodeCurrent.getValue(), end=" ")
        print("")
        
    def getSize(self):
        return self.size
```

```python
list1 = SinglyLinkedList()
list1.insertAt('a', 0)
list1.insertAt('b', 1)
list1.insertAt('d', 2)
list1.insertAt('e', 3)
list1.insertAt('f', 4)
list1.printStatus()

list1.insertAt('c', 2)
list1.printStatus()

list1.removeAt(3)
list1.printStatus()

print("----------output---------------")
'''
a b d e f
a b c d e f
a b c e f
'''
```





### Doubly Linked Lists:

- next pointer와 previous point 모두 있음 

  

![1563960179904](C:\Users\nrchu\AppData\Roaming\Typora\typora-user-images\1563960179904.png)+

## 3.4. Stack

### (1) Scenario of Stack

- 타는 순서의 반대로 내리게되는 택시를 탈 때와 비슷.  
- 항공기에 짐을 싣는 것과도 비슷. 들어가고 나가는 위치가 한 곳으로 정해져있음. 

 

### (2) Structure of Stack

- singly linked list의 변형
- last in first out 구조(LIFO 구조)
- linked list는 중간에 데이터를 넣을 때 사용한 insert operation을 사용할 수 없음
- linked list의 중간이나 끝에 있는 것은 관리를 안함. 오로지 문 앞에 있는 애들만(fist node)을 이용해서 데이터를 넣고 뺄 것. 이 첫번째 element를 **top**이라고 부름
- stack의 **top 만을 이용해서 insert & remove operation을 이용**
- 

### (3) Operation of Stack

- search 안함. insert와 delete 모두 top에 대해서만 시행 
- insert --> push 
- delete --> pop
- linked list 의 insert와 delete에 살짝의 베리에이션을 주면 됌! 유용한 linked list!

```python
from edu.kaist.seslab.ie362.week3.SinglyLinkedList import SinglyLinkedList
class Stack(object):
    lstInstance = SinglyLinkedList()
    def pop(self):
        return self.lstInstance.removeAt(0)
    def push(self):
        self.lstInstance.insertAt(value, 0)
```

```python
stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')

print(stack.pop())
# >> 'c'
print(stack.pop())
# >> 'b'
```



### (4) Example: Balancing Symbols

- 중괄호, 대괄호로 수식을 만들어보자
  - `7 + {10*[2+3]}` --> balancing이 잘 되어있음
  - `7 + {10*[2+3}]` --> balancing이 잘 안되어있음. 대괄호가 이상한 곳에서 닫힘
- 이를 어떻게 검사할까? 
  - 1) empty stack을 만든다
  - 2) 여는 symbol이면 스택 안에 **push**
  - 3) 닫는 symbol인데, empty stack이면 오류 반환. 
  - 4) 닫는 sumbol인데, 열렸던 symbol이 다른 모양이면 오류 반환
  - 5) 닫는 symbol과 동일하고 empty symbol이 아니면 **pop**.



### + 언제 유용? 

- 위에 나온 예시처럼 괄호의 균형이 맞는지 확인할 때. 앞에서 부터 순서대로 체크하고 넘어가야 하므로
- Stack을 만들고, `{`를 찾으면 stack으로 넣기 --> `[` 도 stack에 넣기--> `]`인데 stack 제일 위에서 꺼낸 괄호가 `[`가 아니면 틀림 . 맞으면 제일 위에 있던 애 빼기. 스트링에 있는 다음 괄호가 닫는 괄호 --> 스택에 남아있는 `}`랑 매칭 --> 빼기. 스택  

- 각각의 operation은 **O(1)**
- 

## 3.5. Queue

### (1) Scenario of Queue

- Singly linked list의 특별한 버젼. 
- first in first out 구조(FIFO 구조)
- 들어가는 곳(going in)과 나가는 곳(going out)이 다름
- 중간에 새치기 불가능
- 제품 만드는 과정, 컨페이어 밸트와 비슷. first instance를 통해 나오고 last instance를 통해서 들어감

### (2) Operation of Queue

- Enqueue : 
  - 리스트의 insert 격의 작업을 *마지막* 인스턴스에 대해 수행
  - 링크그 리스트의 마지막에 넣어줌
- Dequeue: 
  - 리스트의 remove 격의 작업을 *첫 번째* 인스턴스에 대해 수행

### (3) Implementation of Queue

- Singly linked list의 특별한 버젼이니까, 이를 활용해서 만들어보자 

```python
from edu.kaist.seslab.ie362.week3.SinglyLinkedList import SinglyLinkedList
class Queue(object):
    lstInstance = SinglyLinkedList()
    def dequeue(self):
        return self.lstInstance.removeAt(0)
    def enqueue(self): 
        # list size가 변함. 즉, list size에 따라 들어갈 위치(index)가 달라짐
        self.lstInstance.insertAt(value, self.lstInstance.getSize())
```

```python
queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print(queue.dequeue())
# >> "a" 
print(queue.dequeue())
# >> "b"
```



