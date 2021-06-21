import sys

def selectionSort(table,column):
    List = table
    # Sorts the given list in ascending order 
    for i in range(len(List)): 
      
        # Detects the minimum element
        minEleIndx = i 
        for j in range(i+1, len(List)): 
            if List[minEleIndx][int(column)] > List[j][int(column)]: 
                minEleIndx = j 
              
        # Swaps the minimum with the first     
        List[i], List[minEleIndx] = List[minEleIndx], List[i] 

def main():
    ## Variable Declaration
    List = []
    fileName = ''
    column = 0

    ## Take User Input
    print("Enter the file name:",end='')
    fileName = input()
    print("Select the column you would like to sort:",end='')
    column = input()

    ## Open and Read the values from file to the list
    with open(fileName,"r") as file:
        for i in file.readlines():
            temporary = i.split(" ")
            try:
                lastStr = str(temporary[2]).rstrip("\n")
                List.append((str(temporary[0]), int(temporary[1]),lastStr))
            except:pass

    ## Show the values on the list, read from the file
    print ("This is the original list:") 
    for i in range(len(List)): 
        print(List[i][0],List[i][1],List[i][2])

    ## Calling selectionSort function to sort the values in list
    selectionSort(List,column)
  
    # Shows the sorted list 
    print ("\nThis is the sorted list:") 
    for i in range(len(List)): 
        print(List[i][0],List[i][1],List[i][2])    

main()

