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
    return matrix

def createGraph(matrix, startLoc):
    matrix[startLoc[0]][startLoc[1]] = 'X'
    #conversion from sparse to dense matrix
    for x in matrix:
        
# compression algorithm

matrix2 = matrix

toBeRemoved = []

count = 0

for y in range(len(matrix2)):
    for x in range(len(matrix2[0])):
        while y + count < len(matrix2)-1 and x < len(matrix2[y+count]):
            if matrix2[y+count][x] == matrix2[y][x]:
                count+=1
            else:
                break
    for z in range(count):
        if (y+z,x) not in toBeRemoved:
            toBeRemoved.append((y+z,x))
    count = 0

toBeRemoved.reverse()
for x in toBeRemoved:
    matrix2[x[0]].pop(x[1])


count = 0

for x in matrix2:
    for y in range(len(x)):
        while y+count+1 < len(x):
            if x[y+count] == x[y]:
                count+=1
            else:
                break
        del x[y:y+count]
        count = 0

while True:
    try:
        matrix2.remove([0])
    except:
        break
