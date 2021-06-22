# 서울시 음식점 추천 웹 페이지

사용자에게 서울시에 있는 음식점을 추천해주는 웹 페이지이다.


### 개발 기간

2021.05 ~ 2021.06



### 기술 스택

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"><img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"><img src="https://img.shields.io/badge/amazon aws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">



### 주요 기능

1. 로그인, 회원가입
2. 음식 검색 기능
3. 음식점 추천 기능
4. 한줄평 기능



### 개발 과정

1. 공공데이터포털에서 서울시 음식점 정보를 가져온 후 AWS RDS로 구축한 데이터베이스에 담는다.
2. Django와 DB 연동 후 User 테이블, 한줄평 테이블 생성.
3. 웹 페이지 UI 제작
4. 추천 질문 선정
4. 카카오맵 API 사용해서 음식점 위치 출력



### 실행 화면

#### 로그인 전 메인화면

![image](https://user-images.githubusercontent.com/57345435/122889301-a2c31a00-d37d-11eb-85db-84de2c9bafb0.png)



#### 로그인 후 메인화면

![image](https://user-images.githubusercontent.com/57345435/122889845-1e24cb80-d37e-11eb-88ce-e3fae3ce48f5.png)



#### 메인화면 - 최근 한줄평

![image](https://user-images.githubusercontent.com/57345435/122890037-4c0a1000-d37e-11eb-8170-a7f7237c4661.png)



#### 메뉴 입력 화면

![image](https://user-images.githubusercontent.com/57345435/122890381-92f80580-d37e-11eb-8bfb-9086b058cd56.png)  



#### 추천 – 질문 화면

![image](https://user-images.githubusercontent.com/57345435/122890455-a73c0280-d37e-11eb-856e-7c6045b4acf8.png)

#### 음식점 추천 화면

![image](https://user-images.githubusercontent.com/57345435/122890677-dce0eb80-d37e-11eb-872b-7533d2b7dd28.png)



#### 음식점 상세 정보 화면 – 현재 위치 및 음식점 정보

![image](https://user-images.githubusercontent.com/57345435/122890849-069a1280-d37f-11eb-8f9a-8980b8b6a64b.png)



#### 음식점 상세 정보 화면 – 한줄평 등록 및 한줄평 보기

![image](https://user-images.githubusercontent.com/57345435/122890993-22051d80-d37f-11eb-8334-8e63404e6a71.png)



### 실행 영상 링크

https://www.youtube.com/watch?v=BpgVBX59RV4
