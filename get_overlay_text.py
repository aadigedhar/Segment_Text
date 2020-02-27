# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure"
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible
#
# You can use the snipped below (in python) to get started if you like
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
from PIL import Image, ImageFilter

def getTextOverlay(datas):
    # Write your code here for output
    ImgData = []
    for ChlData in datas:
        if ChlData[0] >= 20 and ChlData[1] >= 20 and ChlData[2] >= 20:
            ImgData.append((255, 255, 255, 255))
        else:
            ImgData.append(ChlData)
    
    img.putdata(ImgData)
    img.show()
    dilation_img = img.filter(ImageFilter.MaxFilter(5))


    return dilation_img


if __name__ == '__main__':
    img = Image.open('simpsons_frame0.png')
    img = img.convert("RGBA")
    datas = img.getdata()
    output = getTextOverlay(datas)
    
    output.save("yes2.png", "PNG")
#####################

