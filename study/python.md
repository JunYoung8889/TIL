

# python ( 파이썬 )

- variable ( 변수 )
- print(), input() ( 표준입출력함수 )

  

---

### variable ( 변수 )

- ```python
  numVariable = 10
  numVariable2 = 10 + 20
  strVariable = '10'
  strVariable2 = '안녕'
  listVariable = [10,'10','안녕',True]
  boolVariable = True
  noneVariable = None
  ```

- 지정연산자 ( = ) 으로 오른쪽의 값을 왼쪽 변수에 저장한다.

- `변수이름 = 변수에 저장할 값` 

- 변수이름은 용도의 의미에 맞게 만들면 좋다.

- 변수는 자료형의 값을 저장하는 공간 혹은 객체라고 할 수 있다.

  

---

### print(), input() ( 표준입출력함수 )

- print()

  - 데이터를 출력하는 용도로 사용한다.

  - ```python
    print('안녕 파이썬')
    print("안녕 파이썬")
    print('안녕','파이썬')
    print('안녕 '+'파이썬')
    print("안녕 " '파이썬')
    print('안녕'" 파이썬")
    ```
    
  - `''` 로 감싸거나 `""` 로 감싸면 문자열(string)이 되고 짝을 맞추어야한다.

  - `print( str + str )` 은 두 문자열이 붙어서 출력된다.

  - `print( str , str )` 은 두 문자열 사이에 공백 1칸이 생긴다.

    

  - ```python
    strVariable1 = '안녕'
    strVariable2 = '파이썬'
    print( strVariable1 , strVariable2 )
    print( '%s %s'%( strVariable1 , strVariable2 ) )
    print( f'{ strVariable1 } { strVariable2 }' )
    print('{} {}'.format( strVariable1, strVariable2 ) )
    print('{0} {1}'.format(strVariable1,strVariable2))
    print('{1} {0}'.format(strVariable2,strVariable1))
    ```

  - `print('%s %d %f'%(strVariable, intVariable, floatVariable))`

    - % 이후 해당 자료형의 약자를 쓰고 ''뒤에 %(변수이름) 형태로
    - 문장 내부에 변수의 값을 출력할 수 있다.

  - `print( f'{ variable } { variable2 } { variable3 }' )`

    - f string 형태로 {}내부에 변수이름을 작성해서
    - 문장 내부에 변수의 값을 출력할 수 있다.

  - `print('{인덱스}'.format(변수이름))`

    - str.format() 으로 {}안에 인덱스 넘버를 지정해주면
    - format() 안의 변수이름들을 인덱스 넘버에 맞게
    - 문장 내부에 변수의 값을 출력할 수 있다.
    - 인덱스 넘버를 지정하지 않고 {}만 작성할 경우 순차적으로 출력한다.


    

  - ```python
    print(30)
    print(10+20)
    print(3*10)
    numVariable = 30
    print(numVariable)
    print([1,2,3])
    print(None)
    print(True)
    ```

  - 숫자, 리스트, 부울, None 등 다양한 자료형 객체들을 출력할 수 있다.

  

- input()

  - 데이터를 키보드로 입력받는 함수이다.

  - ```python
    strVariable = input()
    print(strVariable)
    ```

  - 첫번째 코드가 실행되면 결과를 바로 출력하지 않고 커서가 깜빡인다.

  - 사용자로 부터 키보드를 통해 값을 입력받기 위해 대기하고 있는 상태이다.

  - `input()` 만 작성해서 파일 실행시 잠시 멈추도록 사용하는 경우도 있다.

  - 커서가 깜빡일때, `안녕 파이썬` 을 작성하고 엔터를 누르면

  - `print()` 함수를 통해 `안녕 파이썬` 이 출력된다.

    

  - ```python
    strVariable = input() # 10을 입력하면 문자열 '10'이 된다.
    print( 2 * strVariable ) # '1010' , 문자열이 2번 반복
    intVariable = int(strVariable) # 10
    print( 2 * intVariable ) # 20
    ```

  - `input()` 으로 입력받은 값은 기본적으로 문자열이다.

  - 이후 계산을 원한다면 원하는 자료형에 맞춰 변경해 주어야한다.

  - ```python
    strVar = input('10을 입력해주세요 : ')
    intVar = int(input('20을 입력해주세요 : '))
    print(int(strVar)+intVar) # 30
    ```

  - `input()` 내부에 문장을 적어서 값을 입력받기 전에 알려줄 수 있다.

  

---

### 문제 1

- 8 + 88 + 888  = 984

- ```python
  strVar = input('1~9 원하는 숫자를 입력해주세요 : ')
  a = int(strVar)
  aa = int(strVar*2)
  aaa = int(strVar*3)
  total = a + aa + aaa
  #print('%d + %d + %d = %d'%(a,aa,aaa,total))
  #print(f'{a} + {aa} + {aaa} = {total}')
  #print('{} + {} + {} = {}'.format(a,aa,aaa,total))
  print('{1} + {3} + {2} = {0}'.format(total,a,aaa,aa))
  ```

  

---

### 문제 2

- 허리둘레 32 inch 는 몇 cm인가?

- ```python
  # 1 inch = 2.54 cm
  strVariable = input('허리둘레 몇 inch?(숫자만입력) : ')
  fVar = float(strVariable)
  inch = 2.54 * fVar
  #print('%.2f inch => %.2f cm'%( fVar, inch ))
  #print('{0:.2f} inch => {1:.2f} cm'.format(fVar,inch))
  print(f'{fVar:.2f} inch => {inch:.2f} cm')
  ```

  

---

### 문제 3

- 몸무게 75kg은 몇 lb(파운드) 인가?

- ```python
  # 1kg = 2.2046lb
  iVar = int(input('몸무게 몇 kg?(숫자만입력) : '))
  lb = iVar * 2.2046
  #print('%.2f kg =>  %.2f lb'%(iVar,lb))
  #print('{:.2f} kg =>  {:.2f} lb'.format(iVar,lb))
  #print('{0:.2f} kg =>  {1:.2f} lb'.format(iVar,lb))
  print(f'{iVar:.2f} kg =>  {lb:.2f} lb')
  ```

  

---

### 문제 4

- 화씨 100도는 섭씨 몇도?

- 100 ℃  = 212 ℉ / 0 ℃ =  32 ℉

- 섭씨 100칸 = 화씨 180칸

- 섭씨 *180/100 +32 = 화씨 ~~확씨~~ 

- (화씨-32) *100/180 = 섭씨

- ```python
  strVariable = input('화씨 몇도?(숫자만입력) : ')
  fVar = float(strVariable)
  C = ( fVar - 32 ) * 100 / 180
  #print('%.2f ℉ =>  %.2f ℃'%(fVar,C))
  #print('{:.2f} ℉ =>  {:.2f} ℃'.format(fVar,C))
  #print('{0:.2f} ℉ =>  {1:.2f} ℃'.format(fVar,C))
  print(f'{fVar:.2f} ℉ =>  {C:.2f} ℃')
  ```

  

---

### 문제 5

- 섭씨 100도는 화씨 몇도?

- 섭씨 *180/100 +32 = 화씨

- ```python
  strVariable = input('섭씨 몇도?(숫자만입력) : ')
  fVar = float(strVariable)
  F = fVar * 180 / 100 + 32
  #print('%.2f ℃ =>  %.2f ℉'%(fVar,F))
  #print('{:.2f} ℃ =>  {:.2f} ℉'.format(fVar,F))
  #print('{0:.2f} ℃ =>  {1:.2f} ℉'.format(fVar,F))
  print(f'{fVar:.2f} ℃ =>  {F:.2f} ℉')
  ```

  

---

### 문제 6

- 농도 30 % 소금물 100g + 농도 50% 소금물 300g

- 혼합된 소금물의 농도?

- [김소원 소금물](https://www.youtube.com/watch?v=WFOKyWcOKC8)

- 전체 소금의 무게 / 전체 소금물 무게 * 100%

- ```python
  # 농도 30 % 소금물 100g + 농도 50% 소금물 300g
  salt = (100*0.3 + 300*0.5) /( 100 + 300 ) * 100
  #print('혼합된 소금물의 농도: %.2f%%'%salt) # %% 주의
  #print('혼합된 소금물의 농도: {:.2f}%'.format(salt))
  #print('혼합된 소금물의 농도: {0:.2f}%'.format(salt))
  print(f'혼합된 소금물의 농도: {salt:.2f}%')
  ```

  

---

### 임시 기록

- ASCII - American Standard Code of Information Interchange

  - 영문 + 기호 => 7bit
  - 한글 + 영문 + 기호 => 16bit

- 2진수, bit, binary digit

- 인터프리터 언어

  - 대화식 환경

- 명령프롬프트

  - python  + 엔터

  - 인터프리터 프롬프트 >>> print('hello')

- String, 문자열

- 내장함수 built in function

- IDLE - Integrated 통합 Development 개발

-  and Learning 학습 Environment 환경

- \ 뺵 슬레쉬

- 변수 Variable

  - 저장공간

- = 지정연산자

- +,-,*,/,//,%,** 산술연산자

- del(x) 변수삭제

- 명령행

  - 물리적 명령행 : 한 줄
  - 논리적 명령행 : 한 명령
    - i=10
    - print(i) 2물리 2논리
    - i=10; print(i) 1물리 2논리

- 들여쓰기(indent)

  - 공백4칸, 1탭, 한명령의 범위
  - 블록 block
  - 같은 들여쓰기 명령집합

- 에디터창

  - 저장, 실행, 여러줄 작성가능
  - 탐색기 실행 => test.py 실행 후 바로 꺼짐
  - 마지막줄에 input() 작성하면 입력받기위해 바로안꺼짐
  - import os
  - os.system('pause')

- 값이 변할 수 있는 수를 저장할 수 있는 저장공간

  - 변수, variable

- 문자열 또는 숫자 등의 결과를 출력할때 사용되는 함수

  - print()

- 주석문

  - 쉽게파악, 도움, 설명문
  - 영향 x
  - '#' 한줄
  - ''' 또는 """
  - 여러줄
  - ''' 또는 """

- import math

- math.pi

- math.sqrt

- 1.2 e0 => 1.2 * 10^0

- 1.2 E3 => 1.2 * 10^3

- \n 줄바꿈

- 예약어, keyword

  - reserved word
  - 기능, 사용용도가 이미 정해짐
  - 변수, 함수이름으로 사용하지말것
  - import keyword
  - keyword.kwlist

- 식별자, identifier

  - 변수이름, 사용자 정의함수 이름
  - 클레스 모듈 이름
  - 숫자로 시작x
  - 영문, 숫자, 밑줄, 유니코드문자, 한글도 가능함

- 변수 variable

  - 변할 수 있는 값
    - 반대, 상수 - constant
  - 값을 저장하는 공간
  - 타 언어처럼 미리 선언할 필요 없음

- 변수이름

  - 식별자와 같은 규칙
  - 일반적으로 변수는 소문자, 상수는 대문자
  - 사용목적에 상관있는 이름으로 만드는게 일반적임
  - 이름이 길면 밑줄_ 사용
  - 중간에 대문자를 써서 낙타체로 사용
  - 특수문자 x

- 변수의 종류

  - data type에 따라 구분
  - 부울형, 정수형, 실수형, 문자열, 복소수형 등등

- 연산자 operator

  - 산술, 관계, 논리, 증감, 비트, 지정

- 상수 Constant

  - 값 변화x
  - 숫자, 문자열

- 주석문 comment

  - 코드를 쉽게 파악할 수 있게 도움
  - 설명문
  - 한줄을 쓰고 싶으면 '#'을 사용
  - 여러줄을 쓰고 싶으면
  - '''                 """
  - 여러줄       여러줄
  - '''                """

- 함수

  - 내장함수 built in function
  - 사용자 정의 함수 user defined function

- 지정연산자 =

  - 값을 지정해준다.

- 기본 입출력 함수

  - input() 입력
  - print() 출력

- print()

  - %d 정수 %f 실수 %s 문자열 %c 한글자 %x 16진수 %o 8진수
  - 10진수 decimal
  - 8진수 octal
  - 16진수 hexa decimal
  - n =123
  - print('%d'%n)  => 123
  - print(''%6d'%n) =>    123 # 글자수 6글자, 빈칸 공백
  - print('%06d'%n) => 000123 # 글자수 6글자, 빈칸 0
  - fn = 12.345
  - print('%f'%fn) => 12.345000
  - print('%7.1f'%fn) =>    12.3 # .을 포함해서 7글자, 소수점 1번째자리까지
  - print('%07.1f'%fn) => 00012.3 # 7글자, 빈칸 0, 소수점 1번째자리까지
  - print('%07.3f'%fn) => 012.345 # 7글자, 빈칸 0, 소수점 3번째자리까지
  - print('%.2f'%fn) => 12.35 # 반올림됨
  - s = 'program'
  - print('%10s'%s) =>    program # 10글자, 빈칸 공백
  - pi=3.14; name='kim'; age=20
  - print('name=%s, age=%d, pi=%.1f'%(name,age,pi))
  - print('name={0}, age={1}, pi={2:.1f}'.format(name,age,pi))
  - print(f'name={name}, age={age}, pi={pi:.1f}')
    - f-문자열 리터럴 기능

- input()

  - str
  - int(), float(), str()

- type()

  - <class ' '>

- 2진수, 8진수, 16진수

  - 0b0101, 0o7577, 0xF09A
  - bin(), oct(), hex()

- 000_000.000_0001 밑줄 사용가능



