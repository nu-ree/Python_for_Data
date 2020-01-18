# Optimization 

### 1 - Gradient Descent

- 머신러닝에서 가장 기본이 되는 최적화 방법. 

- 그래디언트 디센트의 종류

  - 전체 샘플을 한 번에 돌리면 "Batch Gradient Descent"라고 부름
  - 한 샘플씩 돌리면 "Stochastic Gradient Descent"라고 부름

- 그래디언트 디센트에서는 아래와 같은 방법으로 파라미터를 업데이트 함

  $$ W^{[l]} = W^{[l]} - \alpha \text{ } dW^{[l]}$$
  $$ b^{[l]} = b^{[l]} - \alpha \text{ } db^{[l]}$$

- `parameters`($W^{[l]}, b^{[l]}$), `grads`($dW^{[l]}, db^{[l]}$), `learning_rate`($\alpha$)을 입력값으로 받아 최적화 후 `parameters`를 결과값으로 내어야 함

- 파라미터를 업데이트 해나가는 코드로 간단히 표현해보면 아래와 같음

  ```python 
  # updeate parameters!
  L = n_layers
  for l in range(L):
    W[l+1] = W[l+1] - learning_rate*dW[l+1]
    b[l+1] = b[l+1] - learning_rate*db[l+1]
  ```

- 그래디언트 디센트의 전체적인 틀은 아래와 같음

  ```python
  X, y = data
  parameters = init_params(layers_dim)
  for i in range(num_iter):
    # forward prop
    a, caches = forward_prop(X, params)
    # compute cost
    cost +=compute_cost(a, Y)
    #back prop
    grads = back_prop(a, caches)
    #update params
    parameters = update_params(parameters, grads)
  ```

  

### 3 - Momentum

> Momentum takes into account the past gradients to smooth out the update. We will store the 'direction' of the previous gradients in the variable $v$. Formally, this will be the exponentially weighted average of the gradient on previous steps. You can also think of $v$ as the "velocity" of a ball rolling downhill, building up speed (and momentum) according to the direction of the gradient/slope of the hill. 





### 4 - Adam

$$\begin{cases}
v_{W^{[l]}} = \beta_1 v_{W^{[l]}} + (1 - \beta_1) \frac{\partial J }{ \partial W^{[l]} } \\
v^{corrected}_{W^{[l]}} = \frac{v_{W^{[l]}}}{1 - (\beta_1)^t} \\
s_{W^{[l]}} = \beta_2 s_{W^{[l]}} + (1 - \beta_2) (\frac{\partial J }{\partial W^{[l]} })^2 \\
s^{corrected}_{W^{[l]}} = \frac{s_{W^{[l]}}}{1 - (\beta_2)^t} \\
W^{[l]} = W^{[l]} - \alpha \frac{v^{corrected}_{W^{[l]}}}{\sqrt{s^{corrected}_{W^{[l]}}}+\varepsilon}
\end{cases}$$



