import sys, os
from socket import *
from PIL import Image, ImageTk
import time
import threading

#create socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='black')

def showPIL(pilImage):
    imgWidth, imgHeight = pilImage.size
 # resize photo to full screen
    ratio = min(w/imgWidth, h/imgHeight)
    imgWidth = int(imgWidth*ratio)
    imgHeight = int(imgHeight*ratio)
    pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.update_idletasks()
    root.update()

f = open('logfile.txt','a')

if __name__ == '__main__':

    try:

        while True:

            message, address = serverSocket.recvfrom(1024)
            print(message.decode())
            decode_message = message.decode()
            message = message.upper()
            #serverSocket.sendto(message,address)

            if decode_message == "not":
                pilImage = Image.open("floorplan_right.png")
                showPIL(pilImage)
                pilImage.close()
                serverSocket.sendto(message,address)
                time.sleep(1)
            elif decode_message == "block":
                pilImage = Image.open("floorplan_left.png")
                showPIL(pilImage)
                serverSocket.sendto(message,address)
                time.sleep(1)
                pilImage.close()
            else:
                f.write(decode_message)
                f.write("\n")


    except KeyboardInterrupt:
        f.close
        code = os.system("gsutil cp -r ./logfile.txt gs://direxit/")
