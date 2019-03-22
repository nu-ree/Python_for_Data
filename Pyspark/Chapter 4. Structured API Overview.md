# Chapter 4. Structured API Overview 

**Structured API란?**

- 비구조화된 데이터부터 구조화된 데이터까지 모든 데이터 형태를 manipulating 하는 툴

- Datasets, DataFrames, SQL table and view 등이 있음
- *batch computation*과 *streaming computation*에 사용.
- 

the typed APIs vs. untyped APIs

스파크는 어떻게 내가 쓰는 Structured API를 받아서 클러스터에 일을 던져줄까? 

스파크에는 structured collections에는 두 가지가 있음

- structured collections: DataFrames and
  Datasets



**Schema**

- DF의 column name과 type를 정의함

- 직접 정하거나 데이터에서 알아내거나(일명 *schema on read*)



- Spark uses an engine called
  Catalyst that maintains its own type information through the planning and processing of work.
- 겉으론 파이썬을 써도 속에서 돌아가는거는 Spark Type!



- DATAFRAME
- Datasets?



`spark.range(2).collect() # row 2개를 array 형태의 collection으로 보여줌`

