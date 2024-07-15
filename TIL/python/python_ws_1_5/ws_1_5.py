""" 
- movies리스트를 순회하며 영화 제목과 평점을 가진 딕셔너리 객체로 만들고 새로운 리스트에 담는다.
- get_high_rated_movies 함수를 정의하여, threshold 매개변수를 받아서 평점이 threshold 이상인 영화를 리스트로 반환한다.
- 사용자로부터 평점 기준을 입력받아, get_high_rated_movies 함수를 호출하여 해당 평점 이상인 영화를 출력한다. 
"""

movies =  ['Inception', 'Interstellar', 'Dunkirk', 'Tenent']
ratings = [9, 8.5, 7.5, 6]

new_movies_list = []
for title, rating in zip(movies, ratings):
    temp_dict = {'title': title, 'rating': rating}
    new_movies_list.append(temp_dict)
print(new_movies_list)

# 리스트 컴프리헨션 버전
#comp_movies = [{'title': title, 'rating': rating} for title, rating in zip(movies,ratings)]

def get_high_rated_movies(threshold):
    high_rated_movies = []
    for i in range(len(movies)):
        if ratings[i] >= threshold:
            high_rated_movies.append(movies[i])
    return high_rated_movies

threshold = int(input('Enter the rating threshold: '))
print(f"Movies with a rating of {threshold:.1f} or higher")
high_rated_movies = get_high_rated_movies(threshold)
for movie in high_rated_movies:
    print(movie)
