# DirExit
A Directional EXIT sign system that saves more lives via real time route planning and danger identification.  See more  here: https://devpost.com/software/direxit

## Inspiration
When it comes to emergencies in buildings such as fires, earthquakes or active intruders, every second counts. In the US, the number of domestic fires have gone down per year, but deaths per fire due to egress difficulties have been steadily increasing. Traditional red EXIT signs, which are the primary escape infrastructure, are stateless and do not account for pathways such as stairs becoming unusable. For people to exit premises efficiently, a real time solution needs to be implemented to account for the unexpected dangerous or blocked paths.

## What It Does 
DirExit is not just an upgraded form of the EXIT sign, but also an entirely comprehensive safety system designed to navigate human traffic out of buildings, help emergency responders assess situations, and assist in prioritizing exit routes. The physical DirExit sign can perform multiple tasks. It first has an LED indicator to signal which path to take if a person needs to escape. It will also be continuously collecting environment information through a breadth of sensors that will help indicate if a pathway is deemed unusable by fire or debris. At the same time, multiple DirExit signs which are placed in important pathways will be uploading this data to a localized server. The server then calculates the fastest route for egress within the building floor plans for each of the sign's location in real time and pushes this newly updated information back to the corresponding DirExit. The sign will then update its LED indicator if need be towards a new direction if the current path becomes blocked. In addition, all DirExit sensor data is sent to Google Cloud for further analysis which includes graphing, plotting, and visualizing fire or damage circulation. Finally, there is a real time GUI displaying the current calculated routes for a given location which will help responders assess their priorities in rescue.

![Picture2](https://github.com/MisterEddie/DirExit/blob/master/pictures/b487ac2d-005b-42d3-9b03-2efb20f6f34e_200x200.png)
![Picture2](https://github.com/MisterEddie/DirExit/blob/master/pictures/87352668_201059554586016_6301572228530044928_n.jpg)
![Picture1](https://github.com/MisterEddie/DirExit/blob/master/pictures/89056509_1502550259924155_3841543694436007936_n.jpg)
![Picture1\3](https://github.com/MisterEddie/DirExit/blob/master/pictures/dragonhacks.jpg)
![Picture1\4](https://github.com/MisterEddie/DirExit/blob/master/pictures/20200223_165714.jpg)

