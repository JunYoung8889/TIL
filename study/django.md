# Django

- MTV
- Variable Routing
- Django template path
- Django Template Language
- Form tag with Django
- 로또 함수 만들기
- Model
- Django Model Field
- Django project
- ORM





---

### MTV

- Django는 MTV 디자인 패턴으로 이루어진 Web Framework 이다.
- MTV
  - Model Template View
- MVC
  - Model View Controller
- Model : Model
  - 응용프로그램의 데이터구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- View : Template
  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는 데 사용 (presentation)
  - Django는 Templates 폴더에 html들이 있다. 
- Controller : View
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김
  - 요청에따라 로직을 수행하며, 결과를 템플릿으로 렌더링하여 응답한다.



---

### Variable Routing

- Variable Routing 은 Django 에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다.



---

### Django template path

- Django 프로젝트는 render할 templates 파일들을 찾을 때, 기본적으로 settings.py의 INSTALLED_APPS에 등록된 각 앱폴더 안의 templates 폴더 내부를 탐색한다.
- 해당 templates 폴더는 자동으로 생성되는 것이 아니며, 따로 만들어 주어야 한다.



---

### Django Template Language

- forloop.counter0 / forloop.counter

  - ```html
    {% for man in mans %}
    	<p>{{ forloop.counter0 }}번 사람 : {{ man }}</p>
    {% endfor %}
    ```

- empty

  - ```html
    {% for man in mans %}
    	<p>{{ forloop.counter0 }}번 사람 : {{ man }}</p>
    {% empty %}
    	<p>현재 사람이 없습니다.</p>
    {% endfor %}
    ```

- forloop.first / if / else

  - ```html
    {% for man in mans %}
    	{% if forloop.first %}
    		<p>첫 번째 사람 입니다.</p>
    	{% else %}
    		<p>첫 번째 사람이 아닙니다.</p>
    	{% endif %}
    	<p>{{ forloop.counter0 }}번 사람 : {{ man }}</p>
    {% empty %}
    	<p>현재 사람이 없습니다.</p>
    {% endfor %}
    ```

- length / title

  - ```html
    <p>{{ 'man'|length }}</p>
    <p>{{ 'hello world'|title }}</p>
    ```

  - ```
    5
    Hello World
    ```

- 날짜 형식

  - https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#date

  - ```html
    # 2022년 03월 07일 (Mon) AM 03:30
    {{ releasedate|date:"Y년 m월 d일 (D) A h:i" }}
    # 22년 3월 7일 (Monday) a.m. 03:30
    {{ releasedate|date:"y년 n월 j일 (l) a h:i" }}
    ```



---

### Form tag with Django

- action

  - form 이 제출될 때, 처리가 필요한 데이터를 전달받는 곳의 url 주소이다.
  - 만약, 설정이 안되어 있거나 빈 문자열로 설정된다면 폼은 현재 페이지 url로 다시 제출된다.

- method

  - POST

    - 사이트간 요청 해킹에 저항성이 좋게 만들어 줄 수 있기 때문에 서버 데이터베이스가 변경될 경우에는 항상 사용 되어야 한다. 회원가입이나 결제와 같은 경우에 사용한다.

    - ```html
      <form action="{% url 'articles:create' %}" method="POST">
          {% csrf_token %}
      ```

  - GET

    - 사용자 데이터를 변경하지 않는 폼에서만 사용된다.
    - url을 북마크하길 원하거나 공유하기 원하는 경우에 사용된다.

- 쿼리

  - input 태크 name="title" name="content" name="my-site"
  - http://127.0.0.1:8000/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅



---

### 로또 함수 만들기

- ```python
  from multiprocessing import context
  from django.shortcuts import render
  import random
  
  # Create your views here.
  def lotto(request):
      numbers = random.sample(range(1,46), 6)
      numbers.sort()
      context = {
          'numbers' : numbers,
      }
      return render(request, 'lotto.html', context)
  ```

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1>제 1004회 로또 번호 추천</h1>
    <p>회원님께서 선택하신 로또 번호는 {{ numbers }}입니다.</p>
  </body>
  </html>
  ```



---

### Model

- migrations : Django가 Model 에 생긴 변화를 DB에 반영하는 방법

- migrate : Model의 변경사항을 저장하기 위한 명령어

- sqlmigrate <app_name> <table_num> : 생성된 마이그레이션 파일에 대응되는 SQL 문을 확인하기 위한 명령어

- ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  $ python manage.py runserver
  
  
  $ python manage.py sqlmigrate articles 0001
  $ python manage.py showmigrations
  
  
  $ python manage.py createsuperuser
  ```

- python shell

  - Django에서 사용가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때
  - `$ python manage.py shell_plus` 명령어를 통해 해당 Shell을 실행 할 수 있다.
  - 'django_extensions', 를 settings.py의 INSTALLED_APPS 에 추가해 주어야 한다.



---

### Django Model Field

- CharField : 짧은 문자열을 정의할때 사용, max_length 를 지정해 주어야 한다. ex) max_length=10
- TextField :  긴 문자를 정의할때 사용. 
- DateField/DateTimeField : 날짜/ 날짜,시간 정보를 정의할때 사용. 
- IntegerField : 정수값을 정의할때 사용.
- EmailField : 이메일 주소를 정의 할때 사용.
- FileField / ImageField : 파일 및 이미지 업로드를 위해서 사용.
- AutoField : 자동으로 증가하는 IntegerField 이며, primary key 가 정의되지 않으면 자동으로 테이블에 추가되서 primary key 로 사용된다.
- ForeignKey : 다른테이블과의 관계에서 일-대-다 관계를 정의한다.
- ManyToManyField : 다른테이블 과의 관계에서 다-대-다 관계를 정의한다.





---

### Django project

- ```bash
  $ python -m venv venv
  $ source venv/Scripts/activate
  $ pip list
  $ pip install django==3.2.12
  
  
  $ django-admin startproject crud
  $ python manage.py startapp articles
  ```

- crud

  - crud

    - `__init__.py`

      - crud 디렉토리를 패키지로 인식시켜준다.

    - asgi.py

      - 웹서버와 연결 및 소통을 도와준다. / 비동기식

    - wsgi.py

      - 웹서버와 연결 및 소통을 도와준다.

    - urls.py

      - ```python
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('articles.urls')),
        ]
        ```

      - 사이트의 url과 적절한 views의 연결을 지정한다.

    - settings.py

      - 애플리케이션의 모든 설정을 포함한다.

      - ```python
        INSTALLED_APPS = [
            'articles',
            'django_extensions',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
        ```

      - 생성된 앱 이름을 INSTALLED_APPS 에 등록해야한다.

      - django_extensions 는 `$ python manage.py shell_plus`를 실행하기 위해서 등록한다.

      - ```python
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR,'templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```

      - Django는 기본적으로 앱 안에 있는 templates를 인식하는데  html 들의 공통사항이 많아서 스켈레톤 html로 base.html을 생성하고 싶을 때는 crud, articles, manage.py와 같은 선상에 있는 templates에 base.html을 생성하는데 이때 이를 인식하기 위해서는 settings.py의 TEMPLATES의 DIRS를 [Base_DIR, 'templates']로 수정해야한다. 

      - ```python
        LANGUAGE_CODE = 'en-us'
        
        TIME_ZONE = 'UTC'
        
        USE_I18N = True
        
        USE_L10N = True
        
        USE_TZ = True
        ```

      - django 프로젝트를 한국어로 제공하기 위해 번역이 필요하다. 이 설정을 위해 LANGUAGE_CODE 변수에 'ko-kr'을 할당해야 한다.

      - 이때 USE_I18N = True  로 활성화인 상태여야 해당 설정이 가능하다.

      - USE_I18N : internationalization (국제화)

      - USE_L10N : localization (현지화)

      - 서울 시간 기준으로 표기하고 싶다면 TIME_ZONE 변수에 'Asia/Seoul'을 할당해야 한다.

      - ```python
        LANGUAGE_CODE = 'en-us'
        
        TIME_ZONE = 'UTC'
        
        # March 20, 2022, 6:23 a.m.
        ```

      - ```python
        LANGUAGE_CODE = 'ko-kr'
        
        TIME_ZONE = 'UTC'
        
        # 2022년 3월 20일 6:22 오전
        ```

      - ```python
        LANGUAGE_CODE = 'en-us'
        
        TIME_ZONE = 'Asia/Seoul'
        
        # March 20, 2022, 3:24 p.m
        ```

      - ```python
        LANGUAGE_CODE = 'ko-kr'
        
        TIME_ZONE = 'Asia/Seoul'
        
        # 2022년 3월 20일 3:26 오후
        ```

  - manage.py

    - 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

    - ```bash
      $ python manage.py <command> [options]
      ```

  - templates (자동으로 생성 안됨)

    - base.html

      - ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
          <title>Document</title>
        </head>
        <body>
          {% block content %}
          {% endblock content %}
        </body>
        </html>
        ```

  - articles

    - migrations

    - `__init__.py`

      - 디렉토리를 패키지로 인식시켜준다.

    - apps.py

      - 앱의 정보가 작성되는 곳

    - tests.py

      - 프로젝트의 테스트 코드를 작성하는 곳

    - admin.py

      - ```python
        from django.contrib import admin
        from .models import Article
        
        class ArticleAdmin(admin.ModelAdmin):
            list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
        
        admin.site.register(Article, ArticleAdmin) 
        ```

      - 관리자용 페이지를 설정하는 곳

      - ```bash
        $ python manage.py createsuperuser
        ```

      - 관리자용 아이디를 생성 name, email, password

    - models.py

      - ```python
        from django.db import models
        
        # Create your models here.
        class Article(models.Model):
            title = models.CharField(max_length=10)
            content = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
        ```

      - 모델을 정의하는 곳

      - 응용프로그램의 데이터 구조를 정희하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)

    - views.py

      - view 함수들이 정의되는 곳

      - 요청에따라 로직을 수행하며, 결과를 템플릿으로 렌더링하여 응답한다.

      - ```python
        from django.shortcuts import render, redirect
        from .models import Article
        
        def index(request):
            # articles = Article.objects.all()[::-1]
            articles = Article.objects.order_by('-pk')
            context = {
                'articles' : articles,
            }
            return render(request, 'articles/index.html', context)
        
        
        def new(request):
            return render(request, 'articles/new.html')
        
        
        def create(request):
            title = request.POST.get('title')
            content = request.POST.get('content')
            # 1.
            # article = Article()
            # article.title = title
            # article.content = content
            # article.save()
        
            # 2.
            article = Article(title=title, content=content)
            article.save()
        
            # 3.
            # Article.objects.create(title=title, content=content)
        
            return redirect('articles:detail', article.title)
            # return redirect('articles:index')
            # return render(request, 'articles/index.html')
            # redirect안에는 request, context 안들어감 
                #  오직, app_name:url_name_space
        
        
        def detail(request, title):
            articles = Article.objects.filter(title=title)
            context = {
                'articles' : articles,
            }
            return render(request, 'articles/detail.html', context)
        
        
        def delete(request, pk):
            article = Article.objects.get(pk=pk)
            if request.method == 'POST':
                article.delete()
                return redirect('articles:index')
            else: #GET
                return redirect('articles:detail', article.pk)
        
        
        def edit(request, pk):
            article = Article.objects.get(pk=pk)
            context = {
                'article' : article,
            }
            return render(request, 'articles/edit.html', context)
        
        
        def update(request, pk):
            article = Article.objects.get(pk=pk)
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.save()
            return redirect('articles:detail', article.title)
        ```

    - urls.py ( 자동으로 생성 안됨 )

      - 사이트의 url과 적절한 views의 연결을 지정한다.

      - ```python
        from django.urls import path
        from . import views
        
        app_name = 'articles'
        
        urlpatterns = [
            path('', views.index, name='index'),
            path('new/', views.new, name='new'),
            path('create/', views.create, name='create'),
            path('<str:title>/', views.detail, name='detail'),
            path('<int:pk>/delete/', views.delete, name='delete'),
            path('<int:pk>/edit/', views.edit, name='edit'),
            path('<int:pk>/update/', views.update, name='update'),
        ]
        ```

    - templates ( 자동으로 생성 안됨 )

      - articles

        - index.html

          - ```html
            {% extends 'base.html' %}
            
            {% block content %}
              {% for article in articles %}
                <p>제목 : {{ article.title }}</p>
                <p>내용 : {{ article.content }}</p>
                <hr>
              {% endfor %}
            {% endblock content %}
            ```

        - new.html

          - ```html
            <form action="{% url 'articles:create' %}" method="POST">
                {% csrf_token %}
            ```





---

### ORM

- Object Relational Mapping
  - 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django-SQL)데이터를 변환하는 프로그래밍 기술
  - OOP프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- RDBMS의 개념적 정의
  - Relational Database Management System
  - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
- RDBMS를 기반으로 한 DB Engine 의 종류
  - MySQL
  - SQLite
  - PostgreSQL
  - ORACLE
  - MS SQL