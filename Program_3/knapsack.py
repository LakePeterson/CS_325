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
# ## Description: Finds the optimal subset from based off of the data
# ## Parameters: Needs an array of weights and an array of values
# ## Pre-Conditions: Takes in an two arrays, as well as capacity and number of items
# ## Post-Conditions: Return the optimal subset
#######################################################################

def knapSack(bagCap, numItems, weightArr, valueArr):

    row = numItems + 1
    column = bagCap + 1

    sack = [[0 for x in range(column)] for x in range(row)]                                         #Declaring/seeding an array to represent the knapsack

    for rowIndex in range(row):                                                                     #Traverse through the sack to find the optimal
                                                                                                    #optimal subset from the data.
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

    return sack[numItems][bagCap]                                                                   #Return the optimal subset

#######################################################################
# ## Function: main
#######################################################################

def main():

    data = open("data.txt", "r")                                                                    #Open the file data.txt

    for row in data:                                                                                #Set the weight array equal to the first
        weightArr = list(map(int, row.split(' ')))                                                  #row of data
        break;
    for row in data:                                                                                #Set the value array equal to the second
        valueArr = list(map(int, row.split(' ')))                                                   #row of data

    data.close()

    optimalSubset = knapSack(6, len(valueArr), weightArr, valueArr)

    print("The optimal subset is:", optimalSubset)                                                 #Print out the optimal subset

if __name__ == "__main__":

    main()
