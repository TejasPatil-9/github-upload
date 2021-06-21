# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:15:55 2020

@author: tejas
"""

import cv2
import pytesseract
import os #for adding directories
import time


from PIL import Image
"""def Face():
    if __name__ == "__main__":
        TIMER = int(3) 
    
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
        # Open the camera 
        cap = cv2.VideoCapture(0) 
        cnt = 1
        while True:  
            # Read and display each frame 
            ret, img = cap.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.1,10)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2) 
            cv2.imshow('CAMERA', img) 
            # check for the key pressed 
            k = cv2.waitKey(3)   
            # set the key for the countdown to begin. Here we set q if key pressed is q 
            if k == ord('q'): 
                prev = time.time() 
        
                while TIMER >= 0: 
                    ret, img = cap.read() 
                    # Display countdown on each frame specify the font and draw the countdown using puttext 
                    font = cv2.FONT_HERSHEY_SIMPLEX 
                    cv2.putText(img, str(TIMER),  
                                (0, 50), font, 
                                2, (0, 0, 0), 
                                4, cv2.LINE_AA) 
                    cv2.imshow('CAMERA', img) 
                    cv2.waitKey(125) 
                    # current time 
                    cur = time.time() 
                    # Update and keep track of Countdown if time elapsed is one second than decrese the counter 
                    if cur-prev >= 1: 
                        prev = cur 
                        TIMER = TIMER-1
        
                else: 
                    ret, img = cap.read()
        
                    # Display the clicked frame for 2sec.You can increase time in waitKey also 
                    cv2.imshow('a', img) 
        
                    # time for which image displayed 
                    cv2.waitKey(2000) 
        
                    # Save the frame
                    img_name = "Image_{}.png".format(cnt)
                    cv2.imwrite(img_name, img)
                    print("{} Picture has been taken!".format(img_name))
                    cnt += 1
        
                    # HERE we can reset the Countdown timer if we want more Capture without closing the camera 
            # Press Esc to exit 
            elif k == 27: 
                break
        # close the camera 
        cap.release()    
        # close all the opened windows 
        cv2.destroyAllWindows()"""
    
    
    
    
def OCR():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread('Aadhar1.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    
    #detecting words
    hImg,wImg,_ = img.shape
    boxes = pytesseract.image_to_data(img)
    a=list(boxes.split("\n"))
    #print(boxes)
    main = []
    e = ""
    
    for i in range(len(a)):
      for j in range(len(a[i])):
        if a[i][j] != '\t':
          e += a[i][j]
      main.append(e)
    
    name = main[21][496:] + " " + main[22][521:]
    DOB = main[29][675:]
    gender = main[33][766:]
    aadhar = main[41][-4:] + main[42][-4:] + main[43][-4:]
    print("\n")
    print("OCR OUTPUT")
    print("Name = ",name)
    print("DOB = ",DOB)
    print("Gender = ",gender)
    print("Aadhar = ",aadhar)
    Dfile = open('Data.txt','w')
    Dfile.write(name+"\n")
    Dfile.write(DOB+"\n")
    Dfile.write(gender+"\n")
    Dfile.write(aadhar+"\n")
    Dfile.close()   
    for x,b in enumerate(boxes.splitlines()):
        if x!=0:
            b = b.split()
            #print(b)
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
                cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(50,50,255),3)
    
    imS = cv2.resize(img, (800, 800))
    
    cv2.imshow('Result',imS)
    cv2.waitKey(0)


"""    
def Speech():
    import speech_recognition as sr
    
    file1 = open("SYMPTOMS.txt","a")
    r = sr.Recognizer()
    m = sr.Microphone()

    speechData = []
    Data = ""
    sym_dataset = ['cough', 'cold', 'headache', 'pain', 'fever']
    symptoms = []

    print("\n")
    print("Speech Data")
    print("Please Start Speaking...")

    while 'stop' not in Data.split():
        with m as source:
            r.adjust_for_ambient_noise(source)
            Data = r.recognize_google(r.listen(source))
            print(">>" + Data)
            speechData.append(Data)

    for i in speechData:
        for j in sym_dataset:
            if j in i:
                file1.writelines(j + '\n')
                symptoms.append(j)



    return symptoms




def Report():
    #id=input('Enter ID :') #Tejas ->'this is where you get patient id as string'
    
    d=os.getcwd() #path of current working dir
    #d1=os.path.join(d,id) #go to particular folder
    f=os.path.join(d,'Data.txt')
    f1=os.path.join(d,'SYMPTOMS.txt')
    image1 = os.path.join(d,'Image_1.png')
    image = Image.open(image1)
    newsize=(150,120)
    image=image.resize(newsize)
    #image.show()
    
    fh=open(f,'r')
    fl=open(f1,'r')
    pos=['Name = ','Birth Date = ','Gender = ',"Aadhar No =",]
    Details=[]
    for i in fh:
        Details.append(i.strip())
    Details1=[]
    for i in fl:
        Details1.append(i.strip())
    
    
    filename=os.path.join(d,'Report.pdf')#
    documentTitle = 'Document title!'
    title = 'ABC Hospital'
    subTitle = 'Report'
    fh.close()
    
    from reportlab.pdfgen import canvas
    
    pdf = canvas.Canvas(filename)
    pdf.setTitle(documentTitle)
    
    from reportlab.pdfbase.ttfonts import TTFont #libraries
    from reportlab.pdfbase import pdfmetrics
    
    #title of Report
    pdf.setFont('Courier-Bold', 36)
    pdf.drawCentredString(300, 770, title)
    
    #subtitle of 'Report'
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290,720, subTitle)
    
    
    
    pdf.line(40, 710, 590, 710)
    
    from reportlab.lib import colors
    
    textn = pdf.beginText(46, 680)
    textn.setFont("Courier", 14)
    textn.setFillColor(colors.black)
    n=len(pos)
    for i in range(0,n-2):
        textn.textLine(pos[i]+Details[i])
    textn.textLines(pos[n-2]+Details[len(Details)-2])
    #textn.textLines("      "+Details[len(Details)-2])
    textn.textLine(pos[n-1]+Details[len(Details)-1])
    pdf.drawText(textn)
    
    pdf.line(40, 540, 590, 540)
    pdf.drawInlineImage(image, 390, 570)
    
    txt=pdf.beginText(46,520)
    txt.setFont("Courier",14)
    txt.setFillColor(colors.black)
    txt.textLine("History, Examination, Investigation, Treatment and Progress")
    pdf.drawText(txt)
    pdf.line(40,510,590,510)
    
    txt=pdf.beginText(46,490)
    txt.setFont("Courier-Bold",14)
    txt.setFillColor(colors.black)
    txt.textLine("Consultation Details")
    pdf.drawText(txt)
    
    txt=pdf.beginText(46,460)
    txt.setFont("Courier-Bold",14)
    txt.setFillColor(colors.black)
    txt.textLine("Medical History(if any) / Symptoms :")
    for i in range(len(Details1)):
        txt.textLine(Details1[i])
    pdf.drawText(txt)
    
    txt=pdf.beginText(46,395)
    txt.setFont("Courier-Bold",14)
    txt.setFillColor(colors.black)
    txt.textLine("Vitals :")
    pdf.drawText(txt)
    
    txt=pdf.beginText(46,370)
    txt.setFont("Courier-Bold",14)
    txt.setFillColor(colors.black)
    txt.textLine("LAB test :")
    pdf.drawText(txt)
    
    txt=pdf.beginText(46,320)
    txt.textLine("Medication Name")
    pdf.drawText(txt)
    
    txt=pdf.beginText(280,320)
    txt.textLine("Dosage")
    pdf.drawText(txt)
    
    txt=pdf.beginText(450,320)
    txt.textLine("Duration")
    pdf.drawText(txt)
    
    pdf.line(42,340,540,340)
    pdf.line(42,300,540,300)
    pdf.line(42,260,540,260)
    pdf.line(42,220,540,220)
    pdf.line(42,180,540,180)
    
    pdf.line(42,180,42,340)
    pdf.line(230,180,230,340)
    pdf.line(400,180,400,340)
    pdf.line(540,180,540,340)
    
    txt=pdf.beginText(46,150)
    txt.setFont("Courier-Bold",14)
    txt.setFillColor(colors.black)
    txt.textLine("Dr.XYZ")
    pdf.drawText(txt)
    doc=['MBBS,MD(specialisation)','ABC Hospital']
    txt=pdf.beginText(46,130)
    txt.setFont("Courier",14)
    txt.setFillColor(colors.black)
    for j in doc:
        txt.textLine(j)
    txt.textLine('Date = ')
    pdf.drawText(txt)
    
    
    txt=pdf.beginText(46,50)
    txt.setFont("Courier",12)
    txt.setFillColor(colors.black)
    txt.textLine("Note : Consulatation by appointment only")
    txt.textLine("Clinic No : 080-XXXXX001")
    pdf.drawText(txt)
    
    pdf.save()
    print("\n")
    print("Report has been generated.")"""
    
    
    
    
#Face()   
OCR()
#ans = Speech()
#print("Symptoms Found:", ans)
#Report()
