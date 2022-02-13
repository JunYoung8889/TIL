# Web

- HTML
- CSS
- 반응형 웹

---

### HTML

- Hyper Text Markup Language
- 하이퍼 텍스트
  - 하이퍼링크를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language
  - 태그등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 웹표준
  - W3C
  - WHATWG
- DOM( Document Object Model ) 
  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

---

### HTML 문서의 기본구조

- !엔터 눌렀을때 나오는거 정리하기

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Hello, HTML</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="test.css">
      <script src="javascript.js"></script>
      <style>
          p {
              color: black;
          }
      </style>
  </head>
  <body>
      <h1> 웹문서 </h1>
      <ul>
          <li>HTML</li>
          <li>CSS</li>
      </ul>
  </body>
  </html>
  ```

- `<html>` : 문서의 최상위 요소

- `<head>` : 문서 메타데이터 요소

  - 제목, 인코딩, 스타일, 외부 파일 로딩 등

- `<body>` : 문서 본문 요소

  - 실제 화면 구성과 관련된 내용

- `<link>` : 외부 리소스 연결(CSS, favicon 등등)

- `<script>` : 스크립트 요소 (JavaScript 파일/코드)

- `<style>`: CSS 직접 작성

---

### 태그

- 내용이 없는 태그들

  - br, hr, img, input, link, meta

- 요소는 중첩(nested)될 수 있음

- 태그 속성(attribute)

  - 태그 속성 쓸때, 공백 사용X, ""쌍따옴표 사용
  - 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
  - 보통 이름과 값이 하나의 쌍으로 존재 / 속성이름=속성값
  - 태그별로 사용할 수 있는 속성은 다르다.
  - 태그와 상관없이 사용가능한 속성(HTML Global Attribute)들도 있음
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스의 목록
    - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style : 인라인 스타일 지정
    - title : 요소에 대한 추가 정보 지정
    - tabindex : 요소의 탭 순서
    - queryid, role

- 태그

  - ```html
    <h1></h1>
    <P></P>
    <span></span>
    <a href="https://www.naver.com">네이버로 이동!</a>
    <div></div>
    ```

---

### 시멘틱 태그

- ```html
  <header></header>
  <nav></nav>
  <aside></aside>
  <section>
      <article></article>
  </section>
  <footer></footer>
  ```

- header : 문서 전체나 섹션의 해더(머리말 부분)

- nav : 내비게이션

- aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
- section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
- article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
- footer : 문서 전체나 섹션의 푸터(마지막 부분)
- div랑 기능자체는 같으나 영역을 의미로 구분 의미론적 요소를 담음
- h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함

- Non semantic 요소
  - div, span

---

### 텍스트 요소

- ```html
  <a></a>
  <b></b>
  <strong></strong>
  <i></i>
  <em></em>
  <br>
  <img>
  <span></span>
  ```

- a : href 속성을 활용하여 다른 URL로 연견하는 하이퍼링크 생성
- b : 굵은 글씨 요소
- strong : 중요한 강조하고자 하는 요소 (굵은 글씨)
- i : 기울임
- em : 중요한 강조하고자 하는 요소 (기울임)
- br : 텍스트 내에 줄바꿈 생성
- img : src 속성을 활용하여 이미지 표현
- span : 의미 없는 인라인 컨테이너

---

### 그룹 컨텐츠

- ```html
  <p></p>
  <hr>
  <ol></ol>
  <ul></ul>
  <pre></pre>
  <blockquote></blockquote>
  <div></div>
  ```

- p : 하나의 문단
- hr : 수평선, 문단 요소 주제의 분리를 의미
- ol : 순서가 있는 리스트
  - 1.
- ul : 순서가 없는 리스트
  - •
- pre : 작성 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지
- blockquote : 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨
- div : 의미 없는 블록 레벨 컨테이너

---

### table

- table
  - thead
    - tr > th
  - tbody
    - tr > td
  - tfoot
    - tr > td
    - td colsapn="2"
  - caption

---

### form

- form

  - action : form을 처리할 서버의 URL / "", "#" 어디로 보내야할지 안정했으면
  - method : form을 제출할 때 사용할 HTTP 메서드 / GET 혹은 POST
  - enctype : method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded : 기본값
    - multipart/form-data : 파일 전송시 (input type이 file인 경우)

- input

  - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)

  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)

  - required, readonly, autofocus, autocomplete, disabled 등

  - ```html
    <form action="/search" method="GET">
        <input type="text" name="q">
    </form>
    ```

  - https://www.google.com/search?q=방탄소년단

  - q : 쿼리

  - input label

    - ```html
      <label for="agreement">개인정보 수집에 동의합니다.</label>
      <input type="checkbox" name="agreement" id="agreement">

  - type
    - text, checkbox, submit, password, email, number(min, max, step), file, radio
    - checkbox 다중 선택
    - radio 단일 선택
    - color : color picker
    - date : date picker
    - hidden : 사용자에게 보이지 않는 input

- 설문조사

  - ```html
    <img src="images/ssafy.png" alt="main img" width="300">
    <form action="#">
        <div>
            <label for="name">이름</label><br>
            <input type="text" id="name" name="name" autofocus>
        </div>
        <div>
            <label for="location">지역</label><br>
            <select name="location" id="location" required>
                <option value="">선택</option>
                <option value="서울">서울</option>
                <option value="강원" disabled>강원</option>
            </select>
        </div>
        <div>
            <p>체온</p>
            <input type="radio" name="heat" id="normal" value="normal" checked>
            <label for="normal">37도 미만</label><br>
            <input type="radio" name="heat" id="warning" value="warning" checked>
            <label for="warning">37도 이상</label><br>
        </div>
        <input type="submit" value="제출">
    </form>
    ```

---

### CSS

- Cascading Style Sheets

- 스타일을 지정하기 위한 언어

- 선택하고, 스타일을 지정한다.

- ```css
  h1 {
      color: blue;
      font-size: 15px;
  }
  ```

- 선택자, 선언, 속성, 값

- 선택자 : 요소를 선택

- 선언 : 속성: 값; 쌍으로 선언을 진행

- 속성 : 어떤 스타일 기능을 변경할지 결정

- 값 : 어떻게 스타일 기능을 변경할지 결정

---

### CSS 정의 방법

- 인라인(inline)

- 내부참조
  - head 에 style태그
- 외부 참조
  - 분리된 CSS 파일
  - head 에 link 태그 
  - link rel="stylesheet" href="test.css"

---

### 선택자

- 기본 선택자

  - 전체 선택자
    - *

  - 요소 선택자
    - h2
    - p

  - 클래스 선택자
    - .class

  - 아이디 선택자
    - #id
    - 하나의 문서에 1번만, 단일 아이디 사용 권장

  - 속성 선택자

- 결합자
  - 자손 결합자
    - div p
  - 자식 결합자
    - div > p
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

---

### CSS 우선순위

- `!important`

- 인라인
- id
- class, 속성, pseudo-class(의사-클래스)
- 요소, pseudo-element(의사 엘리먼트)
- CSS 파일 로딩 순서
  - CSS 파일 내에 선언 순서 .blue .green green 우선

---

### CSS 상속

- 상속 되는것
  - Text 관련 요소(font, color, text-align), opacity, visibility 등

- 상속 되지 않는 것
  - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
  - position 관련 요소(position, top/right/bottom/left, z-index) 등

---

### 크기단위

- px : 픽셀 기준, 고정적인 단위
- % : 백분율 단위, 가변적인 레이아웃에서 자주 사용
- em 
  - 바로 위, 부모 요소에 대한 상속의 영향을 받음
  - 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - 바로 위, 부모 요소에 대한 상속의 영향을 받지 않음
  - 최상위 요소(html 디폴트 16px)의 사이즈를 기준으로 배수 단위를 가짐

- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax
    - Viewport Width / Viewport Height
    - 1vw : Viewport 기준 1%
    - vmin은 vw와 vh 중 더 작은 것을 적용하고, vmax는 vw와 vh 중 더 큰 것을 적용합니다.
    - 1200px*600px의 뷰포트가 있습니다. 계산하면 `1vw = 12px` / `1vh = 6px`이 됩니다. 
    - `1vmin = 1vh = 6px`으로 계산됩니다. `1vmax = 1vw = 12px`이 됩니다.
    - 500px*900px로 바뀌었다고 해볼게요. `1vw = 5px` / `1vh = 9px`
    - `1vmin = 1vw = 5px` / `1vmax = 1vh = 9px`가 됩니다.

---

### 색상

- 대소문자를 구분하지 않음
- red, blue black과 같은 특정 색을 직접 글자로 나타냄
- RGB색상
  - 16진수 표기법 혹은 함수형 rgb(0,0,0)표기법을 사용해서 특정 색을 표현하는 방식
  - 특정 색  RGB
  - 빨강
    - color: red;
    - color: rgb(255,0,0);
    - color: rgb(100%,0%,0%);
    - color: #FF0000;

- |      색상       |     RGB     |      색상      |      RGB      |
  | :-------------: | :---------: | :------------: | :-----------: |
  |      빨강       |  (255,0,0)  | 마젠타 /자홍색 |  (255,0,255)  |
  |      노랑       | (255,255,0) |      흰색      | (255,255,255) |
  |      라임       |  (0,255,0)  |     검정색     |    (0,0,0)    |
  |      파랑       |  (0,0,255)  |      초록      |   (0,128,0)   |
  | 청록색 / 아쿠아 | (0,255,255) |      보라      |  (128,0,128)  |

- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
- a는 alpha(투명도)
- 검정
  - color: black;
  - color: #000;
  - color: #000000;
  - color: rgb(0, 0, 0);
  - color: rgb(0%, 0%, 0%);
  - color: hsl(120, 100%, 0);
  - color: rgba(0, 0, 0, 0.5);
  - color: hsla(120, 100%, 0.5);

- color, background-color, background-image

---

### 결합자

- 자손 결합자

  - selectorA 하위의 모든 selectorB 요소

  - ```css
    div span {
        color: red;
    }
    ```

- 자식 결합자

  - selectorA 바로 아래의 selectorB 요소

  - ```css
    div > span {
        color: red;
    }
    ```

- 일반 형제 결합자

  - selectorA 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

  - ```css
    p ~ span {
        color: red;
    }
    ```

- 인접 형제 결합자

  - selectorA 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

  - ```css
    p + span {
        color: red;
    }
    ```

---

### CSS Box model

- margin - border - padding - content
- 요소에 적용된 배경색은 padding까지 적용됨
- margin은 배경색 지정할 수 없다.
- margin
  - margin-top
  - margin-right
  - margin-bottom
  - margin-left
  - margin: 1px;  << 상하좌우 1px 적용
  - margin: 1px 2px; << 상하 1px 좌우 2px
  - margin: 1px auto 2px; << 상 1px, 좌우 자동으로 양쪽 마진 맞춰서 컨탠츠가 가운데 오도록해줌, 하 2px
  - margin: 1px 2px 3px 4px; << 상 1px 우 2px 하 3px 좌 4px  / 시계방향 기억하기

- border
  - border-width: 2px;
  - border-style: dashed;
    - border-style: dotted;
    - border-style: solid;
    - border-style: double;
    - border-style: groove;
    - border-style: ridge;
    - border-style: inset;
    - border-style: outset;
    - border-style: none;
    - border-style: hidden;
    - border-style: dotted dashed solid double;  상 우 하 좌 시계방향
  - border-color: black;
  -  border: 5px solid red; 단축형 속성 shorthand
- background-color: bueviolet;
- box-sizing
  - box-sizing: content-box;
    - padding을 제외한 순수 contents 영역만을 box로 지정
  - box-sizing: border-box;
    - border까지의 전체 너비를 width: 100px; 로 지정
    - 원래 전체 너비는 `width + padding*2 + border-widht*2` 142px

---

### CSS display

- 인라인
  - span, a, img, input, label, b, em, i , strong
  - text-align: left; 좌측정렬
  - text-align: right; 우측정렬
  - text-align: center; 가운데정렬

- 블록
  - div, ul, ol, li, p, hr, form, h1~h6
  - margin-right: auto; 좌측정렬
  - margin-left: auto; 우측정렬
  - margin-right: auto; margin-left: auto;  가운데정렬
  - margin: 0px auto 0px; 가운데 정렬
- display: block;
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 너비를 가질 수 없다면 자동으로 margin 부여
- display: inline;
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.
- display: inline-block;
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한줄에 표시가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- display: none;
  - 해당요소 화면에 표시 X, 공간 부여 X
  - visibility: hidden; 은 해당 요소가 공간은 차지하지만 화면에 표시하지 않는다.

---

### CSS position

- static: 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
  - 좌표(top, bottom, left, right)를 사용하여 이동가능 속성
- relative
  - 자신의 static을 기준으로 이동
  - 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음 normal flow 유지
- absolute
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
  - normal flow 벗어남
  - 자신의 static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없으면 body 기준)
  - 부모는 relative
- fixed
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
  - normal flow에서 벗어남
  - 부모 요소와 관계없이 viwport를 기준으로 이동
  - 스크롤 시에도 항상 같은 곳에 위치함

---

### 크롬 개발자 도구

- 주요기능
  - Elements - DOM 탐색 및 CSS 확인 및 변경
    - styles  - 요소에 적용된 모든 CSS 확인
      - 우선순위, 파일 로딩 등에 의해 적용되고 있는 모든 CSS 확인
      - 원하는 속성을 제거해보거나 값을 변경하여 결과를 바로 확인 가능
      - 스타일을 다양하게 추가해 볼 수 있음
      - 기존에 정의된 클래스를 추가해볼 수 있음
    - computed - 해당 요소에 최종 계산된 CSS 확인
      - 현재 요소에 지정된 박스모델에 대한 정보를 쉽게 확인 가능
      - 박스모델에 해당하는 영역 값을 쉽게 변경할 수 있음
    - Event Listeners - 해당 요소에 적용된 이벤트(JS)
    - HTML 태그 구조를 탐색하며 추가, 삭제, 이동, 편집 등이 가능
  - Sources, Network, Performance, Application, Security, Audits 등

---

### 추가

- font-size: 20px;
- font-weight: bold;
- font-family: Arial
- text-align: center;
- background-color: rgb(95, 173, 87);
- color: white;

---

### CSS Layout

- float
- flexbox
- grid

---

### float

- 인라인 요소들이 주변을 wrapping 하도록 함

- 요소가 Normal flow 벗어나도록 함

- float: none; 기본값

- float: left;

- float: right;

- ```css
  .clearfix::after {
      content: "";
      display: block;
      clear: both;
  }
  ```

- 부모요소에 반드시 Clearing Float를 하여 이후 요소부터 Normal Flow를 가지도록 지정

- 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성, 요소에 장식용 콘텐츠를 추가

---

### Flex box

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 수직정렬, 아이템 간격 너비 높이 등등 배치 편리
- 축
  - main axis
  - cross axis
- 구성요소
  - Flex Container
    - display: flex;
    - display: inline-flex;
  - Flex Item

---

### Flex 속성

- 배치 설정
  - flex-direction
    - row, row-reverse, column, column-reverse
  - flex-wrap
    - nowrap, wrap
  - flex-flow
    - flex-direction 과 flex-wrap 의 단축형 shorthand
    - flex-flow: row nowrap;
- 공간 나누기
  - justify-content / Main axis
    - flex-start, flex-end, center, space-between, space-around, space-evenly
  - align-content / Cross axis 기준
    - flex-start, flex-end, center, space-between, space-around, space-evenly
  - space-between
    - 아이템 사이의 간격을 균일하게 분배
  - space-around
    - 아이템을 둘러싼 영역을 균일하게 분배(가질 수 있는 영역을 반으로 나눠서 양쪽에)
  - space-evenly
    - 전체 영역에서 아이템 간 간격을 균일하게 분배
- 정렬
  - align-items
    - stretch, flex-start, flex-end, center, baseline
  - align-self
    - stretch, flex-start, flex-end, center
  - stretch : 컨테이너를 가득 채움
  - baseline : 텍스트 baseline 기준선을 맞춤
- 기타
  - flex-grow : 남은 영역을 아이템에 분배
  - order : 배치순서

---

### Bootstrap

- CDN
  - Content Delivery(Distribution) Network
  - 컨텐츠( CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
  - 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

---

### m, p

- mt-1 0.25 rem 16px * 0.25 = 4px
- mt-2 0.5 rem 8px
- mt-3 1 rem 16px
- mt-4 1.5 rem 24px
- mt-5 3 rem 48px

- mx-0
  - 좌우 0
- mx-auto
  - 좌우 자동 / 수평중앙정렬
- py-0
  - 페딩수직 0
- ms 왼쪽
- me 오른쪽

---

### color

- .bg-primary: 파란색 #007bff;
- .bg-secondary: 회색 #6c757d;
- .bg-success: 초록색 #28a745;
- .bg-info: 하늘색 #17a2b8;
- .bg-warning: 노란색 #ffc107;
- .bg-danger: 빨간색 #dc3545;
- .bg-light: 흰색 #f8f9fa;
- .bg-dark: 검은색 #343a40;
- .bg-white
- .bg-transparent

---

### 추가

- mx-auto 수평 중앙 정렬
- ms-auto 수평 우측 정렬
- text-success 글자 초록색
- text-start, text-center, text-end
- text-decoration-none
  - 링크 밑줄 장식 없애줌
- fw-bold, fw-normal, fw-light
  - font-weight
- fst-italic
  - 기울인 글씨

---

### display

- d-inline p-2
- d-block p-2
- d-none
- fixed-top
- fixed-bottom

---

### Components

- navigation sticky-top d-flex justify-content-between align-items-center bg-light px-4 py-3
  - nav-logo fs-5
  - nav-links
  - nav-links-item text-dark text-decoration-none me-3 /text-decoraiton-line: none;
  - list-style: none;
  - padding-left: 0px;
- container
  - section
    - img src alt
    - img-fluid
  - article
    - text-center
    - fw-bold fs-5 my-5
    - row row-cols-1 row-cols-md-2 g-4
      - col
        - card
          - img card-img-top
          - card-body
            - card-title
            - card-text
  - footer d-flex justify-content-center
    - a style width:30px;
      - img-fluid



---

### Flexbox

- d-flex, d-inline-flex
  - None(xs), sm, md, lg, xl, xxl
- flex-row, flex-row-reverse, flex-column, flex-column-reverse
- justify-content-~
  - start, end, center, between, around, evenly
- align-items-~
  - start, end, center, baseline, stretch
- align-self
  - start, end, center, baseline, stretch
- flex-fill
- flex-grow
- flex-nowrap, flex-wrap, flex-wrap-reverse
- order-0~5
- align-content-~
  - start, end, center, between, around, stretch / evenly 없음



---

### 반응형 웹

- Responsive Web
- 디바이스 크기에 따라 같은 컨텐츠를 배치가 다르게 보이도록 웹 디자인
- 다양한 화면 크기를 가진 디바이스의 등장
- Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag

---

### Bootstrap Grid System

- breakpoints
  - None(xs) 576px 미만 extra small
  - sm 576px 이상 small
  - md 768px 이상 medium
  - lg 992px 이상 large
  - xl 1200px 이상 extra large
  - xxl 1400px 이상 extra extra large
- Column
  - col : 알아서 사이즈 조절 요소들 row에 채워넣음
  - offset
  - col-9, col-4 / 12넘어가니까 col4는 다음줄부터 시작
- Gutter
- Container
- parent
  - align-self-center

---

