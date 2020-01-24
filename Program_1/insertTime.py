######################################################################
# ## Program: Insertion Sort Algorithm
# ## Author: Lake Peterson
# ## Date: 01/12/2020
# ## Description: Algorithm used for sorting numerical values
# ## Input: Inputs values from data.txt
# ## Output: Outputs values back to another file with the sorted values
#######################################################################

import random
import time

#######################################################################
# ## Function: swap
# ## Description: Swaps the values stored in the array
# ## Parameters: Needs an array and an index in order to swap
# ## Pre-Conditions: Takes in two values
# ## Post-Conditions: Ouputs the two values but swaps the order
#######################################################################

def swap(array, i):

    array[i + 1] = array[i]

#######################################################################
# ## Function: insertionSortAlg
# ## Description: Orders numbers in ascending order
# ## Parameters: Needs an array
# ## Pre-Conditions: Takes in an array of numbers
# ## Post-Conditions: Ouputs an array of sorted numbers
#######################################################################

def insertionSortAlg(array):

    for i in range(1, len(array)):

        key = array[i]
        currentIndex = i - 1

        while(currentIndex >= 0 and array[currentIndex] > key):

            swap(array, currentIndex)
            currentIndex -= 1

        array[currentIndex + 1] = key;

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
    insertionSortAlg(array)

    print("\nLength of the array:", len(array))
    print("Amount of time to sort array:", time.time() - intitializeTime, "\n")

if __name__ == "__main__":

    main()
