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



