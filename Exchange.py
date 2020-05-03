import re

class Exchange:

    def __init__(self):
        self.__markLine = True
        self.__timingLine = False
        self.__subLine = False
        self.__file1 = 'SRTFiles/Prueba1.srt'
        self.__file2 = 'SRTFiles/Prueba2.srt'
        self.__resultFile = 'SRTFiles/Result.srt'
        self.__markList = []
        self.__timingList = []
        self.__subList = []
        self.__resultList = []

    def __obtainTiming(self):
        with open(self.__file1, 'r+') as f:
            for line in f:
                if (self.__markLine):
                    # save
                    self.__markList.append(line)

                    self.__markLine = False
                    self.__timingLine = True

                elif (self.__timingLine):
                    # save
                    self.__timingList.append(line)

                    self.__timingLine = False
                    self.__subLine = True

                elif (self.__subLine):
                    # not to save

                    if line == '\n':    # line is a separating line
                        self.__subLine = False
                        self.__markLine = True

    def __obtainSubs(self):
        with open(self.__file2, 'r+') as f:
            for line in f:
                if (self.__markLine):
                    # not to save

                    self.__markLine = False
                    self.__timingLine = True

                elif (self.__timingLine):
                    # not to save

                    self.__timingLine = False
                    self.__subLine = True

                elif (self.__subLine):
                    # save
                    self.__subList.append(line)

                    if line == '\n':    # line is a separating line
                        self.__subLine = False
                        self.__markLine = True

    def __obtainResultList(self):

        subOffset = 0

        try:
            for i in range(0, len(self.__markList)):

                end = False

                self.__resultList.append(self.__markList[i])
                self.__resultList.append(self.__timingList[i])
                self.__resultList.append(self.__subList[i + subOffset])

                j = i + subOffset + 1
                while not end:
                    if self.__subList[j] != '\n':
                        self.__resultList.append(self.__subList[j])
                        j = j + 1
                    else:
                        self.__resultList.append('\n')
                        subOffset = j - i
                        end = True
        except IndexError:
            print(IndexError)
            print("ERROR: The two files do not contain the same number of lines")

    def __obtainExchangeFile(self):

        exchangeFile = open(self.__resultFile, 'w')
        for line in self.__resultList:
            exchangeFile.write(line)
        exchangeFile.close()

    def runExchange(self):
        self.__obtainTiming()
        self.__obtainSubs()
        self.__obtainResultList()
        self.__obtainExchangeFile()

    def showLists(self):

        print("Marks List: ")
        print(self.__markList)

        print("Timings List: ")
        print(self.__timingList)

        print("Subs List: ")
        print(self.__subList)

        print("Result List: ")
        print(self.__resultList)


convertidor = Exchange()

convertidor.runExchange()
#convertidor.showLists()