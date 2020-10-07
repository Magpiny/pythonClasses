#Another class

class Bighead:
    h_size = 25
    h_radius = 4


    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

        print('Am '+self.fname+' '+self.lname)


    def sam(self, age, gender):
        
        
        print(f'age :{age}yrs and gender :{gender}.')


    def phzk(self, height, skin):
        height=5.3
        skin ='light'
        print(f"height  :{height}. complexion :{skin}.")

    def educ(self, high, uni):
        high='Siaya Township'
        uni ='UoN'
        print('Highschool :'+high+' Uni :'+uni)


    def sibl(self, sib):
        sib = ('Tot', 'Aseo', 'Achita', 'Bena')
        print(sib)


    def passwd(self, usr, passcode):
        usr = str(input('Enter username  '))
        passcode = input('Enter password  ')
        if usr=="" or passcode=="":
            print("password or username can't be empty")
        elif usr =='Sam' and passcode=='1234':
            print(f'WELCOME HOME {usr}')

        else :
            print("Password and username doesn't match!")


    def age(self, age):
        pass


def main():
    bigeti = Bighead('Samuel', 'Okoth')

    print("You'll live for ",bigeti.h_size*bigeti.h_radius, "yrs.")

   # bigeti = Bighead('Samuel', 'Okoth')

    bigeti.sam(21, 'Male')
    bigeti.educ('met', 'eat')


    bigeti.phzk(1, 'y3llo')

    print("My siblings :", bigeti.sibl('ocampo'))


    bigeti.passwd('sam', '1234')





if __name__ == "__main__":
    main()




