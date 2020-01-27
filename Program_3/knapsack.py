#######################################################################
# ## Program: Knapsack Algorithm
# ## Author: Lake Peterson
# ## Date: 01/21/2020
# ## Description: Algorithm used for finding optimal subsets
# ## Input: Inputs values from data.txt
# ## Output: Outputs the optimal subset to the terminal
#######################################################################

#######################################################################
# ## Function: knapsackAlg
# ## Description: Finds the opt
# ## Parameters: Needs an array
# ## Pre-Conditions: Takes in an array of numbers
# ## Post-Conditions: Ouputs an array of sorted numbers
#######################################################################

def knapSack(bagCap, itemNum, weightArr, valueArr):

    sackArr = [[0 for x in range(bagCap + 1)] for x in range(itemNum + 1)]

    for indexRow in range(itemNum + 1):

        for indexColumn in range(bagCap + 1):

            if(indexRow == 0 or indexColumn == 0):

                sackArr[indexRow][indexColumn] = 0

            elif weightArr[indexRow-1] >= indexColumn:

                pickItem = (valueArr[indexRow-1] + sackArr[indexRow-1][indexColumn - weightArr[indexRow-1]])
                dnPickItem = (sackArr[indexRow-1][indexColumn])

                sackArr[indexRow][indexColumn] = max(pickItem, dnPickItem)

            else:

                dnPickItem = sackArr[indexRow-1][indexColumn]

                sackArr[indexRow][indexColumn] = dnPickItem

    return sackArr[itemNum][bagCap]

#######################################################################
# ## Function: main
#######################################################################

def main():

    data = open("data.txt", "r")

    for row in data:
        weightArr = list(map(int, row.split(' ')))
        break;
    for row in data:
        valueArr = list(map(int, row.split(' ')))

    data.close()

    print(knapSack(6, len(valueArr), weightArr, valueArr))

if __name__ == "__main__":

    main()
