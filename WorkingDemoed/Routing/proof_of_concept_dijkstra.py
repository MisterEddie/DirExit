# python -m pip install Pillow
from PIL import Image

def ingest(imageName):
    # convert image to array of rgb values
    floorplan = Image.open(imageName)
    dimensions = floorplan.size
    floorplan_rgb = floorplan.convert('RGB')
    # find walls and fill out new matrix with walls as 1 and empty space as 0
    matrix = []
    for x in range(dimensions[0]):
        matrix.append([])
        for y in range(dimensions[1]):
            if floorplan_rgb.getpixel((x,y)) == (0,0,0):
                matrix[x].append(1)
            else:
                matrix[x].append(0)
    matrix[-1][-2] = 'ENDING'
    return matrix

def findPath(arr):
    boolArray = []
    for x in range(len(arr)):
        boolArray.append([])
        for y in range(len(arr[0])):
            boolArray[x].append(False)
    directions = []
    i,j = 0,0
    anchorPoint = []
    while(j<len(arr)-2):
        # Checking down
        try:
            if (arr[j+1][i] != 'ENDING') and (arr[j][i+1] != 'ENDING') and (arr[j-1][i] != 'ENDING') and (arr[j][i-1] != 'ENDING'):
                if (int(arr[j+1][i]) + int(arr[j][i+1]) + int(arr[j-1][i]) + int(arr[j][i-1])) < 1:
                    if [j,i] not in anchorPoint:
                        anchorPoint.append([j,i])
        except:
            None
        if (arr[j+1][i] == 0) and (boolArray[j+1][i] == False):
            j+= 1
            directions.append("down")
            print('down')
            boolArray[j+1][i] = True
        # checking right next to avoid infinite loop
        elif (i< 3) and (arr[j][i+1] == 0) and (boolArray[j][i+1] == False):
            i+= 1
            directions.append("right")
            print('right')
            boolArray[j][i+1] = True
        # checking up
        elif(j>0) and (arr[j-1][i] == 0) and (boolArray[j-1][i] == False):
            j -= 1
            directions.append("up")
            print('up')
            boolArray[j-1][i] = True
        #checking left
        elif(i>0) and(arr[j][i-1] == 0) and (boolArray[j][i-1] == False):
            i -= 1
            directions.append("left")
            # print(boolArray[j][i-1])
            boolArray[j][i-1] = True
        # if no more moves/ ending is reached
        else:
            print('hi')
            if(arr[j][i] == "ENDING"):
                print("solved")
                break
            # if (boolArray[j+1][i] == False) and (boolArray[j][i+1] == False) and (boolArray[j-1][i] == False) and (boolArray[j][i-1] == False):
            #     boolArray[anchorPoint[-1][0]][anchorPoint[-1][1]] = False
                # j = anchorPoint[-1][0]
                # i = anchorPoint[-1][1]
                # anchorPoint = anchorPoint[:-2]
            else:
                print("stuck")
                break
    print(directions)


arr = [[1, 1, 1, 1],
       [1, 0, 0 ,1],
       [1, 0, 0, 1],
       [1, 1, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 1, 1],
       [1, 0, 1, 1],
       [1, 0, 0, 1],
       [1, 1, 'ENDING', 1],
       [1,1,1,1]
       ]


def findPath(arr):
    directions = []
    i,j = 0,0
    while(j<len(arr)-2):
        # Checking down
        if (j < len(arr)-2) and (arr[j+1][i] == 0):
            j+= 1
            notcheck = j
            directions.append("down")
        # checking right next to avoid infinite loop
        elif (i< 3) and (arr[j][i+1] == 0):
            i+= 1
            directions.append("right")
        # checking up
        elif(j>0) and (arr[j-1][i] == 0):
            j -= 1
            directions.append("up")
        #checking left
        elif(i>0) and(arr[j][i-1] == 0):
            i -= 1
            directions.append("left")
        # if no more moves/ ending is reached
        else:
            if(arr[j][i] == "ENDING"):
                print("solved")
            else:
                print("stuck")
            break
    return directions
