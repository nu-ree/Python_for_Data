# Lecture 1 – Introduction and Word Vectors

Stanford CS224N: NLP with Deep Learning | Winter 2019 

### 1.How do we have usable meaning in a computer? 

- 일반적인 솔루션 = WordNet 같은거 사용하기
  - `from nltk.corpus import wordnet as wn`
  - 예를 들면 "good"의 동의어, hyperonyms(hierarchy structure) 알 수 있음
- WordNet의 단점 : 
  - 뉘앙스를 담지 못함. 
  - 단어의 새로운 의미를 알지 못함(impossible to keep up-to-date!)
  - 주관적
  - 만드는데 인간이 공을 들여야 함 
  - 정확한 word similarity를 계산할 수 없음

- Representing words as discrete symbols

  - 전통적으로 NLP에서는 각 단어를 discrete symbols로 표현했음

  - hotel, conference, motel이 있으면 , 각각을 **localist representation**으로 표시함. (one-hot vector처럼)

  - 이 방법의 단점은 ? 

    - 엄청나게 다양한 단어가 존재. 거의 무한대.(가령 단어 끝에만 바꿔서 새로운 단어 무한 생성..) . 즉, 벡터가 너무 커짐

    - 더 큰 문제는, 단어간 similarity relationship을 고려하지 못함. 예를 들어 "seattle motel"이나 "seatel hotel"을 비슷하게 봐야하는데, 이런 개념을 반영할 수 없음!

      - 이 문제는 그럼 WordNet으로 해결할 수 있을까? No. incompleteness 등의 문제가 있음

    - 대신, 벡터 자체의 유사도를 인코딩하는 방법을 알아보자!

      > ***Instead, learn to encode similarity in the vectors themselves***

- Representing words by their context
  - Distributional semantics : 주변에 자주 등장하는 단어에 따라  단어의 의미를  부여하자
  - 현대 통계적 NLP에서 가장 성공적인 아이디어 중 하나!
  - context : 단어 w가 텍스트에서 등장할 때, context란 그 단어 주변(with in a fixed size window)에 가이 등장한 단어의 모음(set)
- Word Vectors
  - 단어를 "distributed representation"으로 표현함 
  - "banking" = [0.286, 0.792, -0.177, -0.107, 0.109, -0.542, 0.349, 0.271]
  - 이렇게 표현되면, "banking"의 의미가 전체 벡터에 골고루 표현되게 됨. 
  - One-hot vector 보다 dense 해짐
  - 동일한 맥락에서 등장한 워드 벡터는 동일함 
  - word vectors, word embeddings, word representations 등 모두 같은 말임



## 3. Word2vec : Overview

- Word2vec(Mikolov et al. 2013) : word vectors를 학습시키는 프레임워크
- 워드 벡터의 차원은 누가 결정하는가? 우리가 직접 설정? 
  - 그건 학습 알고리즘이 결정해서 알아서 아웃풋을 낼 것. 
- 아이디어 : 
  - 우리에겐 많은 corpus of text가 있다
  - fixed vocabulary에 속하는 모든 단어는 벡터로 표현할 수 있다
  -  텍스트에서 중심 단어c와 맥락 단어 o(outside, 윈도우는 설정하기 나름)로 구성된 각 위치 t를 훑는다. 
  - c와 o의 단어 벧터 유사도를 이용해, c가 주어졌을 때 o가 등장할 확률을 계산한다.
  - 이 확률을 극대화 할 수 있는 방향으로 워드 벡터를 고쳐나간다.  

- 예를 들어서, 아래와 같은 문장이 있다고 하자

  - > *... problems turning **into** banking crises as ...*

  - 이 문장에서 "into"의 의미는 문장에서 어떤 맥락에서 사용되었느냐가 결정한다고 생각하는 것이 w2v

- **Likelihood**는 아래와 같음
  $$
  L(\theta) = \prod_{t=1}^T \prod_{-m\leq j \leq m (j \neq 0)}P(w_{t+j}|w_{t};\theta)
  $$
  $\theta$가 바로 우리가 최적화 해야 할 모든 변수.

- **목적 함수** $J(\theta)$ 는 negative log likelihood의 평균 값
  $$
  J({\theta}) = -\frac{1}{T}logL(\theta) 
  =-\frac{1}{T}\sum_{t=1}^T \sum_{-m\leq j \leq m (j \neq 0)} logP(w_{t+j}|w_{t};\theta
  $$
  

  목적 함수는 최소화 = 예측 정확도는 최대화

- 이제 우리의 목표는 $J({\theta})$를 최적화 하는 것!

  - 그렇다면 $P(w_{t+j}|w_{t};\theta)$는 도대체 어떻게 구해야할까? 
  - 한 단어당 두 개의 벡터를 이용할 것!
    - $v_w$ : $w$가 중심 워드일 때의 벡터
    - $u_w$ : $w$가 맥락 단어 일 때의 벡터

- $P(o|c) = \frac{exp(u_o^Tv_c)}{\sum_{w\in V}exp(u_w^Tv_c)} $ 의 의미를 파헤쳐보자!

  - center word c가 주어졌을 때, context word o가 주어질 확률은?
  - $exp$ : makes anything positive
  - dot product($u_o^Tv_c$): __compares similarity of $o$ and $c$__
    - $u^Tv = u.v = \sum_{i=1}^n u_i v_i$
    - 이 값이 클 수록 확률 $P(o|c)$ 값은 커짐
  - $1 / (\sum_{w\in V}exp(u_w^Tv_c))$ : normalize over enitre vocabulary to give probability distribution

- 이 함수는 **softamx function**의 사례임

  $softmax(x_i) = \frac{exp(x_i)}{\sum_{j=1}^{n} exp(x_j)} = p_i$

  - 임의의 값 $x_i$를 확률 분포 $p_i$에 매핑시켜줌

  - "max" : cuz amplifies probability of largest $x_i$
  - "soft" : cuz still assign some probability to smaller $x_i$
  - 딥러닝에서 자주 이용됨

- 모델 트리이닝 하기 
  - loss를 최소화하는 방향으로 파라미터를 최적화하면서 모델 학습시켜야 함
  - Compute all vector gradients!
    - $\theta$는 파라미터를 의미함
    - w2v의 경우 $\theta$는 d차원의 벡터를 뜻함.
    - $ \theta = [ v_{aardvark} , v_a, ... , v_{zebra}, u_{aardvard}, u_a, u_{zebra}] $
    - 모든 단어는 두 가지 벡터로 표현!
    - 그래디언트 디센트를 통해 최적화 해나갈 수 있음
- 각 벡터는 랜덤 값에서 시작하여 최적화 해나갈 것
  - 아웃풋이 될 벡터는 어떤 단어 w가 어떤 맥락에서 등장하는지에 따라 그 의미를 설명할 수 있는 벡터여야 함! 
  - **어떤 중심 단어 주변에 자주 나오는 주변 단어라면, P(o|c)의 값은 올라가게 나올 것이고, 주변에 자주 나오지 않는 주변 단어라면 P(o|c)는 낮게 나올 것** 
- 그래디언트 디센트를 해보자!
  - 식은 아래와 같다 

$$
\frac{\partial}{\partial {v_c}} log \frac{exp(u_o^Tv_c)}{\sum_{w=1}^v exp(u_o^Tv_c)} \\
\\

= \frac{\partial}{\partial v_c} log {exp(u_o^Tv_c)} - \frac{\partial}{\partial v_c}log{\sum_{w=1}^v exp(u_o^Tv_c)}
$$

- $\frac{\partial}{\partial v_c} log {exp(u_o^Tv_c)}$

  - Log 와 exp는 반대니까 지워버릴 수 있음
  - $\frac{\partial}{\partial v_c}(u_o^Tv_c) = u_o$ 
  - $(u_o^Tv_c)$ 풀어서 쓰자면...

  $u_{o_1}v_{c_1} + u_{o_2}v_{c_2}+ ...+u_{o_{100}}v_{c_{100}}$

  - 이를 $v_c$로 미분하면? $v$ 는 지워지고.. 
  - $[u_{o_1}, u_{o_2}, ... , u_{o_{100}} ]$ 만 남음
  - 즉, $u_o$만 남음!

- $\frac{\partial}{\partial v_c}log{\sum_{w=1}^v exp(u_o^Tv_c)}$ 

  - chain rule 기억하기! 
  - log는 미분하면 역수로 바꾸어버림 
  - $= \frac{1}{\sum_{w=1}^v exp(u_o^Tv_c)} \frac{\partial}{\partial v_c}\sum_{x=1}^v  exp(u_x^Tv_c)$
  - $= \frac{1}{\sum_{w=1}^v exp(u_o^Tv_c)} \sum_{x=1}^v \frac{\partial}{\partial v_c} exp(u_x^Tv_c)$
  - $= \frac{1}{\sum_{w=1}^v exp(u_o^Tv_c)} \sum_{x=1}^v \frac{\partial}{\partial v_c} exp(u_x^Tv_c)$
  - $= \frac{1}{\sum_{w=1}^v exp(u_o^Tv_c)} \sum_{x=1}^v exp(u_x^Tv_c)\frac{\partial}{\partial v_c} u_x^Tv_c$
  - $= \frac{1}{\sum_{w=1}^v exp(u_o^Tv_c)} \sum_{x=1}^v exp(u_x^Tv_c)u_x$

- 즉, 
  $$
  \frac{\partial}{\partial {v_c}} log P(o|c) \\
  = u_o - \frac{\sum_{x=1}^v exp(u_x^Tv_c)u_x}{\sum_{w=1}^v exp(u_o^Tv_c)} \\
  = u_o - \sum_{x=1}^{v} \frac{exp(u_x^Tv_c)}{\sum_{w=1}^v exp(u_o^Tv_c)}u_x
  $$

  - 여기서 $ \frac{exp(u_x^Tv_c)}{\sum_{w=1}^v exp(u_o^Tv_c)}$ 이 부분은 $P(x|c)$와 같은 의미!
  - 따라서

  $$
  \frac{\partial}{\partial {v_c}} log P(o|c) \\
  =u_o - \sum_{x=1}^v P(x|c)u_x
  $$

  

- 우리의 목적함수의 기울기는 어떻게 구해질까? 

  - observed representation of context words - what the model think the context should look like! 
  - weighted average of (representation of  each word * probability of the word in the current model) 
    - = expected context word
  - 실제 나타나는 context words ($u_o$)에서 expected context words를 빼주는 것. 이 차이가 가중치를 어느 방향으로 바꾸어 나가야하는지 알려줌!!
