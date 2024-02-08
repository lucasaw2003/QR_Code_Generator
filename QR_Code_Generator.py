#import modeules
import qrcode

def main():
    #take a link as input and save it to link variable 
    link = input("Insert Link Here: ")

    #convert link to qr code
    qr_code_generator(link)

#define qr code converter
def qr_code_generator(link):
    #create qr code object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    #add the link to the qr code object
    qr.add_data(link)
    #make the qr code
    qr.make(fit=True)
    #make the qr code black fill color and white background color
    img = qr.make_image(fill_color="black", back_color="white")
    #save the image to the local computer
    img.save("qr_code.png")

main()