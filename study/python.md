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
    strVariable1 = '안녕'
    strVariable2 = '파이썬'
    print( strVariable1 , strVariable2 )
    print( '%s %s'%( strVariable1 , strVariable2 ) )
    print( f'{ strVariable1 } { strVariable2 }' )
    print('{} {}'.format( strVariable1, strVariable2 ) )
    print('{0} {1}'.format(strVariable1,strVariable2))
    print('{1} {0}'.format(strVariable2,strVariable1))
    print(30)
    print(10+20)
    print(3*10)
    numVariable = 30
    print(numVariable)
    print([1,2,3])
    print(None)
    print(True)
    ```

  - `''` 로 감싸거나 `""` 로 감싸면 문자열(string)이 되고 짝을 맞추어야한다.

  - `print( str + str )` 은 두 문자열이 붙어서 출력된다.

  - `print( str , str )` 은 두 문자열 사이에 공백 1칸이 생긴다.

  

- input()



---



