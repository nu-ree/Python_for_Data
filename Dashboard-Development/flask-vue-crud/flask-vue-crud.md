# Flask & Vue.js for Data Dashborad & Admin Tool Development

## Tutorial Source
<a href = "https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/"> Developing a Single Page App with Flask and Vue.js </a> 를 보고 따라하며 정리한 마크다운입니다.



##Step1. 
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

$ pip install Flask==1.0.2 Flask-Cors==3.0.4
(tutorial-env)$ pip install Flask==1.0.2 Flask-Cors==3.0.4
(tutorial-env)$ python app.py
</code></pre>

	
<pre><code>
$ npm install -g vue-cli@2.9.3
</code></pre>

	4) npm을 처음 쓰는 경우, https://nodejs.org/en/download/ 에서 다운 받는다

