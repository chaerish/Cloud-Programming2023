# Cloud-Programming2023
☁️클라우드 프로그래밍 깃헙 저장소☁️

## 사용언어

## 주차별 학습 내용
### 1주차
- 웹 페이지 동작구조
  - MTV(model-view-template)
  - 사용자 요청-> url.py -> view.py -> model.py 
- django 환경설정 
  - 서버 실행: python manage.py runserver
- migration 이란? : 데이터 베이스를 업데이트 할 때마다 make migration 진행 
- #### POST 모델 구현 
* * *
### 2주차
- url.py: 사용자의 요청에서 url 패턴에 맞는 요청을 찾아 수행할 작업(views.py) 를 찾아줌
  - ex) path('admin/', admin.site.urls),
- FBV: 함수 기반 뷰
- CBV: 클래스 기반 뷰
- #### 블로그 페이지에 포스트 목록 추가 
  - Post.object.all() : 모든 Post 를 가져옴 
  - html 템플릿 문법: {{}}
- #### 포스트 목록 순서 수정
  - order_by('-pk') : 역순정렬
- #### FBV로 포스트 상세 페이지 정의하기
  - 글 목록에 해당되는 글로 이동하기 
  - html에서 상세 글로 이동하는 함수 추가 
- #### CBV로 포스트 목록 페이지 만들기: ListView
- #### 포스트 상세 페이지 만들기: DetailView 
  - DetailView 는 모델명_detail.html 을 템플릿으로 인지한다.
* * *
### 3주차 
- #### static (정적) 파일 관리 
- #### 이미지 업로드하기 
- #### 미디어 파일 관리하기
  - setting.py에서 업로드한 파일이 지정될 폴더 지정
  - pip install Pillow : 파이썬에서 이미지 처리를 위해 필요함.
  - 이미지 파일을 위한 URl 처리
  ```
  urlpatterns =static(..)
  ```
- #### 템플릿 필터 사용하기
  ```
  {%if p. head_image%}
  ..
  {else}
  ```
- #### 페이지 구성 모듈화 
