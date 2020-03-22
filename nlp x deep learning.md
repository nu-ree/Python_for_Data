# Stanford CS224N: NLP with Deep Learning | Winter 2019 | Lecture 2 – Word Vectors and Word Senses

https://youtu.be/kEMJRjEdNzM



- count base approach

## 1. Review : Main idea of word2vec

- 문서 전체를 구성하는 각 단어를 돌면서(iterate) 계산
- 워드 벡터를 이용해서 주변 단어를 에측함
- 돌면서  예측을 잘할 수 있게 벡터를 업데이트 해나감
- $P(o|c)$ : 중심단어 $c$ 가 주어졌을 때, 주변 단어 $o$가 주어질 확률을 두 가지 단어의 벡터곱에 대한 softmax 값으로 계산하여 이를 확률로 만들어줌
- 벡터값을 업데이트 할 때마다, 특정 맥락에서 볼 만한 단어의 확률을 최대한 높여줌

? high frequency effect



## 2.Optimization : Gradient Descent

- 비용함수 $J(\theta)$ 를 최소화 해야함. 경사하강 알고리즘으로! 

  - 경사하강법의 알고리즘은? for current value of $\theta$ , calculate gradient of $J(\theta)$, then take **samll step in the direction of negative gradient** 이걸 반복. 
  - 주의 ! 때에 따라 objective 가 convex하지 않을 수도 있음

- Update equation (for a single parameter): 

  $$ \theta_j^{new} = \theta_j^{old} - \alpha \frac{\partial}{\partial\theta_j^{old}} J(\theta)$$

- Algorithms:

  ```python
  while True:
    theta_grad = evaluate_gradient(J, corpus, theta)
    theta = theta - alpha*theta_grad
  ```

### Stochastic Gradient Descent

- 문제점: 1억개의 단어로 구성된 데이터를 넣는다면, window = 2로만 해도,  1억개의 center words가 있고, 1억 * 2 = 2억개의 주변 단어가 생긴다는 것! 한 턴 도는데만 해도 엄청나게 많은 시간이 걸림!

- 즉, $J(\theta)$ : a function of all windows in the corpus (너무 많음)
  - 계산하는 데 비용이 매우 큼 .한 번 벡터를 업데이트 하는데 엄청 나게 많은 시간을 기다려야 함
- 그래서 **Stochastic gradient descent(SGD)**
  - repeatedly sample windows, and update after each one.

```python
whie True: 
  window = sample_window(corpus)
  theta_grad = evaluate_gradient(J, window, theta)
  tehta = theta - alpha * thata_grad
```

- 가령 32, 64개의 샘플을 골라서 미니 배치를 돌림
  - 장점 : 
    - 병렬처리가 가능해져 더욱 빨라진다 
    - less noisy estimate가 된다

### Stochastic gradient with word vectors!

- nlp에서의 SGD는 다른 딥러닝들과 다른 점이 있음 : 
  - 미니배치를 돌릴 때 (예를 들어 미니배치 사이즈 32로 돌리고, 윈도우 사이즈를 10으로 한다 했을 때), 해당 배치 샘플에는 100~150가지 단어가 있을 것. 나머지 수백억개의 단어 칸에는 0이 채워지게 되고.. 너무 sparse 해지는 문제가 있음 ! 배치에 있었던 단어에 대해서만 업데이트 하게 될 것

> solution : 
>
> either you need sparse matrix update operations to only update certain rows of full embeddedding matrixces U and V, or you need to keep around a hash for word vectors

> if you have millions of word vectors and do distributed computing, it is important to not have to send gigantic updates around!

???





38:58

### 3.But why not capture co-occurence counts directly?

- co-occurence matrix X를 만드는 두 가지 방법 
  - windows vs full documents
- Window based co-occurrence matrix
  - w2v 처럼 각 단어마다 주변 단어들 보고 syntatic과 semantic을 수치화
  - 왼쪽 오른쪽 구분하지 않음 = symmetric
  - ![스크린샷 2020-03-21 오후 6.25.28](/Users/apple/Desktop/cs224n-lec2-p17.png)
  - Problems
    - increase in size with vocabulary
    - very high dimension
    - sparsity problems
  - Solution : Low dimensional vectors
    - 고정된, 낮은 차원의 dense vector 만들어서 주요 정보를 저장해보면 어떨까
    - 25~1000 차원 정도로. 
    - 차원은 어떻게 축소하지?
      - Singular Value Decomposition(SVD)

### Hacks to X (several used in Rohde et al. 2005)

- Scaling the counts in the cells can help ***a lot***
- Problem : 관사같은 단어는 너무 자주 나옴 -> syntax가 너무 많은 영향력을 가지게 됨 min(X, t), with t = 100 하거나 전부 다 무시

- 가까운 단어를 더 많이 카운트할 수 있게 윈도우를 늘리거나
- 카운트 대신에 Pearson correlations 이용해서 음수값은 0으로 바꾸기



### count based vs direct prediction

![스크린샷 2020-03-21 오후 6.51.25](/Users/apple/Desktop/cs224n-lec2-p26.png)