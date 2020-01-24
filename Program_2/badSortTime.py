#######################################################################
# ## Program: Bad Sort Algorithm
# ## Author: Lake Peterson
# ## Date: 01/21/2020
# ## Description: Algorithm used for sorting numerical values
# ## Input: Inputs values from data.txt
# ## Output: Outputs values back to another file with the sorted values
#######################################################################

import math
import numpy
import time
import random

#######################################################################
# ## Function: insertionSortAlg
# ## Description: Orders numbers in ascending order
# ## Parameters: Needs an array
# ## Pre-Conditions: Takes in an array of numbers
# ## Post-Conditions: Ouputs an array of sorted numbers
#######################################################################

def badSortAlg(array, alpha):

    length = len(array)

    if((length == 2) and (array[0] > array[1])):

       temp = array[0]
       array[0] = array[1]
       array[1] = temp

    elif(length > 2):

        if(alpha == 3/4):
            m = int(math.floor(alpha * length))
        else:
            m = int(math.ceil(alpha * length))

        badSortAlg(array[:m], alpha)
        badSortAlg(array[length - m:length], alpha)
        badSortAlg(array[:m], alpha)

    return array

#######################################################################
# ## Function: main
#######################################################################

def main():

    array = []
    alpha = float(float(3)/4)
    arrayLength = int(input("\nPlease input an integer to specify the size of the array: "))

    for i in range(arrayLength):

        value = random.randint(1, 10000)
        array.append(value)

    intitializeTime = time.time()
    badSortAlg(numpy.array(array), alpha)
    print("\nLength of the array:", len(array))
    print("Amount of time to sort array:", time.time() - intitializeTime, "\n")

if __name__ == "__main__":

    main()
