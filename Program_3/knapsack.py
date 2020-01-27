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

def knapSack(bagCap, numItems, weightArr, valueArr):

    row = numItems + 1
    column = bagCap + 1

    sack = [[0 for x in range(column)] for x in range(row)]

    for rowIndex in range(row):

        for columnIndex in range(column):

            if(columnIndex == 0 or rowIndex == 0):

                sack[rowIndex][columnIndex] = 0

            elif(weightArr[rowIndex - 1] <= columnIndex):

                pickItem = valueArr[rowIndex - 1] + sack[rowIndex - 1][columnIndex-weightArr[rowIndex - 1]]
                dPickItem = sack[rowIndex - 1][columnIndex]
                sack[rowIndex][columnIndex] = max(dPickItem,  pickItem)

            else:

                dPickItem = sack[rowIndex - 1][columnIndex]
                sack[rowIndex][columnIndex] = dPickItem

    return sack[numItems][bagCap]

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
