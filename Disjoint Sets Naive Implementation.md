# Disjoint Sets

## 1. Naive Implementation

### 1. Overview

- 미로에서 길찾기(maze) 같은 문제에 적용 가능한 알고리즘

- **Disjoint-set data structure**에는 다음 3개의 operation이 있음
  - `MakeSet(x)` : 1개의 원소를 가지는 set을 만듦
  - `Find(x)` : x를 원소로 가지는 set의 ID 반환
    - {x,y} 이면, Find(x) = Find(y)
    - {x}, {y} 이면, Find(x) != Find(y)
  - `Union(x,y)` : 두 개의 set을 합침
- 미로 문제에 어떻게 적용할 수 있을까? 
  - 시작점(B)에서 끝점(A)까지 가는 길을 찾아야 함
  - 미로의 각 셀에 대해서 이어지는 주변 셀을 담은 set을 만들어냄
  - 시작점(B)와 시작점(A)가 모두 들어있는 set을 찾음

```pseudocode
/* Preprocess */ 
def Preprocess(maze):
	for each cell c in maze:
		MakeSet(c)
	for each cell c in maze:
		for each neighbor n of c:
			Union(c,n)
/* Check if two points are reachable */
def IsReachable(A, B): 
	return Find(A) = Find(B)
```



- 네트워크 만들기에 어떻게 적용할 수 있을까? 
  - 1번부터 4번까지 장비가 있다고 하자. 서로 연결되어 있지 않은 상태에서는 Find(1) != Find(2)임
  - Union(3, 4) Union(3,2)  => 2 - 3- 4번 장비 연결. 여전히 Find(1) != Find(2)
  - Union(1,3) => Find(1) == Find(2) 가 된다!



### 2. Naive Implementations

#### Using the smallest element as ID

- 1부터 n까지의  object가 있다고 해보자. 가장 작은 값을 ID로 설정하려 한다.  ID는 array로 저장한다. 
- 가령 `{9,3,2,4,7}`, `{5}`, `{6,1,8}` 3개의 set이 있다면
  - `smallest[1] = 1`  1이 들어있는 set의 최소값은 1 --> Find(1) = 1
  - `smallest[9] = 2` 9가 들어있는 set의 최소값은 2 --> Find(9) = 2
  - 즉, `smallest = [1, 2, 2, 2, 5, 1, 2, 1, 2]`가 된다! 

```pseudocode
/* Make Set: O(1)*/
smallest[i] = i /*???? 이거 맞음?? */
smallest[i] = Find(i) /*이게 맞는 거 아님? ppt 이상한거 같다.*/

/*Find index of element i : O(1)*/
def Find(i):
	return smallest[i]
	
/* Union sets : O(n) */
def Union(i, j):
	i_id = Find(i)
	j_id = Find(j)
	if i_id == j_id:
		return /*두 id가 같으므로 이미 하나의 set에 있음. 합치지 않고 끝*/
	m = min(i_id, j_id)
	for k in range(0, n):
		if smallest[k] in {i_id, j_id}:
			smallest[k] = m  
			/* 두 개가 합쳐져야 두 id 중 작은 값으로 
			index array인 smallest의 값을 바꿔줌 */ 
			
```

#### Using the linked list tail as ID

- 위에서 해본 방법은 Union 의  러닝 타임이 O(n). 어떤 데이터 구조를 쓰면 보다 효율적으로 union을 할 수 있을까? 

  - Linked list를 써보자! set을 linked list로 만들고 list tail을 ID로 쓰는거야 

  - ` {9,3,2,4,7}`  ==> ID = 7,  `{6,1,8}`  ==> ID = 8 이 되는 것

  - Union 하고 싶으면 한 쪽에 append 하면 되고, 연결된 list의 tail이 ID가 된다. 

    Union(`{9,3,2,4,7}` ,   `{6,1,8}` ) ==> ID = 8이 되도록 7과 6을 연결

  - Union 의 Running Time: O(1)

    하지만 Find의 Running Time이 O(n)이 될 수 있음. 

    long list가 되면 문제 발생.  원하는 값이 tail에 있으면 Tail까지 훑어야 하니깐. 

#### 어떻게 해야 할까? 

- Union(`{9,3,2,4,7}` ,   `{6,1,8}` )==> ID = 7이 되도록  `{6,1,8}` 의 tail(=8)을 7에 연결해볼 수 있겠다!
- 이렇게 하면 거의 find에도, union에도 O(1) 의 시간이 걸림



## 2. Effective Implementation

### 1. Trees for Disjoint Sets

> Union(`{9,3,2,4,7}` ,   `{6,1,8}` )==> ID = 7이 되도록  `{6,1,8}` 의 tail(=8)을 7에 연결해볼 수 있겠다!

- 위 접근은 결국 linked list가 아니라 tree를 만들어냄 
- root가 set의 ID가 된다!

```pseudocode 
/* Make Set : 처음 set을 만들 때 i의 parent 리스트의 i번째 값은 i로 저장.
자기 자체가 root. O(1) */ 
def MakeSet(i):
	parent[i] = i 

/* Find : parent list에서 i의 parent 찾음. 제일 위에 있는 root까지 찾아 올라감.O(1) */ 
def Find(i):
	while i != parent[i]: /*루트가 아니면 반복*/
        i = parent[i]
    return i 
    
```

### 2. Union by Rank

- Union 할 때는 한쪽 트리의 루트를 다른 쪽 루트의 하위 트리가 되도록 연결. 그럼 어느쪽에다 붙여야함? 
  - tree는 가능한 '얕게(shallow)' 유지하는 것이 좋음. 그래야 Find에 걸리는 시간을 최소화 할 수 있음
  - 깊은 쪽에다가 얕은 트리 붙여야 함. 그래야 깊은쪽 트리가 더 깊어지지 않으니까. 
- 얕은 트리/ 깊은 트리를 판단하려면 set을 처음 만들때부터 tree의 height(=rank)를 따로 저장해둬야 함

```pseudocode
/* Make Set : rank 도 저장. 일단 최초에 만들어진 set이라 깊이 = 0. 
O(1) */ 
def MakeSet(i):
	parent[i] = i 
	rank[i] = 0 /*추가!*/

/* Find : 상동 */ 
def Find(i):
	while i != parent[i]: /*루트가 아니면 반복*/
        i = parent[i]
    return i 
    
/* Union : 얕은 트리의 root를 깊은 트리의 root에 연결 */ 
def Union(i, j):
	i_id = Find(i)
	j_id = Find(j)
	if i_id == j_id: 
		return 
	if rank[i_id] > rank[j_id]:
		parent[j_id] = i_id 
		/* 더 깊은 i_id로 j_id 바꾸기. 
		깊은쪽 tree의 rank가 union의 rank. */ 
	else: 
		parent[i_id] = j_id
		if rank[i_id] = rank[j_id]: 
		/* i랑 j가 들어있는 set의 깊이가 같음. i에 j를 붙임. j의 깊이가 1개 깊어짐*/ 
			rank[j_id] = rank[j_id]+1 
```



예제로 보자 
- 이런 set이 있다고 하자: `{1}, {2}, {3}, {4}, {5}, {6}`
  - parent = [1, 2, 3, 4, 5, 6]
  - rank = [0, 0, 0, 0, 0, 0]
- Union(4,2) 하면? 
  - parent = [1,4,3,4,5, 6]
  - rank = [0, 0, 0, 1, 0, 0]

- Union(5,2) 하면? 

  - rank[5] = 0이고 2의 루트인 4의 rank[4]=1이니까 4에 붙임
  -  parent = [1, 4, 3, 4, 4, 6]
  - rank = [0, 0, 0, 1, 0, 0]

- Union(3,1)하면? 

  - parent = [1,4,1,4,5, 6]
  - rank = [1, 0, 0, 1, 0, 0]

- Unioni(2, 3)하면? 

  - 2의루트인 rank[4] = 1이고 rank[3] = 0이니까 3은 4에 붙임
  - parent = [1,4,1,1,4, 6]

  - rank = [2, 0, 0, 1, 0, 0]

- Union(2,6)하면? 

  - rank[2]의 부모노드인 4의 부모노드인  1의 rank[1] = 2 이고 rank[6]=0이니까 6을 1에 붙임
  - parent = [1, 4, 1, 1 4, 1]
  - rank = [2, 0, 0, 1, 0, 0]



- 이렇게 tree 구조를 이용하면 Union의 running time은? 
  - l

> The union by rank heuristic guarantees that Union and Find work in time O(log n).

#### Lemma

- The height of any tree in the forest is at most log2N





















