def findPath(arr):
    boolArray = []
    for x in range(len(arr)):
        boolArray.append([])
        for y in range(len(arr[0])):
            boolArray[x].append(False)
    directions = []
    i,j = 1,1
    anchorPoint = [[1,1]]
    count = 0
    while True:
        count+=1
        # Checking down
        try:
            if (arr[j+1][i] != 'ENDING') and (arr[j][i+1] != 'ENDING') and (arr[j-1][i] != 'ENDING') and (arr[j][i-1] != 'ENDING'):
                if (int(arr[j+1][i]) + int(arr[j][i+1]) + int(arr[j-1][i]) + int(arr[j][i-1])) > 2:
                    if [j,i] not in anchorPoint:
                        anchorPoint.append([j,i])
        except:
            pass
        if (arr[j+1][i] == 0) and (boolArray[j+1][i] == False):
            j+= 1
            directions.append("down")
        # checking right next to avoid infinite loop
        elif (i< len(boolArray[0])) and (arr[j][i+1] == 0) and (boolArray[j][i+1] == False):
            i+= 1
            directions.append("right")
        # checking up
        elif(j>0) and (arr[j-1][i] == 0) and (boolArray[j-1][i] == False):
            j -= 1
            directions.append("up")
        #checking left
        elif(i>0) and(arr[j][i-1] == 0) and (boolArray[j][i-1] == False):
            i -= 1
            directions.append("left")
        # if no more moves/ ending is reached
        else:
            if(arr[j][i] == "ENDING"):
                print("solved")
                break
            else:
                j = anchorPoint[-1][0]
                i = anchorPoint[-1][1]
                directions=directions[:-count]
                anchorPoint.pop()
                count = 0
        boolArray[j][i] = True
    print(directions)