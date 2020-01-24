#######################################################################
# ## Program: Insertion Sort Algorithm
# ## Author: Lake Peterson
# ## Date: 01/12/2020
# ## Description: Algorithm used for sorting numerical values
# ## Input: Inputs values from data.txt
# ## Output: Outputs values back to another file with the sorted values
#######################################################################

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

    data = open("data.txt", "r")
    sortedData = open("insert.out", "w")

    for row in data:

        rowNumber = list(map(int, row.split()))
        sortedData.write(' '.join(map(str, insertionSortAlg(rowNumber[1:]))))
        sortedData.write('\n')

    data.close()
    sortedData.close()

if __name__ == "__main__":

    main()
