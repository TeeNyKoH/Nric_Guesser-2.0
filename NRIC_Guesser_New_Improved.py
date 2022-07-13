import math
from bisect import bisect_left

yearDict = {2021: 38672, 2020: 38590, 2019: 39279, 2018: 39039, 2017: 39615, 2016: 41251, 2015: 42185, 2014: 42232,
            2013: 39720, 2012: 42663, 2011: 39654, 2010: 37967, 2009: 39570, 2008: 39826, 2007: 39490, 2006: 38317,
            2005: 37492, 2004: 37174, 2003: 37485, 2002: 40760, 2001: 41451, 2000: 46997, 1999: 43336, 1998: 43664,
            1997: 47333, 1996: 48577, 1995: 48635, 1994: 49554, 1993: 50225, 1992: 49402, 1991: 49114, 1990: 51142,
            1989: 47669, 1988: 52957, 1987: 43616, 1986: 38379, 1985: 42484, 1984: 41556, 1983: 40585, 1982: 42654,
            1981: 42250, 1980: 41217, 1979: 40779, 1978: 39441, 1977: 38364, 1976: 42783, 1975: 39948, 1974: 43268,
            1973: 48269, 1972: 49678, 1971: 47088, 1970: 45934, 1969: 44562, 1968: 47241, 1967: 50560, 1966: 54680,
            1965: 55725, 1964: 58217, 1963: 59530, 1962: 58977, 1961: 59930, 1960: 61775}
list11 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198]
def getMonth():
    print("Enter your bith month in numbers e.g feb = 02 and dec = 12: ")
    month = int(input())
    return month

def getYear():
    print("Enter your bith year: ")
    year = int(input())
    return year

def getLast4():
    print("Enter the last 4 digits of your NRIC(E.g 321A): ")
    last4 = input()
    return last4

def getTotalBirth(year):
    totalBirths = yearDict[year]
    return totalBirths

def splitYear(year):
    #Function is to split year into each individual digit and add it into a list
    #so that I can access only the last 2 digit
    yearls = [
    (year // (10**i)) % 10 for i in range(math.ceil(math.log(year, 10)) - 1, -1, -1)]
    return yearls

def calWeight(yearSplit , last4 ):#function is to calculate the weight of all all the numbers that are given to us
    #ie the first 2 and the last 4 digits of the nric
    one = yearSplit[2] * 2
    two = yearSplit[3] * 7
    five = int(last4[0]) * 4
    six = int(last4[1]) * 3
    seven = int(last4[2]) * 2
    weight = one + two + five + six + seven
    if yearSplit[0] == 2:
        weight= weight + 4

    return weight 

def calWeightLetter(yearSplit , last4):
    letter = last4[3].upper()
    

    if yearSplit[0] == 1 or 2:
        if letter == "J":
            remainder = 0
        if letter == "Z":
            remainder = 1
        if letter == "I":
            remainder = 2
        if letter == "H":
            remainder = 3
        if letter == "G":
            remainder = 4
        if letter == "F":
            remainder = 5
        if letter == "E":
            remainder = 6
        if letter == "D":
            remainder = 7
        if letter == "C":
            remainder = 8
        if letter == "B":
            remainder = 9
        if letter == "A":
            remainder = 10
    return remainder

def getPotentialCorrectAnswers(weight , remainder):
    sumlist = []
    for i in list(list11):
        i = i - weight
        i = i + remainder
        if i >= 0:
            sumlist.append(i)
            #Sumlist is a list that adds the remainder we got from the letter into a list of multipliers of 11, we then
    
    seperatedigitlist = []
    for sum in sumlist:
        for i in range(sum):
            x = 6 * i #6 is the weight of the third number in the nric
            for j in range(sum):
                y = 5 * j #5 is the weight of the fourth number in the nric
                if x + y == sum:
                    # print(sum)
                    seperatedigitlist.append(i)
                    seperatedigitlist.append(j) 
                    #seperatedigitlist is a list containing the possible answers however we need combine every 2 digits and add it into a new list
    #to remove any numbers in the list that are not usable. as stated above they are a pair of numbers, so if the even digit
    #is removed, it has to remove the odd one also. and if the odd on is removec, it has the remove the digit before it(even)
    for u in seperatedigitlist:
        if u >= 10:
            index = seperatedigitlist.index(u)
            if index % 2 == 0:

                seperatedigitlist.pop(index)
                seperatedigitlist.pop(index)
            else:
                seperatedigitlist.pop(index)
                seperatedigitlist.pop(index - 1)

    listToStr = "".join([str(elem) for elem in seperatedigitlist])#convert list to string
    n=2
    tlist = [listToStr[i : i + n] for i in range(0, len(listToStr), n)] # to add every 2 numbers into the list tlist
    
    tlist = sorted(tlist)

    #in the event of converting string to int, 01 will become 1 no matter what, to stop that from happening, we need to add it manually.
    for i in tlist:
        if len(i) == 1:
            n = i + "0"
            tlist.remove(i)
            tlist.append(n)

    #remove duplicate
    def remove_duplicates_recursion(dupList, temp):
        if len(dupList) == 0:  # condition 0 --> base case
            return dupList
        if dupList[0] in temp:  # condition 1
            temp.append(dupList[0])
            return remove_duplicates_recursion(dupList[1:], temp)
        else:  # condition 2
            temp.append(dupList[0])
            return [dupList[0]] + remove_duplicates_recursion(dupList[1:], temp)

    #remove duplicate
    def remdup(l, dup=None):
    # If has zero or one elements, there are no duplicates.
        if len(l) < 2:
            return l

        # If there's a duplicate to remove, remove it and recurse until ValueError
        # is raised, which means there are none left to remove. Since lists are
        # mutable, we don't have to capture this.
        if dup is not None:
            try:
                l.remove(dup)
                remdup(l, dup)
            except ValueError:
                pass

        # No more duplicates to remove? Then recurse, removing duplicates of the
        # current head!
        return [l[0]] + remdup(l[1:], l[0])


    tlist = sorted(tlist)
    tlist1 = []
    remdup(tlist)
    remove_duplicates_recursion(tlist, tlist1) #running twice because code cant seem to work well


    ttlist000 = []
    for t in tlist1:
        a = t + "000"
        ttlist000.append(a)
    #add another 3 zeros at the back so that in the below steps i can choose the nearest number from this list


    return ttlist000



def chooseNearestAns(last4 , totalBirths , month , getPotentialCorrectAnswers):
    # choose1 = (totalBirths / 12) * month
    # choose1 = choose1 * (1 - ((month / 12) / 2))
    #old Algorithm that wasnt very accurate.
    #Working algorithm was inspired by https://github.com/limyeechern/nric-guesser
    position = abs(int(last4[0:3]) - totalBirths * ((month-0.5)/ 12))



    def take_closest(myList, myNumber):
        """
        Assumes myList is sorted. Returns closest value to myNumber.

        If two numbers are equally close, return the smallest number.
        """
        pos = bisect_left(myList, myNumber)
        if pos == 0:
            return myList[0]
        if pos == len(myList):
            return myList[-1]
        before = myList[pos - 1]
        after = myList[pos]
        if after - myNumber < myNumber - before:
            return after
        else:
            return before

    for i in range(0, len(getPotentialCorrectAnswers)):
        getPotentialCorrectAnswers[i] = int(getPotentialCorrectAnswers[i])
        
    finans = take_closest(getPotentialCorrectAnswers, round(position))
    # print(finans)

    if len(str(finans)) == 1: #add 0 in front of any 4 digit numbers as the nric is 5 digits (s/t YY xxxxx Letter)
        finans = str(finans)
        finans = "0" + finans
    
    return finans


def getNric(year , last4 , position):
    if year[0] == 1:
        letter = "S"
    else:
        letter = "T"

    nric = letter + str(year[2]) + str(year[3]) + str(position)[:2] + str(last4)
    return print("My best guess of your Nric is: " , nric)

    

month = getMonth()
year = getYear()
last4 = getLast4()
totalBirths = getTotalBirth(year)
yearSplit = splitYear(year)
weight = calWeight(yearSplit , last4 )
remainder = calWeightLetter(yearSplit , last4)
potCorrectAns = getPotentialCorrectAnswers(weight , remainder) #this is the list that gives all the potential correct answers
position = chooseNearestAns(last4 , totalBirths , month , potCorrectAns)
NRIC = getNric(yearSplit , last4, position)

# print(month , yearSplit[2],yearSplit[3] , last4 , totalBirths , weight)
# print("tlist1" , potCorrectAns)
# print("Position" , position)

# print("Your Nric is ")
