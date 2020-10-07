#Constructor class or the __init__ class

class Samsam:

     def __init__(self, name, occup):
         self.name = name
         self.occup = occup


     def greetings(self):
         print('Hi '+self.occup+' '+self.name)


     def intro(self):
         print('Am '+self.name+' a '+self.occup)


def main():
    suzy = Samsam('Okoth', 'Engineer')
    suzy.greetings()
    suzy.intro()

    jontez = Samsam('Johny', 'Driver')
    jontez.greetings()
    jontez.intro()


if __name__ == "__main__":
    main()

    
