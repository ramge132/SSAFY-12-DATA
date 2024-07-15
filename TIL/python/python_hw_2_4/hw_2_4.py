""" 
- Animal 클래스를 정의한다.
    - Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
    - Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
- Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
    - Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
    - Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.
- Flyer와 Swimmer 클래스를 정의한다.
    - Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
    - Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
- Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
    - Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
    - Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.
- make_animal_speak 함수를 정의한다.
    - 이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
- 코드를 실행하고, 출력 결과를 확인한다. 
"""

# Animal 클래스 정의
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Dog 클래스 정의 (Animal 상속)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Cat 클래스 정의 (Animal 상속)
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Flyer 클래스 정의
class Flyer:
    def fly(self):
        return "Flying"

# Swimmer 클래스 정의
class Swimmer:
    def swim(self):
        return "Swimming"

# Duck 클래스 정의 (Animal, Flyer, Swimmer 상속)
class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        return "Quack!"

# make_animal_speak 함수 정의
def make_animal_speak(animal):
    print(animal.speak())

# 객체 생성 및 함수 호출
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Daffy")

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(duck)

# Flyer 및 Swimmer 기능 테스트
print(duck.fly())
print(duck.swim())
