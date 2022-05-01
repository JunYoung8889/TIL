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

- 원시타입, 참조타입

- ```
  - 원시 타입 primitive type
  	- Number
  	- String
  	- Boolean
  	- undefined
  	- null  // typeof 찍으면 object가 나옴 버그임 ㅠ
  	- Symbol ?
  - 객체 object가 아닌 기본 타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨
  ```

- ```
  - 참조 타입 Reference type
  	- Objects
  		- Array
  		- Function
  		- ... etc
  - 객체 object 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨
  ```

- ```javascript
  // const 인데 재할당???
  // 참조하고 있는 주소가 바뀐게 아니기 때문에 재할당이 아니다!
  const nums = [1,2,3,4,5]
  console.log(nums[0])  // 1
  nums[0] = 6
  console.log(nums)  // (5) [6,2,3,4,5]
  console.log(nums[0])  // 6
  ```

- ```javascript
  // 원시 타입은 실제 저장된 값이 복사됨 
  let myNum = 5
  let yourNum = myNum
  console.log(myNum)  // 5
  console.log(yourNum)  // 5
  myNum = 6
  console.log(myNum)  // 6
  console.log(yourNum)  // 5, myNum의 실제 값을 복사한 이후에 myNum이 바껴도 yourNum은 안바뀐다.
  ```

---

### 원시 타입 Primitive type

- ```
  - 숫자 Number 타입
  	- 정수, 실수 구분 없는 하나의 숫자 타입
  	- 부동소수점 형식을 따름
  	- Infinity / -Infinity
  	- NaN
  		- 계산이 불가능한 경우 반환되는 값
  		- 산술 연산 불가
  ```

- ```javascript
  // Infinity 관련 참고
  console.log(Infinity)  // Infinity
  console.log(Infinity/4)  // Infinity
  console.log(Infinity/Infinity)  // NaN
  console.log(Infinity*0)  // NaN
  console.log(Infinity - Infinity)  // NaN
  console.log(Infinity * Infinity)  // Infinity
  console.log(Infinity + Infinity)  // Infinity
  console.log(-Infinity * Infinity)  // -Infinity
  ```

- ```
  - 문자열 String 타입
  	- 텍스트 데이터를 나타내는 타입
  	- 16비트 유니코드 문자의 집합
  	- 작은따옴표, 큰따옴표 모두 가능
  	- 탬플릿 리터럴 Template Literal
  		- ES6부터 지원
  		- 따옴표 대신 backtick
  		- ${ expression } 형태로 표현 삽입 가능
  ```

- ```javascript
  // 유니코드 문자
  console.log('a' < 'z')  // true 'a' 가 앞번호 'z'가 뒷번호
  console.log('A' < 'a')  // true 대문자가 앞번호 소문자가 뒷번호
  console.log('A' < 'Z')  // true 'A' 가 앞번호 'Z'가 뒷번호
  
  console.log('a'.charCodeAt())  // 97
  console.log('z'.charCodeAt())  // 122
  console.log('A'.charCodeAt())  // 65
  console.log('Z'.charCodeAt())  // 90
  console.log(String.fromCharCode(97))  // a
  ```

- ```javascript
  // 탬플릿 리터럴, 파이썬 f스트링이랑 비슷, 여러줄 문자열 가능
  const myName = 'JYP'
  const myAge = 8
  const testString = `my name is ${myName},
  my age is ${myAge}`
  console.log(testString)
  /*
  my name is JYP,
  my age is 8
  */
  ```

- ```
  - undefined
  	- 변수의 값이 없음을 나타내는 데이터 타입
  	- 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨
  ```

- ```javascript
  // undefined
  let myNum
  console.log(myNum)  // undefined
  console.log(typeof myNum)  // undefined
  
  // const
  const myNum  // Uncaught SyntaxError: Missing initializer in const declaration
  console.log(myNum)
  
  // const undefined
  const myNum = undefined
  console.log(myNum)  // undefined
  console.log(typeof myNum)  // undefined
  ```

- ```
  - null
  	- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
  	- typeof(null)  // 'object'
  	- typeof null  // 'object'
  ```

- ```
  - NaN, null, undefined
  	- NaN 산술 연산 불가 의미 / typeof NaN // 'number'
  	- null 없다는것을 표시해줄때 / 개발자가 의도하고 쓰는 표현
  	- undefined 선언됐으나 할당안됐을때, / 개발자가 의도하지 않음, 자바스크립트가 자동으로 할당
  ```

- ```
  - Boolean 타입
  	- 논리적 참 또는 거짓을 나타내는 타입
  	- true, false
  	- 조건문, 반복문에서 유용하게 사용
  ```

- ```
  - ToBoolean Conversions (자동 형변환)
  	- undefined : 항상 거짓
  	- null : 항상 거짓
  	- number : 0, -0, NaN 거짓
  	- string : 빈문자열 거짓
  	- object : 항상 참
  ```

- ```javascript
  // undefined 항상 거짓
  if (undefined) {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  ```

- ```javascript
  // null 항상 거짓
  if (null) {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  ```

- ```javascript
  // number 0, -0, NaN 거짓
  if (0) {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  
  if (-0) {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  
  if (NaN) {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  
  if (1) {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  ```

- ```javascript
  // string 빈문자열 거짓
  if ('') {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  
  if (' ') {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  
  if ('hi') {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  ```

- ```javascript
  // object 항상 참
  if ([]) {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  
  if ({}) {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  ```

- ```javascript
  // function 도 object 항상 참
  if (function () {}) {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  
  function testFunction () {
      return false
  }
  if (testFunction()) {
      console.log(true)
  } else {
      console.log(false)
  }  // false
  
  if (testFunction) {
      console.log(true)
  } else {
      console.log(false)
  }  // true
  
  console.log(testFunction)
  /*
  ƒ testFunction () {
      return false
  }
  */
  console.log(testFunction())  // false
  ```

---

### 연산자

- ```
  - 할당 연산자
  	- 오른쪽에 있는 피 연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  	- 다양한 연산에 대한 단축 연산자 지원
  	- +=, -=, *=, /= 등등
  	- Increment(++) / i++ 값 1 증가
  	- Decrement(--) / i-- 값 1 감소
  ```

- ```javascript
  let x = 5
  console.log(x)  // 5
  console.log(x++)  // 5
  console.log(x)  // 6
  ```

- ```
  - 비교 연산자
  	- 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
  	- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  ```

- ```javascript
  // 유니코드 문자
  console.log('a' < 'z')  // true 'a' 가 앞번호 'z'가 뒷번호
  console.log('A' < 'a')  // true 대문자가 앞번호 소문자가 뒷번호
  console.log('A' < 'Z')  // true 'A' 가 앞번호 'Z'가 뒷번호
  
  console.log('a'.charCodeAt())  // 97
  console.log('z'.charCodeAt())  // 122
  console.log('A'.charCodeAt())  // 65
  console.log('Z'.charCodeAt())  // 90
  console.log(String.fromCharCode(97))  // a
  ```

- ```
  - 동등 비교 연산자 (==)
  	- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  	- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  	- 객체는 참조 타입이므로 객체의 경우 메모리의 같은 객체를 바라보는지 판별
  ```

- ```javascript
  // 암묵적 타입 변환
  const a = 100
  const b = '100'
  console.log(a==b)  // true
  console.log(a===b)  // false
  console.log(a+b)  // 100100
  
  const c = 1
  const d = true
  console.log(c==d)  // true
  console.log(c===d)  // false
  console.log(c+d)  // 2
  ```

- ```
  - 일치 비교 연산자 (===)
  	- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  	- 타입과 값 모두 같은지 비교, 암묵적 타입 변환이 발생하지 않음
  	- 객체는 참조 타입이므로 객체의 경우 메모리의 같은 객체를 바라보는지 판별
  ```

- ```
  - 논리 연산자
  	- && and
  	- || or
  	- ! not
  ```

- ```javascript
  // 논린 연산자, 단축 평가 지원
  console.log(1 && 5)  // 5
  console.log(1 || 5)  // 1
  console.log('' && 5)  // ''
  console.log('' || 5)  // 5
  ```

- ```
  - 삼항 연산자 Ternary Operator
  	- 세계의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
  	- 가장 왼쪽의 조건식이 참이면 콜론 앞의 값을 거짓이면 뒤의 값을 사용
  	- 결과가 값이기 때문에 변수에 할당 가능
  ```

- ```javascript
  console.log([] ? 1 : 2)  // 1
  console.log('' ? 1 : 2)  // 2
  const isOkay = {} ? true : false
  console.log(isOkay)  // true
  ```

- 



 