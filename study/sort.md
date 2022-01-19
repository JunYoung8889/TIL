# sort 정렬

### 버블 정렬

- 싸움짱을 뽑자!

- ```python
  nums =[ 5, 8, 2, 6, 3, 1, 7, 4 ]
  
  # len() 없이 해보자!
  cnt = 0
  for i in nums:
      cnt +=1
      
  sort_cnt = 0
  print(sort_cnt,nums,'\n')
  
  for i in range(cnt-1):
      for j in range(cnt-1-i):
          if nums[j] > nums[j+1]:
              nums[j], nums[j+1] = nums[j+1], nums[j]
              sort_cnt += 1
              print(sort_cnt,nums,'\n')
  ```





---

### 삽입 정렬

- 자리찾고 밀어내기!

- ```python
  nums =[ 5, 8, 2, 6, 3, 1, 7, 4 ]
  
  # len() 없이 해보자!
  cnt = 0
  for i in nums:
      cnt +=1
      
  sort_cnt = 0
  print(sort_cnt,nums,'\n')
  
  for i in range(cnt-1):
      for j in range(i+1):
          if nums[i+1] < nums[j]:
              temp = nums[i+1]
              for k in range(i,j-1,-1):
                  nums[k+1] = nums[k]
              nums[j] = temp
              sort_cnt += 1
              print(sort_cnt,nums,'\n')
  ```







---

### 선택 정렬

- 순서대로 불러서 줄세우기!

- ```python
  nums =[ 5, 8, 2, 6, 3, 1, 7, 4 ]
  
  # len() 없이 해보자!
  cnt = 0
  for i in nums:
      cnt +=1
      
  sort_cnt = 0
  print(sort_cnt,nums,'\n')
  
  for i in range(cnt-1):
      min_num = nums[i]
      for j in range(i+1,cnt,1):
          if min_num > nums[j]:
              min_num = nums[j]
              nums[i],nums[j] = min_num,nums[i]
              sort_cnt += 1
              print(sort_cnt,nums,'\n')
  
  ```