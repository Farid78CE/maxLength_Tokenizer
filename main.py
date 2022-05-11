import os
import typing
from hazm import *
import time


class Util:
    def listToDictionary(self, lst: list):
        dictionary = {lst[i]: 0 for i in range(0, len(lst))}
        dictionary_copy = self.removeBackSlashN(dictionary)
        # print(dictionary_copy)
        return dictionary_copy

    @classmethod
    def removeBackSlashN(self, dictionary):
        # below code is removing \n from end of each keys in the dictionary: for example {"by\n":0} -> { "by":0 }
        dictionary_copy = {}
        for keys in dictionary.keys():
            str = keys.strip()
            dictionary_copy[str] = 0
        return dictionary_copy


class Tokenizer:
    counter: int = 1
    flag: bool = False

    def readFile(self, language):
        current: str = ""
        current = os.getcwd()
        if self.counter == 1:
            self.counter += 1
            os.chdir(current + "\\Samples")
            current = os.getcwd()

        listOfWords: list = []

        if language == "english":
            try:
                print(os.getcwd())
                readEnglishFile = open(f"{os.getcwd()}\\en.tokens.en", "r", encoding="utf8")
                for words in readEnglishFile:
                    listOfWords.append(words)
            except Exception as e:
                print(str(e))
        elif language == "farsi":
            try:
                readEnglishFile = open(f"{os.getcwd()}\\fa.words.txt", "r", encoding="utf8")
                for words in readEnglishFile:
                    listOfWords.append(words)
            except Exception as e:
                print(str(e))
        else:
            print("Not a Valid language")

        return listOfWords

    def readMergedFiles(self):
        readfarsiMergedFile = open(os.getcwd() + "\\mergedTokens.fa", "r", encoding="utf8")
        readEnglishMergedFile = open(os.getcwd() + "\\mergedTokens.en", "r", encoding="utf8")

        listOfFarsiMergedList: list = []
        listOfEnglishMergedList: list = []

        for farsiMergedPhrases in readfarsiMergedFile:
            listOfFarsiMergedList.append(farsiMergedPhrases)

        for englishMergedPhrases in readEnglishMergedFile:
            listOfEnglishMergedList.append(englishMergedPhrases)

        return (listOfFarsiMergedList, listOfEnglishMergedList)

    def tokenize(self, listOfFarsiWords: list, listOfEnglishWords: list, listOfFarsiMergedWords: list,
                 listOfEnglishMergedWords: list):
        # util = Util()
        # englishDictionary = util.listToDictionary(listOfEnglishWords)
        # farsiDictionary = util.listToDictionary(listOfFarsiWords)

        for index, word in enumerate(listOfFarsiWords):
            temp = listOfFarsiWords[index].strip()
            temp = "".join([i for i in temp if not i.isdigit()])
            listOfFarsiWords[index] = temp
            print(listOfFarsiWords[index])

        for index, word in enumerate(listOfEnglishWords):
            temp = listOfEnglishWords[index].strip()
            listOfEnglishWords[index] = temp

        word: str = ""
        maxLength: list = []
        chosenWord: str = []
        savedIndex: int = 0
        counter: int = 0
        tokenizedString: str = ""
        tempChar = ""
        tokenizedList: list = []
        for eachMergedPharase in listOfEnglishMergedWords:
            eachMergedPharase = eachMergedPharase.strip()
            while (True):

                word += eachMergedPharase[counter]

                if word in listOfEnglishWords:
                    maxLength.append(word)

                if counter == len(eachMergedPharase) - 1:
                    try:
                        chosen = max(maxLength)
                        eachMergedPharase = eachMergedPharase.replace(chosen, "")
                        tokenizedString = tokenizedString + chosen + " "
                        word = ""
                        counter = -1
                        maxLength = []
                    except Exception as e:
                        print(str(e))
                        print("Empty max ")
                        eachMergedPharase = eachMergedPharase.replace(word, "")

                if len(eachMergedPharase) == 0:
                    tokenizedList.append(tokenizedString)
                    counter = 0
                    word = ""
                    maxLength = []
                    tokenizedString = ""
                    break

                counter += 1

        englishFile = open(os.getcwd() + "\\97463130_Assignment2_EN", "a", encoding="utf8")
        for i in range(0, len(tokenizedList)):
            englishFile.write(str(tokenizedList[i]) + "\n")
        englishFile.close()

'''        word = ""
        maxLength = []
        chosenWord = []
        savedIndex = 0
        counter = 0
        tokenizedString = ""
        tempChar = ""
        tokenizedList = []'''

'''        for eachMergedPharase in listOfFarsiMergedWords:
            eachMergedPharase = eachMergedPharase.strip()
            while (True):

                word += eachMergedPharase[counter]

                if word in listOfFarsiWords:
                    maxLength.append(word)

                if counter == len(eachMergedPharase) - 1:
                    try:
                        chosen = max(maxLength)
                        eachMergedPharase = eachMergedPharase.replace(chosen, "")
                        tokenizedString = tokenizedString + chosen + " "
                        word = ""
                        counter = -1
                        maxLength = []
                    except Exception as e:
                        print(str(e))
                        print("Empty max ")
                        eachMergedPharase = eachMergedPharase.replace(word, "")

                if len(eachMergedPharase) == 0:
                    tokenizedList.append(tokenizedString)
                    counter = 0
                    word = ""
                    maxLength = []
                    tokenizedString = ""
                    break

                counter += 1


        print(str(tokenizedList))
        englishFile = open(os.getcwd() + "\\97463130_Assignment2_FA", "a", encoding="utf8")
        for i in range(0, len(tokenizedList)):
            englishFile.write(str(tokenizedList[i]) + "\n")
        englishFile.close()'''


if __name__ == '__main__':
    tokenizer = Tokenizer()
    listOfEnglishWords = tokenizer.readFile("english")
    listOfFarsiWords = tokenizer.readFile("farsi")
    getMergedFiles = tokenizer.readMergedFiles()  # getMergedFiles is tuple
    listOfFarsiMergedPharases = getMergedFiles[0]
    listOfEnglishMergedPharases = getMergedFiles[1]
    tokenizer.tokenize(listOfFarsiWords, listOfEnglishWords, listOfFarsiMergedPharases, listOfEnglishMergedPharases)
