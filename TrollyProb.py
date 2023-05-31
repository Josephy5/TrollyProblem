class TrollyStats(object):
    humanValue = 100
    animalValue = 70
    evilValue = -40


class Humans(TrollyStats):
    def __init__(self, numOfHumans, isEvil, numOfEvil):
        self.numOfHumans = numOfHumans
        self.isEvil = isEvil
        self.numOfEvil = numOfEvil

    def setIsEvil(self, value):
        self.isEvil = value

    def setNumOfHumans(self, value):
        self.numOfHumans = value

    def setNumOfEvil(self, value):
        self.numOfEvil = value

    def getIsEvil(self):
        return self.isEvil

    def getNumOfHumans(self):
        return self.numOfHumans

    def getNumOfEvil(self):
        return self.numOfEvil

    def calculate(self):
        total = (self.numOfHumans * self.humanValue) + (self.numOfEvil * self.evilValue)
        return total


class Animal(TrollyStats):
    def __init__(self, numOfAnimal, isEvil, numOfEvil):
        self.numOfAnimal = numOfAnimal
        self.isEvil = isEvil
        self.numOfEvil = numOfEvil

    def setIsEvil(self, value):
        self.isEvil = value

    def setNumOfAnimal(self, value):
        self.numOfAnimal = value

    def setNumOfEvil(self, value):
        self.numOfEvil = value

    def getIsEvil(self):
        return self.isEvil

    def getNumOfAnimal(self):
        return self.numOfAnimal

    def getNumOfEvil(self):
        return self.numOfEvil

    def calculate(self):
        total = (self.numOfAnimal * self.animalValue) + (self.numOfEvil * self.evilValue)
        return total


testStr = "there is a trolley heading towards 5 humans. You can pull the lever to set the track towards a track with 5 cats on it"
strHold = testStr.split()
option = 1
for x in range(len(strHold) - 2):
    if strHold[x].isdigit():
        if "humans" in strHold[x + 1] or "humans" in strHold[x + 2]:
            if option == 1:
                option1Humans = Humans(int(strHold[x]), False, 0)
                if "evil" in strHold[x + 1]:
                    option1Humans.setNumOfEvil(int(strHold[x]))
                option = 2
            else:
                option2Humans = Humans(int(strHold[x]), False, 0)
                if "evil" in strHold[x + 1]:
                    option2Humans.setNumOfEvil(int(strHold[x]))
        else:
            if option == 1:
                option1Animal = Animal(int(strHold[x]), False, 0)
                if "evil" in strHold[x + 1]:
                    option1Animal.setNumOfEvil(int(strHold[x]))
                option = 2
            else:
                option2Animal = Animal(int(strHold[x]), False, 0)
                if "evil" in strHold[x + 1]:
                    option2Animal.setNumOfEvil(int(strHold[x]))
option = 1
option1Value=0
option2Value=0
try:
    option1Value += option1Humans.calculate()
except NameError:
    option1Value += 0
try:
    option2Value += option2Humans.calculate()
except NameError:
    option2Value += 0
try:
    option1Value += option1Animal.calculate()
except NameError:
    option1Value += 0
try:
    option2Value += option2Animal.calculate()
except NameError:
    option2Value += 0

print(option1Value)
print(option2Value)
if option1Value > option2Value:
    print("Pulled Lever")
else:
    print("didn't pulled lever")
print(strHold)

