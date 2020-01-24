#######################################################################
## Program: Merge Sort Algorithm
## Author: Lake Peterson
## Date: 01/12/2020
## Description: Algorithm used for sorting numerical values
## Input: Inputs values from data.txt
## Output: Outputs values back to another file with the sorted values
#######################################################################

import random
import time

#######################################################################
# ## Function: splitArray
# ## Description: Splits an array into two even pieces
# ## Parameters: Needs an array
# ## Pre-Conditions: Takes in an array of numbers
# ## Post-Conditions: Ouputs an split array of numbers
#######################################################################

def splitArray(array):

    middlePoint = (len(array) // 2)

    return middlePoint


#######################################################################
# ## Function: mergeSortAlg
# ## Description: Orders numbers in ascending order
# ## Parameters: Needs an array
# ## Pre-Conditions: Takes in an array of numbers
# ## Post-Conditions: Ouputs an array of sorted numbers
#######################################################################

def mergeSortAlg(array):

    if len(array) > 1:

        LeftDivide = array[:splitArray(array)]
        RightDivide = array[splitArray(array):]

        mergeSortAlg(LeftDivide)
        mergeSortAlg(RightDivide)

        leftIndex = 0
        rightIndex = 0
        index = 0

        while(leftIndex < len(LeftDivide) and rightIndex < len(RightDivide)):

            if(LeftDivide[leftIndex] < RightDivide[rightIndex]):

                array[index] = LeftDivide[leftIndex]
                leftIndex += 1

            else:

                array[index] = RightDivide[rightIndex]
                rightIndex += 1

            index += 1

        while(leftIndex < len(LeftDivide)):

            array[index] = LeftDivide[leftIndex]
            leftIndex += 1
            index += 1

        while(rightIndex < len(RightDivide)):

            array[index] = RightDivide[rightIndex]
            rightIndex += 1
            index += 1

        return array

#######################################################################
# ## Function: main
#######################################################################

def main():

    array = []
    arrayLength = int(input("\nPlease input an integer to specify the size of the array: "))

    for i in range(arrayLength):

        value = random.randint(1, 10000)

        array.append(value)

    intitializeTime = time.time()
    mergeSortAlg(array)

    print("\nLength of the array:", len(array))
    print("Amount of time to sort array:", time.time() - intitializeTime, "\n")

if __name__ == "__main__":

    main()
