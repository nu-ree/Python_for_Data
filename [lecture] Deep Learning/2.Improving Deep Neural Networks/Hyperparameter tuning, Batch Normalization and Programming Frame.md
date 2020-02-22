# 3. Hyperparameter tuning, Batch Normalization and Programming Frame

### 3.1. Hyper Parameter tuning

### 3.1.1. Tuning Process

- 튜닝해야 할 하이퍼파라미터
  - 가장 중요한 하이퍼 파라미터 : 학습률($\alpha$)
  - 러닝 속도에 영향을 미치는 하이퍼파라미터 : 
    - 모멘텀 텀($\beta$)
    - 미니배치 사이즈
    - 은닉 유닛 수
  - 그 외 중요한 하이퍼파라미터 
    - 층의 수, learning rate decay
- Try random values. Don't use a grid
  - 하이퍼파라미터가 몇 개 없을때는 그리드 서치도 괜찮음.
  - 딥러닝에서는 임의로 하이퍼파라미터를 골라서 시도하는 게 좋음. 훨씬 많은 파라미터를 시도해볼 수 있으니까.
  - 이렇게 하는 방법 중 흔한 방식이 "coarse to fine sampling scheme"

### 3.1.2. Using an appropriate scale to pick hyperparameters

- "랜덤 샘플링"이라고 해서 모든 하이퍼파라미터를 uniformly random하게 탐색하면 안됩니당
  - 히든 유닛 수, 몇 층으로 쌓을 것인지 등을 정할때는 range를 정하고, 그 안에서 Uniformly random하게 그리드 서치해가면서 값을 선택할 수 있음 
  - 하지만, 어떤 값은 이런식으로 선택할 수 없음
    - 예를 들어, $\alpha$ 값을 찾아낼 때는 uniformly random sampling을 하게 되면 1과 0.001이 나올 확률이 동일해짐
    - 이럴 때는 log로 스케일을 바꾸어 앞쪽 구간에서 좀 더 집중적으로 파라미터 탐색을 할 수 있게 만들 수 있음
    - 가령 $r = [1, 4]$으로 두고 1부터 4까지 $r$ 구간에서 동일한 갯수만큼 하이퍼파라미터를 샘플링해본다면,  $10^{-1}$부터 $10^{-2}$ 사이에서 샘플링 되는 갯수랑 $10^{-3}$부터 $10^{-4}$ 사이에서 샘플링 하는 갯수가 똑같게 할 수 있음. 실제 앞쪽의 구간(0.1~0.01)이 뒤쪽 구간(0.001~0.0001) 보다 더 짧으므로 더 촘촘하게 탐색할 수 있음



### 3.1.3. Hyperparameters tuning in practice: Pandas vs. Caviar

- 하이퍼파라미터는 주기적으로 재평가하여 업데이트 해줘야함
- 관리 방법1. Babysitting one model
  - GPU나 CPU등의 자원이 적은 경우. 한 번에 여러 모델을 트레이닝할 여력이 없는 경우 
  - 1가지 모델만 트레이닝 or 아주 작은 수의 모델만 한 번에 트레이닝
  - 하루에 하이퍼파라미터 하나씩 튜닝해가며 몇 일동안 하나의 모델을 갈고 닦음
  - 판다처럼 한 마리만 낳아서 잘 기르기
- 관리방법2. Training many models in parallel
  - 한 번에 다양한 하이퍼파라미터를 가진 모델을 트레이닝시켜 그 중 최선의 퍼포먼스를 가지는 모델 선택
  - 물고기처럼 알 많이 낳고 그 중에서 선택!





## 3.2. Batch Normalization

- 정규화 알고리즘의 발전은 딥러닝에서 매우 중요한 역할을 함! 
- 배치 정규화는 하이퍼파라미터 탐색 문제를 훨씬 쉽게 만들어지고, 신경망을 튼튼하게 해줌

### 3.2.1. Normalizing activations in a network

- 로지스틱 회귀에서 입력값을 normalize하면 학습 속도가 높아진다고 했었음
- 딥러닝 신경망에서는 레이어가 여러개 쌓이면서 activations가 층마다 있으니 $a$의 평균과 표준편차를 이용해 표준화하는 것이 다음층의 $w, b$를 훈련시키는데 도움이 될 것! (보통은 activation func을 지난 후 나오는 값인 $a$가 아니라 그 전 값인 $z$를 노멀라이즈! )
- Batch Norm 과정에서 입력값 x 뿐만 아니라 중간 중간 히든 레이어의 결과물도 노멀라이즈! 
  - 다만 입력값 x를 노멀라이즈 하는 것과 히든레이어의 결과값 z를 노멀라이즈 하는 작업에는 차이가 있음
  - 히든레이어의 유닛을 노멀라이즈해서 평균이 0, 분산이 1이 되게 만들어버리는 것은 적절한 모델로 가는 길이 아닐 수 있음
  - 그러니 $\gamma, \beta$를 이용해서 $z_{norm}^{i}$ 값이 원하느 범위 안에 있게 만들어야 함. 그 결과값을 $\tilde z ^ {i}$라고함



### 3.2.2. Fitting Batch Norm into a neural network

- Batch Norm 을 하지 않는 뉴럴 네트워크에서는...
  - $w^{1}, b^{1}을 통해 x 로부터 z^{[1]} 가 도출$
  - $activation func(z^{[1]}) = a^{[1]}$

- Batch Norm 을 하면
  - $w^{1}, b^{1}을 통해 x 로부터 z^{[1]} 가 도출$
  - $batch normalization(z^{[1]})을 통해 \tilde z^{[1]}이 도출$
  - 이 과정에서 $\beta, \gamma$라는 파라미터가 추가됨





### 3.3. Multi-class classification

### 3.3.1. Softmax Regression

- boundary가 직선
- 