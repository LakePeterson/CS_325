#######################################################################
# ## Program: Change Algorithm
# ## Author: Lake Peterson
# ## Date: 02/03/2020
# ## Description: Algorithm used to find change for any set of different coin denominations
# ## Input: Inputs values from data.txt
# ## Output: Outputs the coin denomimnations to a file
#######################################################################

import sys

#######################################################################
# ## Global Variables
#######################################################################

makeChangeAnswer = [[], []]
coinArray = []

#######################################################################
# ## Function: createArray
# ## Description: Creates an array based off on the n and k values
# ## Parameters: Needs two integer values and an array
# ## Pre-Conditions: Takes in two values and an array
# ## Post-Conditions: Return the array that was created.
#######################################################################

def createArray(n, k, coin):

    for index in range(0, k + 1):

        coin.append(n**index)

    return coin

#######################################################################
# ## Function: makeChangeAlg
# ## Description: Correctly calculates the change using greedy approach
# ## Parameters: Needs an array and the limit to the amount of change
# ## Pre-Conditions: Takes in one array, as well as change limit
# ## Post-Conditions: Return the correct change denominations
#######################################################################

def makeChangeAlg(coin, changeAmount):

    if(changeAmount == 0):

        return 0

    for index in reversed(coin):

        tracker = index

        if(changeAmount >= tracker):

            if tracker not in makeChangeAnswer[0]:

                makeChangeAnswer[0].append(tracker)
                makeChangeAnswer[1].append(1)

            else:

                makeChangeAnswer[1][makeChangeAnswer[0].index(tracker)] += 1

            return (makeChangeAlg(coin, changeAmount - tracker) + 1)

    return 0

#######################################################################
# ## Function: main
#######################################################################

def main():

    saveOutput = sys.stdout;
    data = open("data.txt", "r")
    changeData = open("change.txt", "w");

    for row in data:

        del coinArray[:]
        del makeChangeAnswer[0][:]
        del makeChangeAnswer[1][:]

        rowNumber = list(map(int, row.split()))
        tempArray = createArray(rowNumber[0], rowNumber[1], coinArray)
        makeChangeAlg(tempArray, rowNumber[2])
        sys.stdout = changeData

        for index in range(0, len(makeChangeAnswer[0])):

            print(makeChangeAnswer[0][index], " ", makeChangeAnswer[1][index])

        print("\n")
        sys.stdout = saveOutput

    changeData.close()
    data.close()

if __name__ == "__main__":

    main()
