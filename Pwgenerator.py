class sambaCracker():

    generatedDict = []
    charList = 'abcdefghijklmnop'

    def __init__(self):
        self.generatePasswords()
        self.fillPwList()

    def generatePasswords(self):
        for current in range(5):
            self.generatedDict = [i for i in self.charList]
            for y in range(current):
                self.generatedDict = [current + i for i in self.charList for current in self.generatedDict]

    def fillPwList(self):
        pwlist = open("pwlist.txt", "w+")
        for password in self.generatedDict:
            pwlist.write(password + ":")
        pwlist.close()


cracker = sambaCracker()
