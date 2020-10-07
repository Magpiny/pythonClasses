import bigetti
from bigetti import Bighead

class Inherit(Bighead):
   pass


terry =  Inherit('Geeky', 'Sam')
terry.passwd('Sam', 1235)
print(terry.fname)


#if __name__ == "__main__":
 #   main()
