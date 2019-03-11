# Flask & Vue.js for Data Dashborad & Admin Tool Development

## Tutorial Source
- <a href = "https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/"> Developing a Single Page App with Flask and Vue.js </a> 를 보고 따라하며 정리한 마크다운입니다.

- 윈도우 환경에서 실행하면서 수정해야 할 부분은 수정하면서 진행하였습니다. 




## Step1. 
1) 튜토리얼을 위한 새로운 폴더를 만들고
2) 그 안에서 파이썬 가상환경을 활성화 한다(윈도우와 우분투의 방법 다름. 위 블로그에는 우분투 사용)
3) Flask가 없으면 설치한다.
3) app.py 소스 파일 만들어서 실행해보면, http://localhost:5000/ping. 화면에 "pong!" 이라는 텍스트 반환

<pre><code>
$ mkdir flask-vue-crud
$ cd flask-vue-crud
$ python3 -m venv tutorial-env
$ tutorial-env\Scripts\activate.bat # for Window -- https://docs.python.org/ko/3/tutorial/venv.html
$ source tutorial-env/bin/activate # for Ubuntu
(tutorial-env)$ pip install Flask==1.0.2 Flask-Cors==3.0.4
(tutorial-env)$ python app.py</code></pre>



## Step 2. 

4) npm을 처음 쓰는 경우, https://nodejs.org/en/download/ 에서 다운 받는다

5) vue client를 설치한다(dnl tkdlxmdpsms $ npm install -g vue-cli@2.9.3라고 되어있지만 버전이 최신이 아니어서 그런지 프로젝트 명 설정에서 더이상 넘어가지 않아 다시 새로운 버전으로 설치히하고 문제 해결!)

<a href = "https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#using-a-node-version-manager-to-install-node-js-and-npm"> npm  설치 관련 참고 사이트 </a>

<pre><code>
$ npm -v
$ npm install -g vue-cli
$ npm install -g @vue/cli-init
</code></pre>



6) flask-vue-crud 폴더 안에서 Vue 프로젝트를 시작하는 아래 코드를 실행한다

<pre><code>
$ vue init webpack client
</pre></code>

7) 처음 세 질문에는 엔터를 쳐서 디폴트 값으로 설정한다. 그 다음 질문에는 아래와 같이 설정한다. 

- y, n 또는 화살표로 선택하고 엔터

1. Vue build: `Runtime + Compiler`
2. Install vue-router?: `Yes`
3. Use ESLint to lint your code?: `Yes`
4. Pick an ESLint preset: `Airbnb`
5. Set up unit tests: `No`
6. Setup e2e tests with Nightwatch: `No`
7. Should we run npm install for you after the project has been created: `Yes, use NPM`

![1552322503850](C:\Users\nrchu\AppData\Roaming\Typora\typora-user-images\1552322503850.png)



