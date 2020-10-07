"""My first python class code"""

class Details:
    def biodata(self):
        name=['Samuel' 'Okoth' 'Wanjare']
        age=34
        gender='Male'
        bio=print(f'{name} {age} {gender}')

    def others(self):
        occup = 'Engineer'
        relig = 'Christian'
        marit = 'Single'
        det=print(occup+' '+relig+' '+marit)

def main():
    samsam=Details()
    samsam.biodata()
    samsam.others()

if __name__ == "__main__":
    main()



