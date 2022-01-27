# oop

### 들어가기 전에

- 함수를 학습했던 순간을 떠올려 봅시다.

- ```python
  def add(x,y):
      return x+y
  
  a = add(3,5)
  print(a, type(a))
  ```

- ```python
  a = [1,2,3]
  print(type(a))
  print(a)
  a.append(4)
  print(a)
  ```
  
- ```python
  a = ['1','2','3']
  b = map(int, a)
  print(b)
  print(type(b))

---

```python
class Person:
    def __init__(self, name, age):
        # 인스턴스 변수를 정의하기 위해 사용!
        self.name = name
        self.age = age

    def greeting(self):
        print('안녕하세요 '+self.name,str(self.age)+'입니다.')

jimin = Person('지민',20)
jimin.greeting()
```

```python
class Person:

    def greeting(self):
        print('안녕하세요 '+self.name,str(self.age)+'입니다.')

jimin = Person()
jimin.name = '지민'
jimin.age = 20
jimin.greeting()
```

```python
class ListTest:
    def append_02(self,a):
        self.list = self.list + [a]
        return self.list

test = ListTest()
print(test)
print(type(test))
test.list = [1,2,3]
print(test.list)
test.append_02(4)
print(test.list)
print(type(test.list))
```

```python
class ListTest:

    def __init__(self, list):
        self.list = list

    def append_02(self,a):
        self.list = self.list + [a]
        return self.list

c = [1,2,3]
test = ListTest(c)
test.append_02(4)
print(test.list)
```

```python
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    # 매직 메소드 활용해보자!
    def __gt__(self, other):
        return self.age > other.age
    def __len__(self):
        return self.height
    def __str__(self):
        return f'<{self.name}> : {self.age}살'
        #<main.Person object at 0x0000014A79EE5DC0> => <재영> : 100살
        # map처럼 더럽게 출력되는 부분을 개발자가 보기 편하게 str형태로 확인가능

p1 = Person('재영',100,190)
p2 = Person('지선',10,185)
print(p1 > p2)
print(len(p1))
print(len(p2))
print(p1)
print(dir(p1))
```

```python
class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r
    def area(self):
        return Circle.pi * self.r * self.r

c1 = Circle(2)
c2 = Circle(3)
print(c1.pi, id(c1.pi))
print(Circle.pi, id(Circle.pi))
print(c2.pi, id(c2.pi))
print(c1.r)
print(c1.area())
```

---

```python
class Person:
    population = 0
    
    @staticmethod
    def add_population():
        Person.population += 1
        
class Student(Person):
    population = 0
        
Person.add_population()
print(Person.population) # 1

Student.add_population()
print(Student.population) # 0
```

```python
class Person:
    population = 0
    
    @classmethod
    def add_population(cls):
        cls.population += 1
        
class Student(Person):
    population = 0
    
        
Person.add_population()
print(Person.population) # 1

Student.add_population()
print(Student.population) # 1
```

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def talk(self):
        print(f'충성충성! {self.name}입니다. 교수님. ^^7')

s1 = Student('승운', 20, 4.5)
s1.talk()
```

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def talk(self):
        print(f'충성충성! {self.student_id} {self.name}입니다. 교수님. ^^7')

s1 = Student('준영', 28, '20141648')
s1.talk()
```

```python
class A:
    name = 'A'
class B(A):
    name = 'B'
class C(A):
    name = 'C'
class D(B, C):
    pass
d = D()
print(d.name)
```

```python
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    def get_age(self):
        return self._age
    
p1 = Person('송지', 23)
print(p1._age) # 가능은 하지만, 암묵적으로 이렇게 하지말자
print(p1.get_age())
```

```python
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
p1 = Person('송지', 23)
#print(p1.__age) 불가능 
print(p1.get_age())
```

```python
class Person:
    
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age - 10
    
p1 =Person(30)
print(p1.age)
```



