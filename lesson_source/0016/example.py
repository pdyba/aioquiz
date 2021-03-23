class Creature:
    alive = True

    def is_live(self):
        print('I am alive')

    def is_dead(self):
        if self.alive:
            self.live()
            return True
        print('I am dead')
        return False

    def kill(self):
        alive = False


class Animal(Creature):
    def eat(self):
        print('chrum chrum')


class Manmal(Animal):
    def __init__(self, sex, height, weight=100):
        self.sex = sex
        self.height = height
        self.weight = weight
        self.bmi = weight / height ** 2

    @classmethod
    def get_name(cls):
        return cls.__name__


class Cow(Manmal):
    def __init__(self, name, *args, surname="superKorwa", **kwargs):
        print(args)
        print(*args)
        print(kwargs)
        super().__init__(*args, **kwargs)
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.get_name()} - {self.name} {self.surname}"


krowa = Cow("Ala", "female", 200, weight=999, surname="Nord")
print(krowa)
print(krowa.weight)


def arg_test(*args, **kwargs):
    print(args)
    print(kwargs.get("z", kwargs.get("k")))

arg_test(1,2,3123,123, k=12, p=90, w=30)