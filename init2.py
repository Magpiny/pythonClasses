class Shark:
    def __init__(self, name, age):
        self.age = age
        self.name = name


    def weed(self):
        print(self.name+' likes weed ', self.age)


    def actor(self):
        t=' is my favorite actor at '
        print(self.name+t, self.age)


    def sqr(self):
        x = int(input('Get the square of :'))
        y = x*x
        print(f'The square of {x} = {y}')


def main():
    sowd = Shark("Aseo", 27)
    sowd.weed()
    sowd.actor()
    jack = Shark("John", 34)
    jack.weed()
    jack.actor()
    jack.sqr()


if __name__ == "__main__":
    main()
    
