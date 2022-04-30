# JavaScript

### JavaScript의 필요성

- ```
  - 브라우저 화면을 '동적'으로 만들기 위함
  - 브라우저를 조작할 수 있는 유일한 언어
  - 브라우저
  	- URL로 웹을 탐색하며 서버와 통신하고
  	- HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
  ```

---

### 브라우저에서 할 수 있는 일

- DOM, BOM, JavaScript Core

- ```
  - DOM Document Object Model
  	- HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
  	- 문서를 구조화, 객체로 취급,  key로 접근 가능, 논리적 트리 모델
  	- 속성 접근, 메서드 활용, 프로그래밍 언어적 특성을 활용한 조작 가능
  	- document
  		- 페이지 컨텐츠의 Entry Point 역할을 함
  		- head body 등과 같은 수많은 다른 요소들을 포함
  		- document.title
  		- document, head, body, title, forms, links
  	- 파싱 (Parsing)
  		- 구문 분석, 해석
  		- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
  ```

- ```
  - BOM Browser Object Model
  	- 자바스크립트가 브라우저와 소통하기 위한 모델
  	- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  	- 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
  	- nevigatior, location, history, screen, frames, console, window
  	- window
  		- DOM을 표현하는 창(브라우저 탭), 최상위 객체 (작성 시 생략 가능)
  		- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭
  		- window.open() : 새탭 열기
  		- window.print() : 현재창 인쇄
  		- window.confirm() : 팝업창 / 확인, 취소 / true false
  		- window.alert() : 팝업창 / 확인 / undefined
  		- window.document : 현재 페이지 문서 객체
  			- #document
  ```

- ```
  - JavaScript Core (ECMAScript)
  	- 브라우저(BOM & DOM)을 조작하기 위한 명령어 약속(언어)
  	- Data Structure(Object, Array) 자료구조(객체, 배열)
  	- Conditional Expression 조건문
  	- Iteration 반복문
  	- ECMAScript
  		- ECMA : 정보 통신에 대한 표준을 제정하는 비영리 표준화 기구
  		- ECMA-262 규격에 따라 정의한 언어
  		- ECMAScript6는 ECMA에서 제안하는 6번째 표준 명세를 말함
  ```

---

### 세미콜론

- ```
  - 세미콜론 (semicolon)
  	- 자바스크립트는 세미콜론을 선택적으로 사용 가능
  	- ASI Automatic Semicolon Insertion 자동 세미콜론 삽입 규칙
  ```

- ```javascript
  // 세미콜론 O
  const nums = [1,2,3,4,5];
  console.log(nums);  // (5) [1, 2, 3, 4, 5]
  
  // 세미콜론 X
  const nums2 = [6,7,8,9,10]
  console.log(nums2)  // (5) [6, 7, 8, 9, 10]
  ```

---

### 식별자

- ```
  - 식별자 identifier
  	- 변수를 구분할 수 있는 변수명을 말함
  	- 문자, 달러($) 또는 밑줄(_)로 시작
  	- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
  	- 예약어 사용 불가능
  		- for, if, function 등
  ```

- ```
  - 식별자 작성 스타일
  	- 카멜 케이스 camelCase lower-camel-case
  		- 변수, 객체, 함수에 사용
  		- ex ) variableName
  	- 파스칼 케이스 PascalCase upper-camel-case
  		- 클래스, 생성자에 사용
  		- ex ) ArticleAdmin
  	- 대문자 스네이크 케이스 SNAKE_CASE
  		- 상수 constants에 사용
  		- 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미
  		- ex ) BASE_DIR
  ```

---

### 변수 선언

- ```
  - let
  	- 재할당 할 예정인 변수 선언 시 사용
  	- 변수 재선언 불가능
  	- 블록 스코프
  - const
  	- 재할당 할 예정이 없는 변수 선언 시 사용
  	- 변수 재선언 불가능
  	- 블록 스코프
  - 블록 스코프 block scope
  	- if, for, 함수 등의 중괄호 내부를 가리킴
  	- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
  ```

- ```javascript
  // 블록 스코프
  let myAge = 8
  if (true) {
      let myAge = 28  // 재선언 아님! / let은 블록 스코프 / 블록 내부, 바깥 별개!
      console.log(myAge)  // 28
  }
  console.log(myAge)  // 8
  ```

- ```
  - 선언 Declaration
  	- 변수를 생성하는 행위 또는 시점
  - 할당 Assignment
  	- 선언된 변수에 값을 저장하는 행위 또는 시점
  - 초기화 Initializtion
  	- 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점
  ```

- ```javascript
  // 선언
  let letVar
  console.log(letVar) // undefined
  // 할당
  letVar = 10
  console.log(letVar) // 10
  
  // 선언 + 할당
  let myAge = 8
  console.log(myAge) // 8
  ```

- ```
  - var
  	- var로 선언한 변수는 재선언 및 재할당 모두 가능
  	- ES6 이전에 변수를 선언할 때 사용되던 키워드
  	- 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능
  		- ES6 이후부터는 var 대신 const와 let 사용을 권장
  		- 호이스팅 : 변수를 선언 이전에 참조할 수 있는 현상
  	- 함수 스코프
  		- 함수 바깥에서 접근 불가능
  		- Uncaught ReferenceError : ~~ is not defined
  ```

---

### 변수 선언 관련 에러

- ```javascript
  const myNum  // Uncaught SyntaxError: Missing initializer in const declaration
  myNum = 5
  console.log(myNum)
  
  // const는 선언+할당 필수! 선언만 하면 문법 오류 발생
  const myNum = 5
  console.log(myNum)  // 5
  
  // const는 재할당 불가능
  const myNum = 5
  myNum = 6  // Uncaught TypeError: Assignment to constant variable.
  console.log(myNum)
  
  // let은 재할당 가능
  let myNum2 = 5
  myNum2 = 6
  console.log(myNum2)  // 6
  ```

- ```javascript
  // let 재선언 불가능
  let myNum = 5
  let myNum = 6  // Uncaught SyntaxError: Identifier 'myNum' has already been declared
  
  // const 재선언 불가능
  const myNum = 5
  const myNum = 6  // Uncaught SyntaxError: Identifier 'myNum' has already been declared
  ```

- ```javascript
  // 1
  let myNum = 5
  if (true) {
      let myNum = 6  // let은 블록스코프 이므로 재선언이 아님, 에러발생 X 
      console.log(myNum)  // 6
  }
  console.log(myNum)  // 5
  
  // 2
  /*
  Uncaught ReferenceError : ~~ is not defined 를 예상하고 짠 코드인데
  의외로 에러없이 둘다 출력됨
  */
  let myNum = 5
  if (true) {
      console.log(myNum)  // 5
  }
  console.log(myNum)  // 5
  
  // 3
  /*
  myNum2 는 if문 블록 스코프 내에서 let으로 선언했기 때문에
  블록 밖에서 접근하면 선언하지 않았다고 ReferenceError가 발생한다.
  let, const는 블록 스코프이다.
  */
  let myNum = 5
  if (true) {
      let myNum2 = 6
      console.log(myNum)  // 5
      console.log(myNum2)  // 6
  }
  console.log(myNum)  // 5
  console.log(myNum2)  // Uncaught ReferenceError: myNum2 is not defined
  
  // 4
  // var는 함수 스코프이므로 if 블록 밖에서 접근 가능하다.
  if (true) {
      var myNum = 5
      console.log(myNum)  // 5
  }
  console.log(myNum)  // 5
  
  // 5
  /*
  myNum 은 myFunc 함수 내부에서 var로 선언했기 때문에
  함수 밖에서 접근하면 선언하지 않았다고 ReferenceError가 발생한다.
  var는 함수 스코프이다.
  */
  function myFunc (para) {
      var myNum = 5
      console.log(myNum)  // 5
      const paraNum = para
      console.log(paraNum)  // 6
  }
  myFunc(6)
  console.log(myNum)  // Uncaught ReferenceError: myNum is not defined
  ```

- ```javascript
  // 호이스팅 : 변수를 선언 이전에 참조할 수 있는 현상
  // var
  console.log(myName)  // undefined
  var myName = 'JYP'
  console.log(myName)  // JYP
  
  // 앞에 아무것도 안썼을 때
  myName = 'JYP'  // var, let, const 안써도 동작함
  console.log(myName)  // JYP
  
  console.log(myName)  // Uncaught ReferenceError: myName is not defined
  myName = 'JYP'
  
  // let
  console.log(myName)  // Uncaught ReferenceError: myName is not defined
  let myName = 'JYP'
  
  // const
  console.log(myName)  // Uncaught ReferenceError: myName is not defined
  const myName = 'JYP'
  ```

---

### 데이터 타입 종류

- 



 