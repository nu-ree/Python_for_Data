# Part I. Gentle Overview of Big Data and Spark

## Chapter 1. Apache Spark

### What is Spark? 
- Unified (no need to stitch multiple APIs and Systems to do parallel data processing)
  - 1) 새로운 라이브러리 / 기존 라이브러리을 잘 조합해줌
  - 2) Structured API (DF, Dsets SQL)
- Coumputing Engine (not a storage)
  - 클라우드 저장 시스템,분산파일시스템,메시지 버스 등과 잘 연동.
  - 데이터가 어디 있건 여러 저장소에 있는 데이터를 메모리에 올려서 돌아가게 할 수 있음
  - 하둡은 저장 시스템 + 분산처리시스템을 조합했지만 
  - 스파크는 저장 시스템과 분산처리시스템을 분리함. 
- Libraries for data analytics (MLib, GraphX, Spark SQL etc.)



### Key factors
- Structured APIs
- Advanced Analytics
- Libraries & Ecosystem
- Structured APIs (Datasets, DataFrames, SQL)
- Low-level APIs (RDDs, Distributed Variables)



### History

- 맵리듀스 엔진은 large application을 만드는 것이 어렵고 비효율적임. 가령 모델을 병렬처리할 때 데이터를 밑에서부터 끌고 올라와야 함
- 반면 스파크는 데이터를 손에 들고 있어서 
- SQL로도 쿼리 가능

> *Over time, the project added a plethora of new APIs that build on this more powerful structured foundation, including DataFrames, machine learning pipelines, and Structured Streaming, a high-level, automatically optimized streaming API.*



## Chapter 2. A Gentle Introduction to Spark
### Spark’s Basic Architecture
- 데이터 처리는 하나의 컴퓨터로 감당하기 어려운 작업
- 여러 컴퓨터를 클러스터로 구성하여 마치 하나의 컴퓨터로 사용할 수 있게 해줌
- 스파크는 클러스터 안에 있는 컴퓨터에 데이터 관련 task execution을 던지는 일을 **managing**하고 **coordinating**함

### Spark Application
- 기본적으로 a driver process와 일련의 executor processes로 구성
