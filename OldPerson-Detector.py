class Person:
    #CONSTRUCTOR METHODE initializing
    def __init__(self,initialAge):
        self.age = initialAge
        if self.age<0:
            print('Age is not valid,setting age to 0.')
            self.age = 0

    #METHODE for printing age
    def AmiOld(self):
        if self.age<13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')

    #METHODE for incrieasing age
    def yearPasser(self):
        self.age+=1

if __name__=='__main__':
    t = int(input())
    for i in range(0,t):
        age = int(input())
        p = Person(age)
        p.AmiOld()
        for j in range(0,3):
            p.yearPasser()

        p.AmiOld()
        print('')