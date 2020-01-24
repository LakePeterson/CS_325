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

       if(alpha == float(float(3)/4)):
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

    data = open("data.txt", "r")
    sortedData = open("bad.out", "w")

    alpha = float(float(2)/3)

    for row in data:

        rowNumber = list(map(int, row.split()))
        sortedData.write(' '.join(map(str, badSortAlg(numpy.array(rowNumber[1:]), alpha))))
        sortedData.write('\n')

    data.close()
    sortedData.close()

if __name__ == "__main__":

    main()
