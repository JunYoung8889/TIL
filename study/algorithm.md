# algorithm

### 알고리즘

- 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법
- 슈도코드
  - 일반적인 언어로 코드를 흉내 내어 알고리즘을 써 놓은 코드
  - 의사 코드
  - 대략적으로 모델링
- 순서도
  - 진행흐름을 기호나 문자로 나타낸 도표
  - 흐름도
- 정확성, 작업량, 메모리 사용량, 단순성, 최적성
- 성능분석
  - 연산횟수
  - 실제 걸리는 시간
  - **실행되는 명령문 개수**
- 시간 복잡도 - 빅-오 표기법
  - O(2n+1) = O(n)
  - O(2n^2+10n+100) = O(n^2)

---

### list_01

- 배열 : 같은 타입 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
- list :  다양한 데이터를 저장, 가변적으로 변경 가능, 2차원 리스트도 가능
- 시퀀스 자료형
  - 순서 존재, 인덱싱, 슬라이싱 연산 모두 적용가능
- len(), +, *, in, not in, min, max, sorted()
- append(), insert(), pop(), remove(), count()
- list comprehension
- [i for i in list if i%2==0]

---

### 완전검색

- Exhaustive Search
- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- Brute-force, Generate-and-Test
- 순열(Permutation)
- nPr = n!

---

### 탐욕 알고리즘

- Greedy Algorithm
- 최적해를 구하는데 사용되는 근시안적인 방법
- 그순간에 최적
- 지역적으로 최적
- 부분 해 집합
- 문제의 제약 조건 위반 여부
- 문제의 해 인지 확인, 해가 아니면 부분 해 집합 선택 순서로 돌아감

---

### 정렬

- sort

- 2개 이상의 자료를 특정 기준에 의해 오름차순 혹은 내림차순 재배열

- 키 - 자료를 정렬하는 기준

- 버블, 카운팅, 선택, 삽입, 병합, 퀵

- 버블

  - 인접한 두개 비교 자리교환 방식

  - ```python
    a = [0,4,1,3,1,2,4,1]
    for i in range(len(a)-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)
    ```

- 카운팅 정렬

  - 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능

  - ```python
    a = [0,4,1,3,1,2,4,1]
    b = [0]*len(a)
    c = [0]*(max(a)+1)
    for i in range(0,len(a)):
        c[a[i]] += 1
        # c = [0,0,0,0,0]
        # c = [1,3,1,1,2]
        
    for i in range(1,len(c)):
        c[i] += c[i-1]
        # c = [1,3,1,1,2]
        # c = [1,4,5,6,8]
        
    for i in range(len(b)-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
        
    print(b)
    ```

---

### list 2

- 2차원 리스트
- 부분집합
- 검색
- 정렬

---

### 2차원 리스트

- arr = [0] * 5

- arr = [i for i in range(10) if i%2 == 0]   #  [0,2,4,6,8]

- brr = [[1,2,3]] * 3   # [[1,2,3],[1,2,3],[1,2,3]]

- brr = [[1,2,3] for i in range(3)]   # [[1,2,3],[1,2,3],[1,2,3]]

- crr = [[i,j] for i in range(3) for j in range(2)]   # [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]

- 행열 입력 받기

  - ```python
    n, m = map(int, input().split())
    arr = [0]*n
    for i in range(n):
       arr[i] = list(map(int, input().split()))
    print(arr)
    ```

  - ```python
    n, m = map(int, input().split())
    arr = list()
    for i in range(n):
        arr.append(list(map(int, input().split())))
    ```

- 행열 1찾기

  - ```python
    new_arr = [[i,j] for i in range(n) for j in range(m) if arr[i][j]==1]
    ```

  - ```python
    n, m = map(int, input().split())
    arr = [0]*n
    new_arr = list()
    for i in range(n):
        arr[i] = list(map(int, input().split()))
        for j in range (m):
            if arr[i][j] == 1:
                new_arr.append([i,j])
    ```

- 리스트 순회

  - 행 우선 순회

  - 열 우선 순회

  - 지그재그 순회

    - ```python
      for i in range(n):
          for j in range(m):
              arr[i][j+(m-1-2*j)*(i%2)]
              # i가 짝수이면 arr[i][j] 정방향
              # i가 홀수이면 arr[i][m-1-j] 역방향
      ```

- 델타를 이용한 2차원 리스트 탐색

  - dx = [0,0,-1,1] # 상하좌우
  - dy = [-1,1,0,0]

- 전치행렬

  - ```python
    for i in range(n):
        for j in range(n):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```

- Zip 함수

  - ```python
    arr = ['a','b','c']
    brr = [1,2,3]
    crr = list(zip(arr,brr)) # [('a',1),('b',2),('c',3)]
    ```

  - ```python
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    brr = list(zip(*arr)) #[(1,4,7),(2,5,8),(3,6,9)]
    ```

  - ```
    전치 행렬
    [(1, 2, 3),
     (4, 5, 6),
     (7, 8, 9)]
     
    [(1, 4, 7),
     (2, 5, 8),
     (3, 6, 9)]
    ```

---

### 부분집합

- ```python
  bit = [0,0,0,0]
  for i in range(2):
      bit[0] = i
      for j in range(2):
          bit[1] = j
          for k in range(2):
              bit[2] = k
              for l in range(2):
                  bit[3] = l
                  print(bit)
  ```

- 비트 연산자

  - 이진수에 대한 연산을 수행하는 연산자
  - & : and
  - | : or
  - << : 왼쪽이동
  - `>>` : 오른쪽 이동
  - `i & (1 << j)` i에서 j번째 비트가 1인지 아닌지 리턴

- 비트연산자 활용 부분집합

  - ```python
    arr = [3, 6, 7, 1, 5, 4]
    for i in range(1<<n): # 2**n, 부분집합의 개수
        for j in range(n): # 원소의 수
            if i & (1 << j): # i의 j번째 비트가 1이면 j번째 원소 출력
                print(arr[j], end=",")
        print()
    ```

---

### 검색

- 원하는 항목찾기
- 탐색키
- 순차검색
  - 일렬 순서대로 검색
  - 순차구조로 구현된 리스트에서 유용함
  - 비효율적
  - 정렬되어있는경우
    -  순서대로 검색, 키값이 같은 원소가있는지
    - 있으면 인덱스 반환
    - 키보다 원소크면 더이상 검사필요 x
  - 정렬되어있지 않는 경우
    - 끝까지 검색
    - 못찾으면 -1반환하게 설계
- 이진검색
  - 가운데 항목의 키값 비교
  - 반씩 줄여나감
  - 자료가 정렬되어 있어야 가능
  - 중앙값 목표값 비교
    - 목표값이 작으면 왼쪽
    - 목표값이 크면 오른쪽
- 인덱싱
  - 인덱스는 키 필드만 갖고있음

---

### 셀렉션 알고리즘

- 선택정렬
  - 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
  - 최소값 찾고 교환
  - 

