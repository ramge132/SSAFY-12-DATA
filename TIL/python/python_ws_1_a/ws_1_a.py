""" 
- name 변수에 'Alice' 문자열을 할당한다.
- age 변수에 25 정수를 할당한다.
- height 변수에 5.6 부동 소수점을 할당한다.
- is_student 변수에 True 불린 값을 할당한다.
- 각 변수에 담긴 값을 출력한다.
- f-string을 활용하여 'Alice는 25살이고, 키는 5.6이며 학생 여부는 True입니다.' 문자열을 출력한다.
    - 단, name, age, height, is_student 변수를 사용하여야 한다. 
"""

# 변수 할당
name = "Alice"
age = 25
height = 5.6
is_student = True

# 각 변수 출력
print(name)
print(age)
print(height)
print(is_student)

# f-string을 활용한 출력
print(f"{name}는 {age}살이고, 키는 {height}이며 학생 여부는 {is_student}입니다.")
