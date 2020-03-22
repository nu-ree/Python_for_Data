#[Natural Language Processing in TensorFlow](https://www.coursera.org/learn/natural-language-processing-tensorflow/home/welcome)



[1주 차](https://www.coursera.org/learn/natural-language-processing-tensorflow/home/week/1)

### Sentiment in text

(1) Word based encoding

- 각 단어를 인코딩해서 문장을 숫자로 표현 할 수 있다
- 예: I love my dog = 01, 02, 03, 04 / I love my cat = 01, 02, 03, 05

(2) Using APIs 

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ['I love my dog', 'I love my cat']

tokenizer = Tokenizer(num_words = 100) 
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)
# {'i': 1, 'my': 3, 'dog': 4, 'cat': 5, 'love': 2}
```

- 이 예제에선 5개 단어밖에 없어서 상관 없지먄, `num_words=100`으로 설정하면, 상위 100개 단어만 가져와서 인코딩함
- `num_words`단어 수를 적게 설정할수록 훈련 시간이 많이 소요
- 대소문자, 특수문자 등은 상관 없이 인코딩



(3) Text to sequence

```python
sequences = tokenizer.texts_to_sequences(sentences)
print(sequences)
# [[1,2,3,4], [1,2,3,5]]
```

- 모르는 단어가 들어간 문장을 넣으면? 

```python
tokenizer.texts_to_sequences(['I really love my dog'])
print(sequences)
# [1,2,3,4] = I love my dog
```

(4) Looking more at the Tokenizer

- 그럼 모르는 단어는 `<OOV>`라는 토큰으로 만들어서 sequence화 하자 

```python
tokenizer = Tokenizer(num_words = 100, oov_token = '<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)
# {'i': 1, 'my': 3, 'dog': 4, 'cat': 5, 'love': 2, '<OOV>': 6}
tokenizer.texts_to_sequences(['I really love my dog'])
# [1, 6, 2, 3, 4]
```

(5) Padding

- 문장의 단어 수가 서로 다를 때 이를 하나의 메트릭스로 표현할 수가 없음
- `pad_sequences(sequences)`을 이용해서 앞쪽에 공백을 넣어줄 수 있음

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ['I love my dog', 'I love my cat', 'I really love my dog']

tokenizer = Tokenizer(num_words = 100, oov_token = '<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)
# {'i': 1, 'my': 3, 'dog': 4, 'cat': 5, 'love': 2, '<OOV>': 6}
sequences = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequences)
print(sequences)
# [[1, 2, 3, 4], [1, 2, 3, 5], [1, 6, 2, 3, 4]]
print(padded)
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 5], [1, 6, 2, 3, 4]]
```

- `pad_sequences(sequences, padding = 'post')`을 이용해서 뒤쪽에 공백을 넣어줄 수 있음
- `pad_sequences(sequences, maxlen = 5)`을 이용해서 매트릭스의 크기를 설정할 수도 있음 (문장의 앞쪽부터 자름. 뒤부터 자르고 싶으면 `truncating = 'post'` 설정 추가)