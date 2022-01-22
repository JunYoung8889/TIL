# recursive function - 재귀함수

### 유튜브 추천

- [유튜브 - 얄팍한 코딩사전 - 재귀함수](https://www.youtube.com/watch?v=aPYE0anPZqI)





---

### 명제

- [JunYoung8889/TIL/study/CT/01_ct.md](https://github.com/JunYoung8889/TIL/blob/master/study/CT/01_ct.md)

- p -> q 에서 p가 거짓이면 전체 명제는 항상 참이다.

- |  p   |  q   | p -> q |
  | :--: | :--: | :----: |
  |  T   |  T   |   T    |
  |  T   |  F   |   F    |
  |  F   |  T   |   T    |
  |  F   |  F   |   T    |





---

### 귀납법

- [JunYoung8889/TIL/study/CT/02_ct.md](https://github.com/JunYoung8889/TIL/blob/master/study/CT/02_ct.md)
- P(1), P(n) -> P(n+1)
  - P(1)이 성립함을 보이고
  - P(n)이 T라고 가정했을때, P(n+1)이 T가됨을 보여서 증명한다.
  - 또는, P(n-1)이 T라고 가정했을때, P(n)이 T가됨을 보여서 증명한다.
  - 또는, p(1)^p(2)^•••^p(n-1)이 T라고 가정했을때, p(n)이 T가 됨을 보여서 증명한다.



---

### 재귀함수

- sum(n)
- factorial(n)
- fibonacci(n)



---

### sum(n)

- sum(n) = 0+1+2+•••+n-1+n

- 점화식 : sum(n) = n + sum(n-1)

  - P(1)이 성립함을 보여라

    - 해당 점화식의 첫째항은 0이다.
    - sum(0) = 0

  - P(n-1)이 T일때, P(n)이 T임을 보여라

    - p -> q 에서 p가 F면 전체 명제는 항상 T이므로
    - 가정 p가 F인 상황은 고려할 필요가 없다.
    - 가정 p가 T일때, q가 T가되야 p->q가 T가된다.
    - 따라서 p가 T라고 가정했을때, q가 T임을 보이면
    - p->q 전체 명제는 항상 참이된다.
    - p->q
      - p : sum(n-1) = 0 + 1 + 2 + ••• + n-1
      - q : sum(n) = 0 + 1 + 2 + ••• + n-1 + n
      - sum(n) = n + sum(n-1)
      - 가정 p 가 T라고 가정했으므로(F이면 전체는 T)
      - sum(n) = n +(0+1+2+•••+n-1)
      - sum(n) = 0+1+2+ ••• + n-1 + n
      - 따라서 p가 T이면 q가 T임을 보였다.

  - 코드

  - ```python
    def my_sum(n):
        if n == 0:
            return 0
        	# my_sum(0) = 0
        else:
            return n + my_sum(n-1)
        	# my_sum(n) = n + my_sum(n-1)
    
    print(my_sum(10))
    # 0 + 1 + 2 + ••• + 9 + 10 = 55
    ```





---

### factorial(n)

- sum(n)과 같이 귀납법으로 증명가능한 점화식 형태를 찾아서

- 재귀함수로 만들어주자!

  - factorial(n) = `1 * 2 * ••• * n`

  - factorial(n) = n * factorial(n-1)

  - P(1)이 성립함을 보여라
  
    - 해당 점화식의 첫째항은 1이다. (0이면 전체 곱 0)
    - factorial(1) = 1

  - P(n-1)이 T이면 P(n)이 T임을 보여라
  
    - p -> q
    - p : factorial(n-1) =  `1 * 2 * ••• * (n-1)`
    - q : factorial(n) = n * factorial(n-1)
    - 가정 p가 T라고 가정했으므로
    - factorial(n) = n * (`1 * 2 * ••• * (n-1)`)
    - factorial(n) = `1 * 2 * ••• * n`
    - 따라서 p가 T이면 q가 T임을 보였다.

  - 코드
  
  - ```python
    def facto(n):
        if n == 1:
            return 1
        	# facto(1) = 1
        else:
            return n * facto(n-1)
        	# facto(n) = n * facto(n-1)
    
    print(facto(5))
    # 1 * 2 * 3 * 4 * 5 = 120
    ```





---

### fibonacci(n)

- [피보나치 수열 - 위키 백과](https://ko.wikipedia.org/wiki/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98_%EC%88%98)

- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, •••

- |  **n**  | **0** | **1** | **2** | **3** | **4** |
  | :-----: | :---: | :---: | :---: | :---: | :---: |
  | fibo(n) |   0   |   1   |   1   |   2   |   3   |
  |  **n**  | **5** | **6** | **7** | **8** | **9** |
  | fibo(n) |   5   |   8   |  13   |  21   |  34   |

- fibo(0) = 0, fibo(1) = 1

- fibo(n) = fibo(n-1) + fibo(n-2)

- 코드

- ```python
  def fibo(n):
      if n == 0 or n == 1:
          return n
      	# fibo(0) = 0, fibo(1) = 1
      else:
          return fibo(n-1) + fibo(n-2)
      	# fibo(n) = fibo(n-1) + fibo(n-2)
      
  print(fibo(9))
  # fibo(9) = fibo(8) + fibo(7)
  # 34 = 21 + 13
  ```





---

### 선택 정렬

- [JunYoung8889/TIL/study/sort.md](https://github.com/JunYoung8889/TIL/blob/master/study/sort.md)

```python
def my_sort(para_list):
    if len(para_list) == 1:
        return para_list
    else:
        min_num = min(para_list)
        para_list.remove(min_num)
        return [min_num] + my_sort(para_list)
    
print(my_sort([ 5, 8, 2, 6, 3, 1, 7, 4 ]))
```



---

### 버블 정렬

```python
def my_sort(para_list):
    ans_bool = True
    for i in range(len(para_list) -1):
        if para_list[i] > para_list[i+1]:
            ans_bool = False
            para_list[i], para_list[i+1] = para_list[i+1], para_list[i]
            print(para_list)
    if ans_bool == True:
        return para_list
    else:
        return my_sort(para_list)

    
print(my_sort([ 5, 8, 2, 6, 3, 1, 7, 4 ]))
```





---

### 삽입 정렬

```python
def my_sort(para_list):
    ans_bool = True
    for i in range(1,len(para_list)):
        for j in range(i):
            if para_list[j] > para_list[i]:
                ans_bool = False
                temp = para_list[i]
                for k in range(i,j,-1):
                    para_list[k] = para_list[k-1]
                para_list[j] = temp
                print(para_list)
    if ans_bool == True:
        return para_list
    else:
        return my_sort(para_list)

    
print(my_sort([ 5, 8, 2, 6, 3, 1, 7, 4 ]))
```

