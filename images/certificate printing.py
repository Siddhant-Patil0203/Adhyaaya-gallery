from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd
import os
import shutil

col = pd.read_csv("mail.csv", error_bad_lines=False)
names = col["PARTICIPANT"]
# events = col["Event"]
# des = 'C:\\Users\\Ritesh\\Desktop\\PROJECTS\\Certificate_generator\\participants'
des1 = "C:\\Users\\acer\\Documents\\Certificate_1\\participants_final\\"

    #code wale folder mae participants folder  ka address


certificates = []
i=0

for name in names:
    img = Image.open("part.png") #certificate ke file ka naam
    img = img.convert('RGB')

    draw = ImageDraw.Draw(img)

    selectFont = ImageFont.truetype("VIVALDII.ttf", size = 100)#font ki file code wale folder mae

    message= name

    bounding_box = [76, 578, 1894, 703]
    x1, y1, x2, y2 = bounding_box  # For easy reading

    # Calculate the width and height of the text to be drawn, given font size
    w, h = draw.textsize(message, font=selectFont)

    # Calculate the mid points and offset by the upper left corner of the bounding box
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1

    # Write the text to the image, where (x,y) is the top left corner of the text
    draw.text((x, y), message, (170,147,22), align='center', font=selectFont)

    # Draw the bounding box to show that this works
    #draw.rectangle([x1, y1, x2, y2])

    
    # text1 = event
    
    # draw.text((4500,3200),text1,(0,0,0),font=selectFont)

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    sv = img.save(name + ".pdf", "PDF", resolution=100.0)
 
    source = 'C:\\Users\\acer\\Documents\\Certificate_1\\' + name + '.pdf' 

    sv1 = shutil.move(source,des1)
    
    vs = os.path.basename(sv1)

    certificates.append(vs)

# certificates.sort()
print(certificates)

# for certificate in certificates:
#     # for event in events:
#     img = Image.open('C:\\Users\\Ritesh\\Desktop\\PROJECTS\\Certificate_generator\\participants\\'+certificate)
#     draw = ImageDraw.Draw(img)

#     selectFont = ImageFont.truetype("MyriadPro-Regular.otf", size = 215)

#     text1= events[i]

#     draw.text((4500,3190), text1, (0,0,0), font=selectFont)
        
#         # text1 = event
        
#         # draw.text((4500,3200),text1,(0,0,0),font=selectFont)

#     if img.mode == 'RGBA':
#         img = img.convert('RGB')

#     base = os.path.basename('C:\\Users\\Ritesh\\Desktop\\PROJECTS\\Certificate_generator\\participants\\'+certificate)
#     st = os.path.splitext(base)[0]
#     sv = img.save(st + ".pdf", "PDF", resolution=100.0)
#     source = 'C:\\Users\\Ritesh\\Desktop\\PROJECTS\\Certificate_generator\\'+st+'.pdf'

#     sv1 = shutil.move(source,des1)
    
#     vs = os.path.basename(sv1)
#     i+=1
# print(certificates)