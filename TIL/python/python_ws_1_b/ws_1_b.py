"""
- numbers 리스트에 1부터 10까지의 정수를 할당한다.
- numbers 리스트의 각 요소를 순회하며, 짝수일 경우 해당 숫자를 출력한다.
- numbers 리스트의 각 요소를 순회하며, 홀수일 경우 해당 숫자를 '홀수'로 출력한다.
- numbers 리스트의 각 요소를 순회하며, 숫자가 5일 경우 반복을 종료한다. 
"""

# numbers 리스트에 1부터 10까지의 정수를 할당
numbers = list(range(1, 11))

# 리스트의 각 요소를 순회하며 조건에 따라 출력
for number in numbers:
    if number == 5:
        break
    if number % 2 == 0:
        print(number)
    else:
        print(f"{number}은(는) 홀수")
