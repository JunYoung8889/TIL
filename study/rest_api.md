# REST API

### HTTP

- ```
  HyperText Transfer Protocol
  웹 상에서 컨텐츠를 전송하기 위한 약속
  리소스들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
  REST의 정보의 자원은 URI로 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.
  HTTP method는 GET, POST, PUT, DELETE가 있다.
  ```

- ```
  HTTP response status codes
  200 - OK, 요청이 성공적으로 완료되었다는 의미로 정보는 요청에 따른 응답으로 반환처리 된다.
  400 - Bad Request, 잘못된 문법으로 인해 서버가 요청을 이해할 수 없음을 의미한다.
  401 - Unauthorized, 비인증, 클라이언트는 반드시 스스로를 인증해야 한다.
  403 - Forbidden, 클라이언트가 접근할 권리를 가지고 있지 않다는것이다.
  404 - Not Found, 알려지지 않은 URL, 리소스를 찾을 수 없음을 의미한다.
  500 - Internal Server Error, 서버의 문제가 있음을 의미
  ```

- ```
  URI Uniform Resource Identifier 통합 자원 식별자
  인터넷 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열, 일반적으로 URL
  URL Uniform Resource Locator 통합 자원 위치
  과거 실제 자원의 위치 / 현재 추상화된 의미론적인 구성
  웹주소, 링크
  URN Uniform Resource Name 통합 자원 이름
  위치에 영향을 받지 않는 유일한 이름
  ```

- ```
  URI 구조
  Schema (protocol) - 프로토콜, http(s)
  Host (Domain name) - 서버이름, IP주소
  Port - 리소스 접근 gate / HTTP 80 / HTTPS 443
  Path - 리소스 경로
  Query (Identifier) - 추가적인 매개변수
  Fragment - 부분 식별자, 북마크의 한 종류
  ```

---

### RESTful API

- ```
  API Application Programming Interface
  프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  프로그래밍을 통해 특정한 기능을 수행
  HTML, XML, JSON등으로 응답
  ```

- ```
  REST REpresentational State Transfer
  API Server를 개발하기 위한 소프트웨어 설계 방법론
  자원 - URI
  행위 - HTTP Method
  표현 - 추상화된 결과물, JSON으로 표현된 데이터를 제공
  ```

- ```
  RESTful API
  REST 원리를 따라 설계한 API
  프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성
  ```

---

### Response

- ```
  Serialization 직렬화
  데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고
  나중에 재구성할 수 있는 포맷으로 변환하는 과정이다.
  Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로
  쉽게 변환할 수 있는 Python 데이터 타입으로 만들어준다.
  ```

- JsonResponse 객체를 활용한 JSON 데이터 응답

  - ```python
    # articles/views.py
    
    from django.http.response import JsonResponse
    
    def article_json_1(request):
        articles = Article.objects.all()
        articles_json = []
        for article in articles:
            articles_json.append(
            	{
                    'id' : article.pk,
                    'title' : article.title,
                    'content' : article.content,
                    'created_at' : article.created_at,
                    'updated_at' : article.updated_at,
                }
            )
        return JsonResponse(articles_json, safe=False)
    ```

  - dict 이외의 객체를 직렬화(Serialization)하려면 safe=False로 설정해야 함

  - 필드를 개별적으로 직접 만들어 주어야 함

- Django의 내장 HttpResponse를 활용한 JSON 응답

  - ```python
    # articles/views.py
    
    from django.http.response import HttpResponse
    from django.core import serializers
    
    def article_json_2(request):
        articles = Article.objects.all()
        data = serializers.serialize('json', articles)
        return HttpResponse(data, content_type='application/json')
    ```
    
  - 주어진 모델 정보를 활용하기 때문에 필드를 개별적으로 직접 만들어 줄 필요 없음

- DRF Django REST Framework 라이브러리를 사용한 JSON 응답

  - ```python
    # articles/serializers.py
    
    from rest_framework import serializers
    from .models import Article
    
    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Articcle
            fields = '__all__'
    ```

  - ```python
    # articles/views.py
    
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from .serializers import ArticleSerializer
    
    # @api_view() 기본적으로 GET
    @api_view(['GET'])
    def article_json_3(request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    ```

---

### DRF

- Postman

  - ```
    API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼
    설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성 할 수 있도록 도움
    ```

  - ```
    DRF 가 제공하는 기본 Form 뿐만 아니라
    Postman을 통해서도 HTTP Method를 테스트 해볼 수 있다.
    ```

- api_view

  - ```
    @api_view() 기본적으로 GET
    @api_view(['GET', 'POST', 'PUT', 'DELETE']) 사용할 HTTP Method를 리스트 형식으로 목록화
    DRF에서는 데코레이터가 선택이 아닌 필수적으로 작성해야 view 함수가 정상적으로 작동한다.
    ```



