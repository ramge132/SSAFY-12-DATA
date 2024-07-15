""" 
모든 학생의 평균 점수를 계산하여 출력하시오.
80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오. 
"""

students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eve": 95
}

print("1. 학생들의 이름과 점수를 딕셔너리에 저장")
print(f"students type: {type(students_scores)}")

average_score = sum(students_scores.values()) / len(students_scores)
print(f"2. 모든 학생의 평균 점수: {average_score}")

students_above_80 = [name for name, score in students_scores.items() if score >= 80]
print(f"3. 기준 점수(80점) 이상을 받은 학생 수: {students_above_80}")

sorted_students = sorted(students_scores.items(), key=lambda item: item[1], reverse=True)
print("4. 점수 순으로 정렬:")
for name, score in sorted_students:
    print(f"{name}: {score}")

max_score = max(students_scores.values())
min_score = min(students_scores.values())
score_difference = max_score - min_score
print(f"5. 점수가 가장 높은 학생과 낮은 학생의 점수 차이: {score_difference}")

print("6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")
for name, score in students_scores.items():
    if score < average_score:
        print(f"{name} 학생의 점수는 평균 이하입니다.")
    else:
        print(f"{name} 학생의 점수는 평균 이상입니다.")
