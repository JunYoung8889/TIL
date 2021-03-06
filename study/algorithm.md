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





---

### 문자열

- 문자열
- 패턴 매칭
- 문자열 암호화
- 문자열 압축

---

### 문자의 표현

- 각 문자에 대응되는 숫자를 정해 놓고 이것을 메모리에 저장하는 방법이 사용될 것이다.
- 글자 모양 그대로 저장하는 비트맵 형식은 메모리 낭비가 심함
- 각 지역별로 코드체계를 정해놓고 사용하다가 네트워크(인터넷)이 발전하면서 서로간에 정보를 주고 받을 때 정보를 달리 해석한다는 문제가 생겼다.
- 그래서 혼동을 피하기 위해 표준안을 만들기로 했다.
- ASCII
- 빈칸이랑 null은 다름
- 확장 아스키
  - 표준 아스키는 7비트
  - 확장 아스키는 8비트
- 유니코드
  - 자국의 문자 한글을 표현하기 위하여 코드체계를 만들어 조합형 완성형으로 따로 사용하다가 자국의 코드체계를 타 국가가 가지고 있지 않으면 정보를 잘못 해석할 수 밖에 없었다.
  - 다국어 처리를 위한 표준
  - 유니코드도 다시 Character Set으로 분류된다.
    - UCS-2
    - UCS-4
  - 바이트 순서에 대해서 표준화하지 못했음
  - UTF-8
    - 필요에 따라서 8비트 ~ 4바이트 가변
  - 8-bit / 8bits
  - Python 인코딩
    - 2.x 버전 `#-*- coding: utf-8 -*-` 첫줄에 명시
    - 3.x 버전 생략가능

---

### 문자열의 분류

- 자바, 파이썬 String 클래스

- C언어

  - char ary[] = {'a','b','c','\0'};

- ```python
  s1 = list(input())
  s2 = input()
  print(s1)
  print(s2)
  # ['1', '2', '3']
  # 123
  ```

- strlen() 함수 만들어 보기

- ```python
  def strlen(para_list):
      cnt = 0
      while para_list[cnt] != '\0':
          cnt += 1
      return cnt
  
  
  a = ['a', 'b', 'c', '\0']
  print(strlen(a))
  ```

---

### 문자열 처리

- 메소드

  - replace()
  - split()
  - isalpha()
  - find()

- ```python
  s1 = 'abc'
  s2 = s1[:3]
  print(s1, s2)
  print(id(s1), id(s2))
  print(s1==s2)
  print(s1 is s2)
  ```

  ```python
  s1 = 'abc'
  s2 = s1[:2] + 'c'
  print(s1, s2)
  print(id(s1), id(s2))
  print(s1==s2)
  print(s1 is s2)
  ```

  

- ```python
  s1 = ['a', 'b', 'c']
  s2 = s1[:3]
  print(s1, s2)
  print(id(s1), id(s2))
  print(s1==s2)
  print(s1 is s2)
  ```

- ```python
  s1 = 'abc'
  s2 = 'ab'
  print( s1>s2 )
  ```

- ```python
  def atoi(s):
      i = 0
      for x in s:
          i = i*10 + ord(x) - ord('0')
      return i
  
  print(atoi('123'))
  ```

---

### 패턴 매칭

- 고지식한 알고리즘(Brute Force)

  - 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

  - ```python
    def BruteForce(p, t):
        i = 0
        j = 0
        while j < len(p) and i < len(t):
            if t[i] != p[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
        if j == len(p):
            return i - len(p)
        else:
            return -1
    
    p = "is"
    t = "This is a book"
    print(BruteForce(p, t))
    ```

---

### KMP

- ```python
  def kmp(t, p):
      N = len(t)
      M = len(p)
      lps = [0] * (M+1)
  
      j = 0
      lps[0] = -1
      for i in range(1, M):
          lps[i] = j
          if p[i] == p[j]:
              j += 1
          else:
              j = 0
      lps[M] = j
      
      i = 0
      j = 0
      while i < N and j <= M:
          if j == -1 or t[i] == p[j]:
              i += 1
              j += 1
          else:
              j = lps[j]
          if j == M:
              print(i-M, end = ' ')
              j = lps[j]
      print()
      return
  
  t = 'zzzabcdabcdabcefabcd'
  p = 'abcdabcef'
  kmp(t,p)
  ```



---

### 보이어-무어

- 끝자리 비교하고 한칸씩 앞으로 비교 실패하면 길이만큼 건너가서 반복
- 빅오 - 최악의경우, 세타 - 항상이정도
- 호스풀 알고리즘 찾아보기





---

### 문자열 암호화

- 평행이동
- 단일치환
- 배타적 논리합 / exclusive-or / ^
- 문자열 압축 - 이미지 BMP 파일포맷 압축방법

---

### 스텍1

- 스텍
  - 푸시
  - 팝
  - 탑
- 메모아이제이션
- DP

---

### 스택2

- DFS
- 계산기
- 백트래킹
- 부분집합, 순열
- 분할정복

---

### DFS

- 깊이 우선 탐색(Depth First Search, DFS)
- 너비 우선 탐색(Breadth First Search, BFS)
- 더 이상 갈곳이 없게 되면 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 탐색
- 방문 했는지 안했는지 v w 로 구분 하면서 스텍으로 push했다가 꺼내썼다가 하면서 스택으로 구현 가능
- 재귀함수로도 구현가능
- `+` do while 일단 한번 들어가는 와일문

---

### 계산기

- 문자열 계산식
- 중위 표기식
- 후위 표기식
- 여는괄호 확인
  - 연산자 (우선순위에 따라 스텍에 푸쉬)
  - 피연산자 후위표기식 문자열에 저장

---

### 백트래킹

- 미로찾기

- 엔퀸

- 부분집합

  - ```python
    def f(i, N, K):
        global cnt
        cnt += 1
        if i == N:
            s = 0
            for j in range(N):
                if bit[j]:
                    s += a[j]
            if s == K:
                for k in range(N):
                    if bit[k]:
                        print(a[k], end = ' ')
                print()
        else:
            bit[i] = 1
            f(i+1, N, K)
            bit[i] = 0
            f(i+1, N, K)
    
    cnt = 0
    a = [1,2,3,4,5,6,7,8,9,10]
    N = len(a)
    bit = [0]*N
    f(0,N,10)
    print(cnt)
    ```
    
  - ```python
    def f(i, N, s, t):
        global cnt
        cnt += 1
        if s == t:
            for j in range(N):
                if bit[j]:
                    print(a[j], end = ' ')
            print()
        elif i == N:
            return
        elif s > t:
            return
        else:
            bit[i] = 1
            f(i+1, N, s + a[i], t)
            bit[i] = 0
            f(i+1, N, s, t)
            
    
    cnt = 0
    N = 10
    a = [x for x in range(1, N+1)]
    bit = [0] * N
    t = 10
    f(0, N, 0, t)
    print(cnt)
    ```
  
- 순열

  - ```python
    def f(i, N):
        if i == N:
            print(p)
        else:
            for j in range(i, N):
                p[i], p[j] = p[j], p[i]
                f(i+1, N)
                p[i], p[j] = p[j], p[i]
    
    N = 3
    p = [x for x in range(1, N+1)]
    f(0, N)
    ```

  - 



---

### Queue 큐

- 큐의 특성
  - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
  - 선입선출구조(FIFO: First In First Out)
    - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First In)된 원소는 가장먼저 삭제(First Out)된다.

---

### 큐의 선입선출 구조

- 머리 Front
- 꼬리 Rear
- 삽입 enQueue
- 삭제 deQueue

---

### 큐의 사용을 위해 필요한 주요 연산

- enQueue(item)
  - 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산
- deQueue()
  - 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산
- createQueue() 
  - 공백 상태의 큐를 생성하는 연산
- is





---

### 큐의 연산 과정

- 공백 큐 생성 createQueue();
  - front = rear = -1
  - front 마지막으로 삭제된 위치
  - rear 마지막으로 저장된 위치
- 원소 A 삽입 enQueue(A);
  - front += 0, rear += 1
- 원소 반환/삭제
  - front += 1, rear += 0
- 큐가 비어있다.
  - front == rear



---

### 선형큐

- 1차원 배열을 이용한 큐
- 상태
  - 초기 -1
  - 공백 front == rear
  - 포화 rear == n-1



---

### 삽입 : enQueue(item)

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

- ```python
  def enQueue(item):
      global rear
      if isFull() :
          print('Queue_Full')
      else:
          rear = rear + 1
          Q[rear] = item
  ```



---

### 삭제 : deQueue()

- 가장 앞에 있는 원소를 삭제하기 위해

- ```python
  def deQueue():
      if
  ```

- 



---

### 공백상태 및 포화상태 검사

- isEmpty(), isFull()

- 공백 front == rear

- rear == n-1

- ```python
  def isEmpty():
      
  ```



---

### 검색 : Qpeek()

- 가장 앞에 있는 원소를 검색하여 반환하는 연산

  - ```python
    def Qpeek():
        if isEmpty():
            print('Queue_Empty')
    ```



---

### 큐 예시

- ```python
  front = rear = -1
  Q = [0]*10
  # enQueue(1)
  rear += 1
  Q[rear] = 1
  
  #deQueue()
  front += 1
  print(Q[front])
  ```

- 들어간 순서대로 나온다.



---

### 원형 큐

- 초기 공백 상태
  - front = rear = 0
  - 처음에는 0번 비워두고 두번째 바퀴부터 0 채움
  - 한칸 비워둠? 한칸비면 꽉참>?
- Index의 순환
  - front와 rear의 위치가 n-1을 가리킨후 논리적 순환으로 0으로
- rear의 다음칸이 front이면 꽉찬거
- rear == front이면 비어있는거





---

### 우선순위 큐

- Priority Queue
- 선입선출이 아니라 우선순위가 높은 순서대로 먼저 나감
- 트리구조?
- 



---

### 버퍼

- 키보드 버퍼?





---

### BFS

- 너비 우선 탐색

- 너비 우선탐색 깊이 우선 탐색 차이점 개념적으로 정리하기

- ```python
  def BFS(G, V, n):
      visited = [0]* (n+1)
      queue = []
      queue.append(V)
      while queue :
          t = queue.pop(0)
          if not visited[t]:
              visited[t] = True
              visit(t)
          for i in G[t]:
              if not visited[i]:
                  queue.append(i)
  ```

- ```python
  def BFS(G, V, n):
      visited = [0]* (n+1)
      queue = []
      queue.append(V)
      visited[V] = 1
      while queue :
          t = queue.pop(0)
          visit(t)
          for i in G[t]:
              if not visited[i]:
                  queue.append(i)
                  visited[i] = visited[t] + 1
  ```

- 
